# Generated by Django 4.2 on 2023-04-10 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartjs', '0004_remove_surveyquestion_question_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='question',
            field=models.TextField(default=''),
        ),
    ]