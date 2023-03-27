from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Classroom
from home.models import Announcements
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	     
		def clean_email(self):
			email = self.cleaned_data['email']
		#	if User.objects.filter(email=email).exists():
				
			#	raise forms.ValidationError('That email is in use. Please Log in or use a different Email')
			return email

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

class ClassJoinForm(forms.ModelForm):
	class Meta:
		model = Classroom
		fields = ['classroom']



