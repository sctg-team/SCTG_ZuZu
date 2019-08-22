from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.http import JsonResponse
from django.views.generic import View
from .forms import RegisterForm,LoginForm,TestUser
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
import logging
# 记日志
logger = logging.getLogger('account')

# Create your views here.
def test(request):
    return HttpResponse("功能还在测试中")


class Register(View):
    def get(self, request):
        # get方法用没有绑定数据的表单,只显示字段不显字段检测的提示信息,如该字段是必填项等
        form = RegisterForm()
        # return render(request, "account/register_teacher.html", {"form": form})
        return render(request, "register.html", {"form": form})

    # Ajax提交表单
    def post(self, request):
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax():
            # post方法绑定表单数据,这时可以检测字段并显示提示信息
            form = RegisterForm(request.POST)
            # form.is_valid()：验证表单中的数据是否合法
            # 会去form验证所有以clean开头字段名结尾的方法，如clean_moblie
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                mobile = form.cleaned_data["mobile"]
                mobile_captcha = form.cleaned_data["mobile_captcha"]
                # 手机验证码只需要存一段时间，为了减少占用用Redis缓存手机验证码
                # cache.get(mobile)???
                mobile_captcha_reids = cache.get(mobile)
                # 看手机验证码是否正确
                if mobile_captcha == mobile_captcha_reids:
                    # 添加数据到User表,用Django自带的加密函数make_password给密码加密
                    user = TestUser.objects.create(username=username, password=make_password(password))
                    user.save()
                    ret['status'] = 200
                    ret['msg'] = "注册成功"
                    logger.debug("新用户{}注册成功！".format(user))
                    # 给用户授权
                    user = auth.authenticate(username=username, password=password)
                    # 用户是否有效
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        logger.debug("新用户{}登录成功".format(user))
                    else:
                        logger.error("新用户{}登录失败".format(user))
                else:
                    # 验证码错误
                    ret['status'] = 401
                    ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = form.errors
        logger.debug("用户注册结果：{}".format(ret))
        return JsonResponse(ret)


class Login(View):
    # 当加载Login页面时
    def get(self, request):
        # 如果已登录，则直接跳转到index页面
        # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
        if request.user.is_authenticated:
            # return redirect(reverse('account:index'))
            return redirect(request.session["next"])
        form = LoginForm()
        # request.session["next"] = request.GET.get('next', reverse('account:login'))
        # 设置下一跳转地址(如果get有next,如果没有跳转到repo: index)
        request.session["next"] = request.GET.get('next', reverse('index2'))
        return render(request, "login.html", {"form": form})

    def post(self, request):
        # 表单数据绑定
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            captcha = form.cleaned_data["captcha"]
            session_captcha_code = request.session.get("captcha_code","")
            logger.debug("登录提交验证码:{}-{}".format(captcha,session_captcha_code))
            # 验证码一致
            if captcha.lower() == session_captcha_code.lower():
                user, flag = form.check_password()
                # user = auth.authenticate(username=username, password=password)
                if flag and user and user.is_active:
                    auth.login(request, user)
                    logger.info("{}登录成功".format(user.username))
                    # 跳转到next
                    return redirect(request.session.get("next", '/'))
                msg = "用户名或密码错误"
                logger.error("{}登录失败, 用户名或密码错误".format(username))
            else:
                msg = "验证码错误"
                logger.error("{}登录失败, 验证码错误".format(username))
        else:
            msg = "表单数据不完整"
            logger.error(msg)
        return render(request, "login.html", {"form": form, "msg": msg})


# @login_required
def index(requeset):
    return redirect(requeset, reverse('accounts:login'))


def logout(request):
    auth.logout(request)
    return redirect(reverse("accounts:login"))

