from django.db import models
from django.contrib.auth.models import *

class MyUser(AbstractUser):
	email = models.EmailField()
	first_name = models.CharField(max_length=100, unique=True)
	last_name = models.CharField(max_length=100, unique=True)
	img = models.ImageField(upload_to = 'img_profile/',default = '',verbose_name = 'Изображение для профиля:',)
	about = models.TextField(max_length=100, null=True)
	is_teacher = models.BooleanField(default=False)
	
	def __str__(self):
		return self.username

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	teacher = models.ForeignKey(MyUser, on_delete=models.CASCADE, default='')
	
	days = models.IntegerField(default=0)
	days_mounth = models.IntegerField(default=0)
	days_all = models.IntegerField(default=0)
	
	days_eat = models.IntegerField(default=0)
	
	date_change = models.DateField(auto_now=True)
	def __str__(self):
		return self.first_name + '---' + self.last_name

class clas(models.Model):
	name = models.CharField(max_length=50)
	students = models.ManyToManyField(Student, blank=True)
	teacher = models.OneToOneField(MyUser, on_delete = models.CASCADE, default='')
	def __str__(self):
		return self.name