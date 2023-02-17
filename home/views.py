from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def front_page(request):
	return HttpResponse('<h1>ISP Home<h1>')

def about(request):
	return HttpResponse('<h1>ISP About<h1>')