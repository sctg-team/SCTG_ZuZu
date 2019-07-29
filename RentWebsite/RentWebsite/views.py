from django.shortcuts import HttpResponse,render
import logging

# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')

def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')

def index(request):
    return HttpResponse('这是index页面')
    # return render(request,"index.html")
def index2(request):
    # return render(request,"index2.html")
    return HttpResponse('这是index2页面')