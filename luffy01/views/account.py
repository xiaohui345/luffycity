# -*- coding: utf-8 -*-
# @Author: 曾辉
from rest_framework.views import APIView
from rest_framework.response import Response
from luffy01.models import Userinfo, Tokeninfo
import uuid


class Login(APIView):
	# def options(self, request, *args, **kwargs):
	# 当跨域是复杂请求的时候，浏览器先给你发送一个options预检的请求，
	# 然后预检通过后再给你发送你实际要发送的请求(post),
	# 因此还必须带着Access-Control-Allow-Origin请求头，让你请求通过。这样麻烦才写到中间件去。
	# 预检实际上就是检查你的请求头上是否有
	# 允许你的域名来获取我的数据
	# response["Access-Control-Allow-Origin"] = "*"
	#
	# 允许你携带CONTENT-Type请求头
	# response['Access-Control-Allow-Headers'] = 'Content-Type'
	# 允许你发送DELETE,PUT
	# response['Access-Control-Allow-Methods'] = 'DELETE,PUT'
	# return Response
	def post(self, request, *args, **kwargs):
		print(request.data)
		ret = {
			"code": 1000,
			"data": {"token":'',
			         'nickname': '', }
		}
		user = Userinfo.objects.filter(**request.data).first()
		if user:
			token = str(uuid.uuid4())
			# 没有就创建，有就更新;
			Tokeninfo.objects.update_or_create(user=user, defaults={"tokens": token})
			ret["data"]["token"] = token
			ret["data"]["nickname"] = user.nickname
		else:
			ret["code"] = 10001
			ret["erorr"] = "账号或密码错误"
		return Response(ret)

class register(APIView):
	def post(self,request,*args,**kwargs):

		ret = {
			"code": 1000,
			"data": {"token":'',
			         'nickname': '', }
		}

		# print(request.data)
		user = Userinfo.objects.create(**request.data)
		if user:
			token = str(uuid.uuid4())
			# 没有就创建，有就更新;
			Tokeninfo.objects.update_or_create(user=user, defaults={"tokens": token})
			ret["data"]["token"] = token
			ret["data"]["nickname"] = user.nickname
		else:
			ret["code"] = 1001
			ret["erorr"] = "账号不可用"

		return Response(ret)