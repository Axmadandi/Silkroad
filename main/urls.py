from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.HomePageView.as_view() , name='home'),
    path('teacher/',views.TeacherView.as_view() , name='teacher'),
    path('course/',views.CourseView.as_view() , name='course'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.BlogView.as_view(),name='blog'),
    path('teacher/<slug:teacher_slug>/',views.teacherDetail, name='teacher_detail'),
    path('course/<slug:course_slug>/',views.courseDetail, name='course_detail'),
    path('blog/<slug:blog_slug>/',views.blogDetail, name='blog_detail'),
    path('category/<slug:category_slug>/', views.categoryDetail,name='category_detail'),
    path('author/<slug:author_slug>/', views.authorDetail,name='author_detail'),
    path('accounts/profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),

    
  
]
