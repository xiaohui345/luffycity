# -*- coding: utf-8 -*-
# @Author: 曾辉
from django.utils.deprecation import MiddlewareMixin

class CorsMidleware(MiddlewareMixin):

	def process_response(self,request,response,*args,**kwargs):
		# 给最后的响应加上 跨域的请求头
		response['Access-Control-Allow-Origin'] = '*'

		#允许你携带CONTENT-Type请求头
		response['Access-Control-Allow-Headers'] = 'Content-Type'

		return response