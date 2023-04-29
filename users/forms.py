from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Classroom
from home.models import Announcements
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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

class TeacherRegisterForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['is_teacher']
		labels = {"is_teacher": "Are you a teacher?"}

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'theme']

class ClassJoinForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['user_class_code']

		def clean_user_class_code(self):
			user_class_code = self.cleaned_data['user_class_code']
			return user_class_code
			
	user_class_code = forms.CharField(
		label = "Enter the Class Code",
		max_length = 80,
		required = True,
	)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-exampleForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		self.helper.add_input(Submit('submit', 'Submit'))

	

