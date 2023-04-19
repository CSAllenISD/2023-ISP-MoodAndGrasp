from django.db import models
from django.contrib.auth.models import User
from users.models import Classroom
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    gpa = models.FloatField(default=3.0)
    user_class_code = models.CharField(blank=True, default='', max_length=36)
    student_classroom = models.ManyToManyField(Classroom, blank=True)
    Mood = models.IntegerField(default=0)
    Grasp = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'

class SurveyQuestion(models.Model):
    QUESTION_CHOICES = (
        (-10, 'Far left'),
        (-5, 'Close left'),
        (0, 'Middle'),
        (5, 'Close right'),
        (10, 'Far right'),
    )
    question = models.CharField(max_length=200, blank=True)
    mood_question = models.BooleanField(default=False)
    grasp_question = models.BooleanField(default=False)
    emoji_1 = models.CharField(max_length=100, default='chartjs/angry.png')
    emoji_2 = models.CharField(max_length=100, default='chartjs/conflict.png')
    emoji_3 = models.CharField(max_length=100, default='chartjs/meh.png')
    emoji_4 = models.CharField(max_length=100, default='chartjs/good.png')
    emoji_5 = models.CharField(max_length=100, default='chartjs/happy.png')

    def __str__(self):
        return self.question
