from django.conf.urls import url
from . import views

urlpatterns = [
    # 获取手机验证码
    url(r'^get_mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    # 得到验证码
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    # 检查验证码
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
]