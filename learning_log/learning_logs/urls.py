#__author:  bluebubble
#data:2020/7/2

# from django.conf.urls import  url
from django.contrib import admin
from django.urls import path
from . import  views


urlpatterns = [
    # #主页
    # url(r'^$', views.index, name='index'),
    # path('admin/', admin.site.urls),
    # path('login/', views.login),
    path('register/', views.register),
    path('index/', views.index, name='index'),
]