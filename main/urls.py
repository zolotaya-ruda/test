from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
	#path('teachers_cabinet/add-student', AddStudent.as_view(), name='add_student'),
	path('', main, name='main'),
	path('main/<str:pk>', days_plus, name='days_plus'),
	path('teachers_cabinet/add-class', AddClass.as_view(), name='add_class'),
	path('teachers_cabinet/', cabinet, name='cabinet'),
	path('teachers_cabinet/add-student-to-class/<str:pk>', add_student_to_class, name='add-student-to-class'), # добавление ученика в класс
	path('teachers_cabinet/plus-day/<str:pk>', plus, name='plus'),
	path('teachers_cabinet/add_student', AddStudent.as_view(), name='add_student'),
	path('teachers_cabinet/minus-day/<str:pk>', minus, name='minus'),
	path('teachers_cabinet/plus-day-eat/<str:pk>', plus_eat, name='plus_day_eat'),
	path('teachers_cabinet/minus-day-eat/<str:pk>', minus_eat, name='minus_day_eat'),
	path('teachers_cabinet/changing', changing, name='changing'),
]