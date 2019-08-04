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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logtest/$', views.logtest, name='logtest'),
    url(r'^index/',views.index,name='index1'),
    url(r'^index2/',views.index2,name='index2'),
    url(r'^accounts/',include('apps.accounts.urls',namespace='accounts')),
    url(r'^apis/',include('apps.apis.urls',namespace='apis')),
    url(r'^uc/',include('apps.usercenter.urls',namespace='uc')),
    url(r'^django_view/',include('apps.django_view.urls',namespace='django_view')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.my404