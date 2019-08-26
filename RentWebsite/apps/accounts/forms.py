from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.hashers import check_password as auth_check_password

"""
当表单中的数据要写入数据库或者要修改某些记录的值时，
让表单继承自ModelForm，这样可以指定某个Model并使用里面的字段创建相应的表单
"""
# 用户注册表单
class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label="密 码2",
                                widget=widgets.PasswordInput(attrs={"class": "form-control",
                                                                    "placeholder": "请再次输入密码"}))
    mobile_captcha = forms.CharField(label="验证码",
                                     widget=widgets.TextInput(attrs={"style": "padding: 15px; width: 140px;",
                                                                     "placeholder": "请输入验证码",
                                                                     "error_messages": {"invalid": "验证码错误"}}))

    class Meta:
        # fields和exclude必选选其一，exclude是排除哪些字段
        # 选择将User中的哪些字段生成表单
        model = User
        fields = ['username', 'mobile', 'password']
        widgets = {
            'username': widgets.TextInput(attrs={"class": "form-control", "placeholder": "请输入用户名"}),
            'mobile': widgets.TextInput(attrs={"class": "form-control", "placeholder": "请输入手机号"}),
            'password': widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码"}),
        }

    """
    给某个字段添加验证方法：clean_字段名
    给整个表单添加验证方法：clean
    """
    # username是否重复django会自动检查，因为它是unique的，所以不需要自己写clean_username

    # 检查手机号是否已存在
    def clean_mobile(self):
        # self.cleaned_data.get("mobile") => 获取表单上提交过来的mobile
        # 在TestUser表里过滤出mobile的值等于表单提交过来的mobile值 => ret
        # 注意，用get()方法一定要有返回值，否则会引发异常
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    # 检查密码复杂度
    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("密码不能全是数字")

    def clean(self):
        """
        验证两次输入的密码是否一致
        对整个表单验证时，不需要有返回值
        """
        if self.cleaned_data.get("password") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")


"""
ModelForm对于unique字段会检查是否已经存在，如果存在，is_valid结果会为False
所以登录功能不适合继承自ModelForm，只能继承自Form自定义表单元素
"""
# 用户登录表单
class LoginForm(forms.Form):
    username_login = forms.CharField(label="用户名", max_length="24",
                               widget=widgets.TextInput(attrs={"class": "form-control",
                                                               "placeholder": "用户名"}))
    captcha = forms.CharField(label="验证码",
                              widget=widgets.TextInput(attrs={"style": "width: 160px;padding: 10px",
                                                              "placeholder": "验证码",
                                                              "onblur": "check_captcha()",
                                                              "error_messages": {"invalid": "验证码错误"}}))
    password_login = forms.CharField(label="密 码",
                               widget=widgets.PasswordInput(attrs={"class": "form-control",
                                                                   "placeholder": "密码"}))

    def check_password(self):
        # 接收从表单传过来的用户名和密码
        """
        问题：HTML上的是context_processor传过去的表单，可这里收不到HTML提交的数据
        已解决，给form表单定义一个id，通过ajax里的data: $("#id").serialize()传过来
        """
        username = self.cleaned_data['username_login']
        password = self.cleaned_data['password_login']
        try:
            # 注意，用get()方法一定要有返回值，否则会引发异常（用try...except...自己引发异常）
            user = User.objects.get(username=username)
            # 用Django自带的auth_check_password检查密码是否正确，它可以对明文和密文进行对比
            return user, auth_check_password(password, user.password)
        except:
            return None, False

    def clean_username(self):
        ret = User.objects.filter(username=self.cleaned_data.get("username_login"))
        if ret:
            return self.cleaned_data.get("username_login")
        else:
            raise ValidationError("用户名或密码不正确")
