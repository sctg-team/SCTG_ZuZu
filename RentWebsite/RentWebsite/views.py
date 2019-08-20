from django.shortcuts import HttpResponse,render
from django.contrib.auth.decorators import login_required
import logging

# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')

def base(request):
    return render(request, 'base.html')


def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')

# @login_required
def index(request):
    return render(request, "bak/index1_origin.html")

# @login_required
def index2(request):
    return render(request, "repo/index2.html")

def my404(request):
    return render(request, 'repo/404.html')

def test(request):
    return render(request, 'account/login.html')


def logintest(request):
    return render(request,'account/login_teacher.html')