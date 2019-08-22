# -*- coding: utf-8 -*-
# @Author: 曾辉
from django.conf.urls import url
from luffy01.views import course,account
app_name = 'luffy01'

urlpatterns = [


    #第二种方式
    url(r'course/$', course.CourseView.as_view({"get":"list"})),
    url(r'course/(?P<pk>\d+)/$', course.CourseView.as_view({"get":"retrieve"})),

    #登录
    url(r'login/$', account.Login.as_view()),
    #注册
    url(r'register/$', account.register.as_view()),
	#
    url(r'micro/$', course.MicroView.as_view({"get":"list"})),
	url(r'micro/(?P<pk>\d+)/$', course.MicroView.as_view({"get": "retrieve","post":"create"})),
]