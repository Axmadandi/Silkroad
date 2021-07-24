from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
	ListView,
	DetailView,
	View,)
from .models import *

class HomePageView(View):
	def get(self,request):
		recent_add = Blog.objects.all().order_by('-id')[:3]
		teachers = Teacher.objects.all().order_by('-id')
		context = {
			'recent_add':recent_add,
			'teachers':teachers,
			}
		return render(request,'index.html',context)

class TeacherView(ListView):
	def get(self,request):
		blogs = Teacher.objects.all()
		context = {
			'blogs':blogs,
		}
		return render(request, 'teacher.html',context)

class CourseView(ListView):
	def get(self,request):
		blogs = Cours.objects.all()
		context = {
			'blogs':blogs,
		}
		return render(request, 'course.html',context)

def courseDetail(request, course_slug):
	blogs = Cours.objects.get(slug=course_slug)

	context = {
		'blogs':blogs,
	}
	return render(request,'course_detail.html',context)

class BlogView(View):
	def get(self,request):
		blogs = Blog.objects.all()
		context = {
			'blogs':blogs,
		}
		return render(request, 'blog.html',context)

def teacherDetail(request, teacher_slug):
	blogs = Teacher.objects.get(slug=teacher_slug)

	context = {
		'blogs':blogs,
	}
	return render(request,'teacher_detail.html',context)

def blogDetail(request, blog_slug):
	detail = Blog.objects.get(slug=blog_slug)

	context = {
		'detail':detail,
	}
	return render(request,'blog_detail.html',context)

def categoryDetail(request,category_slug):
	category = get_object_or_404(Category,slug=category_slug)
	blogs = Blog.objects.filter(category=category)
	context = {
		'blogs':blogs
	}
	return render(request, 'category_detail.html', context)

def authorDetail(request,author_slug):
	author = get_object_or_404(Author,slug=author_slug)
	blogs = Blog.objects.filter(author=author)
	context = {
		'blogs':blogs
	}
	return render(request, 'category_detail.html', context)


def contact(request):
	if request.method=="POST":
		contact = Contact()
		name = request.POST.get('name')
		message = request.POST.get('message')
		tel = request.POST.get('tel')
		contact.name=name
		contact.message=message
		contact.tel=tel
		contact.save()
		return render(request,'contact.html')
	return render(request,'contact.html')