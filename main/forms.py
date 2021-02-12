from .models import *
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import *



StudentForm = modelform_factory(Student,
	fields=('first_name', 'last_name')
	)
	