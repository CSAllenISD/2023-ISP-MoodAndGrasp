from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Classroom
from chartjs.models import Student

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
	if created:
		Student.objects.create(user=instance)


#@receiver(post_save, sender=User)
#def create_teacher(sender, instance, created, **kwargs):
#	if created:
#		Teacher.objects.create(user=instance)
#		Classroom.objects.create(user=instance)
	
	

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

