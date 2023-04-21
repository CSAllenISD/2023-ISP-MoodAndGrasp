from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field, Submit
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *
import pandas as pd
import random
from random import choice
# Create your views here.

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
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartjs/index.html')

class SliderForm(SurveyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['mood', 'grasp', 'question']:
            self.fields.pop(field_name)

class SurveyCreateView(LoginRequiredMixin, CreateView):
    model = SurveyQuestion
    form_class = SurveyForm
    template_name = 'chartjs/survey.html'
    success_url = reverse_lazy('front_page')
    def get_context_data(self, **kwargs):
        mood_question = SurveyQuestion.objects.filter(mood_question=True).order_by("?")[:4]
        grasp_question = SurveyQuestion.objects.filter(grasp_question=True).order_by("?")[:4]
        
        context = super().get_context_data(**kwargs)
        context['mood_questions'] = mood_question
        context['grasp_questions'] = grasp_question

        return context

    def form_valid(self, form):
        survey = form.save(commit=False)
        survey.student = self.request.user.student
        survey.save()
#        change.Mood = survey.cleaned_data.get('Mood')
#        change.Mood = survey.cleaned_data.get('Grasp')
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Process form cleaned data
            change = Student.objects.get(user=self.request.user)
            print(self.request.POST.get('mood'))
            change.Mood = request.GET.get('mood', None)
            change.Grasp = request.GET.get('grasp', None)
            return HttpResponseRedirect('../classes')
        else:
            print(form)
        return render(request, self.template_name, {'form': form})

@login_required
def survey(request):
    student = Student.objects.all()
    if request.POST:
        s_form = SurveyForm(request.POST, instance=request.user.student)
        if s_form.is_valid():
            s_form.save()
            change = Student.objects.get(user=request.user)
            print(request.POST.get('mood', None))
            change.Mood = request.POST.get('mood', None)
            change.Grasp = request.POST.get('grasp', None)
            messages.success(request, f'Your data have been recorded!!')
            return JsonResponse({"mood":change.Mood, "grasp":change.Grasp}, status=200)
        else:
            messages.error(request, f'Something came up idk what happend', extra_tags='error')
            return JsonResponse(status=400)
    else:
        s_form = SurveyForm(request.POST, instance=request.user.student)
        change = Student.objects.get(user=request.user)

    mood_question = SurveyQuestion.objects.filter(mood_question=True).order_by("?")[:4]
    grasp_question = SurveyQuestion.objects.filter(grasp_question=True).order_by("?")[:4]

    context = {
        'mood_questions': mood_question,
        'grasp_questions': grasp_question,
        'form': s_form,
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

class SurveyFormView(FormView):
    template_name = 'chartjs/survey.html'
    form_class = SurveyForm
    success_url = reverse_lazy('survey_results')

    def form_valid(self, form):
        user = self.request.user
        mood = user.mood
        grasp = user.grasp
        mood_change = form.cleaned_data['mood_slider']
        grasp_change = form.cleaned_data['grasp_slider']
        mood += mood_change
        grasp += grasp_change
        user.mood = mood
        user.grasp = grasp
        user.save()
        return super().form_valid(form)

def testing(request):
    result = request.GET.get('result', None)
    return JsonResponse()