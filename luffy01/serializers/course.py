# -*- coding: utf-8 -*-
# @Author: 曾辉

from rest_framework import serializers
from luffy01.models import *


class CouserSerializers(serializers.ModelSerializer):
	'''
	课程的序列化
	'''
	#自定义的字段

	#source为表里面的所有字段
	level = serializers.CharField(source='get_level_display') #自动的帮你添加()
	course_type = serializers.CharField(source='get_course_type_display')

	class Meta:
		model = Course
		fields = ["id",'name',"course_img","course_type","brief","level","period"]
		# depth=2  用深度帮你进行跨表


class CourseDetailViewSerializers(serializers.ModelSerializer):
	'''
	详细课程的序列化
	'''
	#一对一的反向查询，fk,choice都是用source,只能取一条或者是一个数据
	name = serializers.CharField(source='course.name')
	img = serializers.CharField(source='course.course_img')
	content = serializers.CharField(source='course.brief')
	id = serializers.CharField(source='course.id')

	#多对多的，用SerializerMethodField(),可以获取多个

	#推荐课程
	recommend_courses = serializers.SerializerMethodField()
	#老师
	teachers= serializers.SerializerMethodField()
	# 每个时间段的价格
	price = serializers.SerializerMethodField()

	# 课程大纲
	course_detail = serializers.SerializerMethodField()

	#课程章节
	coursechapter = serializers.SerializerMethodField()
	#
	# #课时目录
	# coursesection = serializers.SerializerMethodField()

	# 推荐课程
	def get_recommend_courses(self,obj):  #obj-->  CourseDetail.obj
		# obj.recommendcourse.all()
		return [{"id":item.id,"title":item.name}for item in obj.recommend_courses.all()]

	def get_teachers(self,obj):  #obj-->  CourseDetail.obj
		# obj.recommendcourse.all()
		return [{"id":item.id,"name":item.name,"title":item.title}for item in obj.teachers.all()]
	# 每个时间段的价格
	def get_price(self,obj):
		return [{"valid_period":item.get_valid_period_display(),"price":item.price}for item in obj.course.price_policy.all()]

	def get_course_detail(self,obj):
		return [{"title":item.title,"content":item.content}for item in obj.courseoutline_set.all()]

	def get_coursechapter(self,obj):
		return [{"chapter":item.chapter,"title":item.name,"summarys":item.summary}for item in obj.course.coursechapters.all()]

	# def get_coursesection(self,obj):
	# 	return [{"chapter":item.chapter,"name":item.name,"summary":item.summary}for item in obj.course.coursechapters.coursesections.all()]

	class Meta:
		model = CourseDetail

		fields = ["id","name","img","hours","teachers","content",'why_study',"what_to_study_brief",
		          "career_improvement","prerequisite","recommend_courses","price",'course_detail','coursechapter',]

class ArticleSerializers(serializers.ModelSerializer):
	'''
	文章的序列化
	'''
	#自定义的字段

	#source为表里面的所有字段
	source = serializers.CharField(source='source.name') #自动的帮你添加()
	position = serializers.CharField(source='get_position_display')


	class Meta:
		model = Article
		fields = ["id",'title',"source","brief","head_img","content","comment_num",
		          "agree_num","collect_num","position"]
		# depth=2  用深度帮你进行跨表

class ArticledetialSerializers(serializers.ModelSerializer):

	'''
	详细文章的序列化
	'''

	source = serializers.CharField(source='source.name')  # 自动的帮你添加()




	class Meta:
		model = Article
		fields = ["id", 'title', "source", "head_img", "content", "comment_num",
		          "agree_num", "collect_num"]