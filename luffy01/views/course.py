# -*- coding: utf-8 -*-
# @Author: 曾辉
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSetMixin
from rest_framework.response import Response
from luffy01.models import *
from luffy01.serializers.course import *

class CourseView(ModelViewSet):
	def list(self,request,*args,**kwargs):
		'''
		课程API
		:param request:
		:param args:
		:param kwargs:
		:return:
		'''
		ret={
			"code":1000,
			"data":[],
		}
		cobj = Course.objects.all()
		qureyset = CouserSerializers(instance=cobj,many=True)

		# print(qureyset.data)
		ret["data"]=qureyset.data
		return Response(ret)

	def retrieve(self, request, *args, **kwargs):
		'''
		课程详细API
		:param request:
		:param args:
		:param kwargs:
		:return:
		'''
		ret = {
			"code": 1000,
			"data": [],
		}
		c_pk = kwargs.get('pk')
		# 这里的ID是课程ID
		cdobj = CourseDetail.objects.filter(course__id=c_pk).first()
		qureyset = CourseDetailViewSerializers(instance=cdobj, many=False)
		# print(qureyset.data)

		ret["data"].append(qureyset.data)
		return Response(ret)


class MicroView(ViewSetMixin,APIView):

	def list(self, request, *args, **kwargs):
		'''
		文章列表
		:param request:
		:param args:
		:param kwargs:
		:return:
		'''
		ret = {
			"code": 1000,
			"data": [],
		}
		article_list = Article.objects.all()
		# print(article_list)
		qureyset = ArticleSerializers(article_list,many=True)
		ret["data"] = qureyset.data
		return Response(ret)

	def retrieve(self, request, *args, **kwargs):
		'''
		文章详细
		:param request:
		:param args:
		:param kwargs:
		:return:
		'''
		ret = {
			"code": 1000,
			"data": [],
		}
		arctile_id = kwargs.get('pk')
		article_obj = Article.objects.filter(id = arctile_id).first()
		# 得到关于这个文章的所有评论
		arcticle_comment = []
		for item in article_obj.Comment_list.all():
			if not item.p_node:
				# 没有父级评论
				arcticle_comment.append({"username":item.account.nickname,"comment":item.content,
				                         "disagree_number":item.disagree_number,
				                         "agree_number":item.agree_number,"date":item.date})

		# print(article_list)
		qureyset = ArticledetialSerializers(article_obj, many=False)
		ret["data"]=qureyset.data
		ret["arcticle_comment"] = arcticle_comment
		return Response(ret)

	def create(self, request, *args, **kwargs):
		'''
		创建文章的评论
		:param request:
		:param args:
		:param kwargs:
		:return:
		'''
		ret = {
			"code": 1000,
			"comment": '',
		}

		print(request.data)
		try:
			article_id = request.data.get("article_id")
			# 要添加的具体的对象
			arctile_obj = Article.objects.filter(id=article_id).first()
			content = request.data.get("comentcontent")
			tokens = request.data.get("token")
			account = Tokeninfo.objects.filter(tokens = tokens).first().user

			# 生成评论记录
			Comment.objects.create(content_object=arctile_obj,content=content,account=account)

			#更新点赞数,收藏数
			comment_num = request.data.get("comment_num")
			agree_num = request.data.get("agree_num")
			collect_num = request.data.get("collect_num")

			Article.objects.update_or_create(id=article_id,defaults={"comment_num":comment_num,"agree_num":agree_num,"collect_num":collect_num})
			ret['comment'] = {"username":account.nickname,"comment":content}
			ret['msg'] = '评论成功'
		except Exception:
			ret["code"] = 1001
			ret['error'] = '评论失败'

		return Response(ret)