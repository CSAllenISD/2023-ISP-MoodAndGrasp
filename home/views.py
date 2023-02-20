from django.shortcuts import render
from .models import Announcements

# Create your views here.

def front_page(request):
	context = {
		'announcements': Announcements.objects.all()
	}
	return render(request, 'home/home.html', context)

def about(request):
	return render(request, 'home/about.html', {'title': 'About'})