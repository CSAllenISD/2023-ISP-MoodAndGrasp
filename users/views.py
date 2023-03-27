from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.forms import ValidationError
from django.contrib.auth.models import User
from django import forms
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			if User.objects.filter(email=form.cleaned_data.get('email')).exists():
	#			raise forms.ValidationError('That email is in use. Please Log in or use a different Email')
				messages.error(request, f'That email is in use. Please Log in or use a different Email', extra_tags='error')
			else:
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Your account has been created! You are now able to log in')
				return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form

	}
	return render(request, 'users/profile.html', context)
def classes(request):
	c_form = None
	if request.method == 'POST':
		c_form = ClassJoinForm(request.POST, instance=request.user)
		if c_form.is_valid():
			c_form.save()
		else:
			c_form = ClassJoinForm(instance=request.user)
	return render(request, 'users/classes.html', {'c_form':c_form})

