# @Time : 2020/6/20 11:49 
# @Author : JunHong
# @File : url.py 

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
]
