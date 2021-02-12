from django.shortcuts import render
from .models import * 
import datetime
from django.http import *
from django.views.generic import *
from .forms import *
import json

def error_404(request, exception):
    return render(request,'main/404.html')

def error_403(request, exception):
    return render(request,'main/403.html')

def error_400(request, exception):
    return render(request,'main/400.html')

def error_500(exception):
    return render(request,'main/500.html')

data = [
    { 'url': 'ya.ru', 'name': 'yandex' }, 
    {'url': 'google.com', 'name': 'google'}
]
print(data)
print(json.dumps(data))
def main(request):
	classes = clas.objects.all()
	date = datetime.datetime.now()
	counts = Student.objects.filter(days=1).count()
	counts_all = Student.objects.count()
	month_name = date.strftime('%B')
	counts_eat = Student.objects.filter(days_eat=1).count()
	context = {
			'date': date, 
			'counts': counts, 
			'classes': classes, 
			'counts_all': counts_all, 
			'month_name': month_name,
			'counts_eat': counts_eat
			}
	return render(request, 'main/main_1.html', context)

def days_plus(request, pk):
	
	a = Student.objects.get(id=pk)
	if a.days == 0:
		a.days = a.days + 1
		a.save()
	else:
		a.days = a.days - 1
		a.save()
	return HttpResponseRedirect('/teachers_cabinet/')


def add_user(request):
	template_name = 'main/cabinet.html'
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.teacher = request.user
			form.save()
	else:
		form = StudentForm
	return render(request, 'main/cabinet_form.html', {'form': form})

class AddStudent(CreateView):
	model = Student
	fields = ('first_name','last_name',)
	success_url = '/teachers_cabinet'
	def form_valid(self, form):
		form.instance.teacher = self.request.user
		form.instance.clas = self.request.user.clas
		return super().form_valid(form)

class AddClass(CreateView):
	model = clas
	fields = ('name',)
	success_url = '/main'
	def form_valid(self, form):
		form.instance.teacher = self.request.user
		return super().form_valid(form)

def cabinet(request):
	
	
	add_user(request)
	user = MyUser.objects.get(id=request.user.id)
	date = datetime.datetime.now()
	classes = clas.objects.all()
	
	for student in user.student_set.all():
		print(student.date_change.strftime('%d'))
		print((date.day) == int(student.date_change.strftime('%d')))
		print('date', date.month, int(student.date_change.strftime('%m')))
		if date.month >  int(student.date_change.strftime('%m')):
			student.days_mounth = 0
			student.save()
		if date.day > int(student.date_change.strftime('%d')):
			
			student.days_mounth = student.days_mounth + 1
			student.days_all = student.days_all + 1
			student.days = 0
			student.days_eat = 0
			student.save()
	
	counts = Student.objects.filter(days=1).count()
	counts_all = Student.objects.count()
	counts_eat = Student.objects.filter(days_eat=1).count()
	classes = clas.objects.get(teacher=request.user)
	students = Student.objects.filter(teacher=request.user)
	
	context = {
		'classes': classes,
		'students': students,
		'counts': counts,
		'counts_all': counts_all,
		'counts_eat': counts_eat
	}

	return render(request, 'main/siter.html', context)
def changing(request):
	
	students = Student.objects.filter(teacher=request.user)

	context = {
		'students': students
	}

	return render(request, 'main/cabinet_form.html', context) 

def add_student_to_class(request, pk):
	students = Student.objects.get(id=pk)
	classes = clas.objects.get(teacher=request.user)
	if students in classes.students.all():
		classes.students.remove(students)
		classes.save()
		return HttpResponseRedirect('/teachers_cabinet')
	else:
		classes.students.add(students)
		classes.save()
		return HttpResponseRedirect('/teachers_cabinet')

def plus(request, pk):
	student = Student.objects.get(id=pk)
	student.days = student.days + 1
	student.save()
	data = {
	'value': student.days,
	
	}
	return HttpResponseRedirect('/teachers_cabinet/changing')
	

def minus(request, pk):
	student = Student.objects.get(id=pk)
	student.days = student.days - 1
	student.save()
	return HttpResponseRedirect('/teachers_cabinet/changing')

def plus_eat(request, pk):
	student = Student.objects.get(id=pk)
	student.days_eat = student.days_eat + 1
	student.save()
	return HttpResponseRedirect('/teachers_cabinet/changing')

def minus_eat(request, pk):
	student = Student.objects.get(id=pk)
	student.days_eat = student.days_eat - 1
	student.save()
	return HttpResponseRedirect('/teachers_cabinet/changing')