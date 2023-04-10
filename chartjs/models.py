from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=200)
	rank = models.IntegerField()

class SurveyQuestion(models.Model):
    question = models.TextField(default="")
    answer = models.IntegerField(default=5)

    def __str__(self):
        return self.question
