from django.shortcuts import HttpResponse,render
import logging

# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')

def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')

def index(request):
    return render(request, "index1_origin.html")

def index2(request):
    return render(request, "repo/index2.html")