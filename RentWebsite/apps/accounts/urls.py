"""question_repo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # 注册
    url(r'register/$', views.Register.as_view(), name="register"),
    # 登录
    url(r'login/$', views.Login.as_view(), name="login"),
    # 退出
    url(r'logout/$', views.logout, name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.test, name="passwd_forget"),
    # 重置密码
    url(r'password/reset/$', views.test, name="passwd_reset"),
    # 帐户信息
    url(r'profile/$', views.test, name="profile"),
    # 用户列表
    url(r'users/$', views.test, name="user_list"),
    # 添加用户
    url(r'user/$', views.test, name="user_add"),
]
