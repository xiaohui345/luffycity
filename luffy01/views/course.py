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
			# 区别一下哪些是子评论和 根评论
			try:
				p_id = item.p_node.id
				# 父评论的数据
				p_comment={
					"username":item.p_node.account.nickname,
					'comment':item.p_node.content
				}

			except Exception:
				p_id = False
				p_comment={}
			arcticle_comment.append({"id":item.id,"username":item.account.nickname,"comment":item.content,
			                         "disagree_number":item.disagree_number,
			                     "agree_number":item.agree_number,"date":item.date,"p_id":p_id,"p_comment":p_comment})


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
			#父评论的ID
			p_node = request.data.get("p_node")
			print(account,arctile_obj)
			if p_node:
				#子评论
				# 先找到'\n'的索引位置
				nindex = content.index('\n')
				# 那'\n'的索引位置的后面的数据才是真正的内容。
				new_content = content[nindex + 1:]
				comment_obj = Comment.objects.create(content_object=arctile_obj,content=new_content,account=account,p_node_id=p_node)
			else:
				# 根评论
				# 生成评论记录
				comment_obj = Comment.objects.create(content_object=arctile_obj, content=content, account=account)

			ret['comment'] = {"username":account.nickname,"comment":content,"date":comment_obj.date}
			ret['msg'] = '评论成功'
		except Exception:
			ret["code"] = 1001
			ret['error'] = '评论失败'

		return Response(ret)

# 对字段进行操作，需要用F包起来；
from django.db.models import F
class UpdownView(APIView):
	def post(self,request,*args,**kwargs):
		ret = {
			"code": 1000,
			"data" : {"status":True,"msg": "",}
		}
		article_id = request.data.get("article_id")
		arctile_obj = Article.objects.filter(id=article_id).first()
		tokens = request.data.get("token")
		account = Tokeninfo.objects.filter(tokens=tokens).first().user
		isUp = request.data.get("isup")  # 已经反序列化为true了
		# print(isUp)
		try:
			ArticleUpDown.objects.create(article = arctile_obj,user = account,is_up=isUp)
			if isUp:
				# 表示点赞数
				Article.objects.filter(pk=article_id).update(agree_num=F("agree_num") + 1)
			#否则是踩数加1
			# else:
			# 	Article.objects.filter(pk=article_id).update(up_count=F("agree_num") + 1)
		except Exception:
		#已经点赞过了
			ret["data"]["status"] = False
# 如果有点赞或是踩的时候需要判断一下，用户第一次的操作，是点赞还是踩，然后才返回提示（点赞过或是踩过）在这么只有点赞，所以没有补充
			ret["data"]["msg"] = "已经点赞过了"
		return Response(ret)

from django.contrib.contenttypes.models import ContentType

class CollectionView(APIView):
	def post(self,request,*args,**kwargs):

		ret={
			"code":1000,
			"msg":'',
			"collections":True,
		}

		article_id = request.data.get("article_id")
		arctile_obj = Article.objects.filter(id=article_id).first()
		tokens = request.data.get("token")
		account = Tokeninfo.objects.filter(tokens=tokens).first().user
		print(ret,account,arctile_obj)
		try:
			# 收藏成功
			Collection.objects.create(content_object = arctile_obj,account = account)
			#收藏数加1

			Article.objects.filter(pk=article_id).update(collect_num=F("collect_num") + 1)

			ret["msg"] = "收藏成功"


		except Exception:
			#这里报错就相当于在点击了一次收藏，即取消收藏
			Article.objects.filter(pk=article_id).update(collect_num=F("collect_num") - 1)

			str_model = Article._meta.model_name

			Collection.objects.filter(content_type = ContentType.objects.get(model=str_model),object_id=article_id,account = account).delete()

			ret["msg"] = "取消收藏"
			ret["collections"] = False


		return Response(ret)