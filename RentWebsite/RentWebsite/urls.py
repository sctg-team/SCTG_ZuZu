"""RentWebsite URL Configuration

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
from django.conf.urls import url,include,handler404,handler500
from django.contrib import admin
from . import views
from .settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',include('apps.account.urls',namespace="account")),
    # 首页
    url(r'^$',views.index2 ,name="index2"),
    # 用户登录注册
    url(r'^accounts/',include('apps.accounts.urls',namespace='accounts')),
    # 接口
    url(r'^apis/',include('apps.apis.urls',namespace='apis')),
    # 用户中心
    url(r'^uc/', include('apps.uc.urls', namespace='uc')),
    # 商品库
    url(r'^goods/', include('apps.goods.urls', namespace='goods')),
    # media 处理
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
    # ckeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # base页面
    url(r'^base/$', views.base, name='base'),
    # 日志测试
    url(r'^logtest/$', views.logtest, name='logtest'),
    # 首页
    url(r'^index/', views.index, name='index1'),
]
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = views.my404