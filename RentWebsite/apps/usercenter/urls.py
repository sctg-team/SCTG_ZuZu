from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # 修改个人资料
    url(r'^profile/change$', views.uc_profile, name='profile_change'),
    # 修改密码
    url(r'^password/$', views.test, name='passwd_change'),
    # 我的收藏
    url(r'^collect/$', views.test, name='collect'),
]