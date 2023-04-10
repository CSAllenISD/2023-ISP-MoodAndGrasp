from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from rest_framework.views import APIView
from rest_framework.response import Response
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field
from django.http import JsonResponse
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

def slider_view(request):
    if request.method == 'POST':
        form = SliderForm(request.POST)
        if form.is_valid():
            slider_value = form.cleaned_data['slider']
            slider_value.save()
            # Do something with the slider value, like save it to a database
            return redirect('success')
    else:
        form = SliderForm()

    return render(request, 'chartjs/survey.html', {'form': form})

def success_view(request):
    return render(request, 'users/classroom.html')

class SurveyCreateView(CreateView):
    model = SurveyQuestion
    template_name = 'chartjs/survey.html'
    form_class = SurveyQuestionForm
    success_url = reverse_lazy('survey_results')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        questions = list(SurveyQuestion.objects.all())
        random.shuffle(questions)
        kwargs.update({'questions': questions[:8], 'initial': {'question': 'sample question'}})
        return kwargs

class SurveyResultsView(View):
    def get(self, request, *args, **kwargs):
        survey_responses = SurveyResponse.objects.all()
        return render(request, 'chartjs/survey_results.html', {'survey_responses': survey_responses})

class SliderView(FormView):
    form_class = SurveyQuestionForm
    template_name = 'chartjs/survey.html'
    success_url = reverse_lazy('success')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['questions'] = SurveyQuestion.objects.all()
        return kwargs

def survey_view(request):
    questions = SurveyQuestion.objects.all()
    form = SurveyQuestionForm(questions=questions)
    if request.method == 'POST':
        form = SurveyQuestionForm(request.POST, questions=questions)
        if form.is_valid():
            form.save()
            # do something with the form data
            return redirect('success')
    return render(request, 'survey.html', {'form': form})