# Generated by Django 4.1.7 on 2023-03-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_classroom_class_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student_classroom',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_class_code',
            field=models.CharField(blank=True, default='', max_length=36),
        ),
    ]
