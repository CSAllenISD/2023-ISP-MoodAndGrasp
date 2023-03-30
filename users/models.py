from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid
import random

class Classroom(models.Model):
	classroom = models.OneToOneField(User, on_delete=models.CASCADE)

	def create_new_class_code(self):
		not_unique = True
		while not_unique:
			unique_ref = random.randint(1000000000, 9999999999)
			if not Classroom.objects.filter(class_code=unique_ref):
				not_unique = False
		return str(unique_ref)

	class_code = models.CharField(
			max_length = 36,
			blank=True,
			editable=True,
			unique=True,
			default=uuid.uuid4
		)

	def __str__(self):
		return f'{self.classroom.username}''s Classroom'

	def save(self, *args, **kwargs):
		super(Classroom, self).save(*args, **kwargs)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	user_class_code = models.CharField(blank=True, default='', max_length=36)
	student_classroom = models.ManyToManyField(Classroom, blank=True)
	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		img = Image.open(self.image.path).convert('RGB')

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
