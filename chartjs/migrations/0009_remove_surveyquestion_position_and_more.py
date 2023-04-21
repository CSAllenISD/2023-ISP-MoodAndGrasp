# Generated by Django 4.1 on 2023-04-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartjs', '0008_surveyquestion_emoji_1_surveyquestion_emoji_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyquestion',
            name='position',
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='emoji_1',
            field=models.CharField(default='chartjs/angry.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='emoji_2',
            field=models.CharField(default='chartjs/conflict.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='emoji_3',
            field=models.CharField(default='chartjs/meh.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='emoji_4',
            field=models.CharField(default='chartjs/good.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='emoji_5',
            field=models.CharField(default='chartjs/happy.png', max_length=100),
        ),
    ]