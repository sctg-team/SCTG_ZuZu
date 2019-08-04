from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view_test', views.view_test,name='view_test'),
    url(r'^zoo/(\d+)', views.view_test,name='view_test'),
]