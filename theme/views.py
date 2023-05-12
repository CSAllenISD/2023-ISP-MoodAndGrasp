from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ClassJoinForm, TeacherRegisterForm
from django.forms import ValidationError
from django.contrib.auth.models import User
from django import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from chartjs.models import *
from users.models import *

def home(request):
    return render(request, 'home.html')

def baseView(request):
    return render(request, "classroom.html")

def register(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            r_form = UserRegisterForm(request.POST)
            t_form = TeacherRegisterForm(request.POST)
            if r_form.is_valid() and t_form.is_valid():
                r_form.save()
                t_form.save()
                messages.success(request, f'Your account has been created!')
                return redirect('front_page')
    else:
        r_form = UserRegisterForm(request.POST)
        t_form = TeacherRegisterForm(request.POST)
    context = {
        'r_form': r_form,
        't_form': t_form,
    }
    return render(request, 'register.html', context)

@login_required
def profile_view(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile_view')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form

	}
	return render(request, 'profile_view.html', context)

@login_required
def survey(request):
    student = Student.objects.all()
    mood_question = SurveyQuestion.objects.filter(mood_question=True).order_by("?")[:4]
    grasp_question = SurveyQuestion.objects.filter(grasp_question=True).order_by("?")[:4]

    context = {
        'mood_questions': mood_question,
        'grasp_questions': grasp_question,
        'student': student
    }
    return render(request, 'chartjs/survey.html', context)

def surveySubmit(request, mood=int, grasp=int):
    s = Student.objects.get(user=request.user)
    s.Mood = mood
    s.Grasp = grasp
    s.save()

    context = {
        'mood_average': mood,
        'grasp_average': grasp,
    }
    return render(request, 'chartjs/surveySubmit.html', context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        labels = [
            'January',
            'February', 
            'March', 
            'April', 
            'May', 
            'June', 
            'July'
            ]
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        scatterdata = []
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'graph.html')


def classes(request):
    student = Student.objects.get(user=request.user)
    context = {
        'class_group': student.student_classroom.all()
    }
    return render(request, 'classes.html', context)