#__author:  bluebubble
#data:2020/7/2

from django.conf.urls import  url

from . import  views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index')
]