from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import *
import random
from random import sample

class SurveyForm(forms.ModelForm):
    mood = forms.IntegerField(required=False)
    grasp = forms.IntegerField(required=False)
    
    class Meta:
        model = SurveyQuestion
        fields = ['question']
    
    def clean(self):
        cleaned_data = super().clean()
        mood_score = 0
        grasp_score = 0
        for key, value in cleaned_data.items():
            if key.startswith('mood_'):
                mood_score += int(value)
            elif key.startswith('grasp_'):
                grasp_score += int(value)
        cleaned_data['Mood'] = mood_score
        cleaned_data['Grasp'] = grasp_score
        return cleaned_data
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))