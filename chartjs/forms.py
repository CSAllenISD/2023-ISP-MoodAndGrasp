from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import *
import random
from random import sample


class SurveyQuestionForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestion
        fields = []
    def __init__(self, *args, **kwargs):
        self.questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'

        initial_questions = sample(self.questions, 8)
        for i in range(8):
            self.fields[f'question_{i+1}'] = forms.IntegerField(
                label=initial_questions[i].question,
                widget=forms.NumberInput(attrs={
                    'type': 'range',
                    'min': '1',
                    'max': '5',
                    'step': '1',
                    'oninput': 'updateSliderColor(this)',
                    'class': 'slider'
                })
            )

    def save(self, user):
        for i in range(8):
            question = self.questions[i]
            answer = self.cleaned_data[f'question_{i+1}']
            response = SurveyResponse(user=user, question=question, answer=answer)
            response.save()
