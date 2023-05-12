from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ClassJoinForm, TeacherRegisterForm
from django.forms import ValidationError
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Classroom
from chartjs.models import Student
import os
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		form_teacher = TeacherRegisterForm(request.POST)
		if form.is_valid():
			if User.objects.filter(email=form.cleaned_data.get('email')).exists():
	#			raise forms.ValidationError('That email is in use. Please Log in or use a different Email')
				messages.error(request, f'That email is in use. Please Log in or use a different Email', extra_tags='error')
			else:
				form.save()
				form_teacher.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Your account has been created! You are now able to log in')
				return redirect('login')
	else:
		form = UserRegisterForm()
		form_teacher = TeacherRegisterForm()
	return render(request, 'users/register.html', {'form':form, 'form_teacher':form_teacher})



@login_required
def classes(request):
	if request.method == 'POST':
		c_form = ClassJoinForm(request.POST, instance=request.user.profile)
		if c_form.is_valid():
			if Classroom.objects.filter(class_code=c_form.cleaned_data.get('user_class_code')).exists():
				c_form.save()
				code = Student.objects.get(user=request.user)
				code.student_classroom.set(Classroom.objects.filter(class_code=c_form.cleaned_data.get('user_class_code')))
				messages.success(request, f'You have joined the classroom!')
				return redirect('front_page')
			else:
				messages.error(request, f'No Classroom found with that code', extra_tags='error')
	else:
		c_form = ClassJoinForm(request.POST, instance=request.user.profile)
		code = Student.objects.get(user=request.user)
	context = {
		'c_form': c_form,
		'student_classroom':code.student_classroom.first(),
		'student_classroom_check':code.student_classroom.exists()
	}
	return render(request, 'users/classes.html', context)


