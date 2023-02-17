from django.shortcuts import render


# Create your views here.
announcements =[
	{
		'author': 'Robel Abraham',
		'title': 'First announcement',
		'content': 'this is a test for announcements',
		'date_posted': 'Feburary 17, 2023'
	},
	{
		'author': 'William Turner',
		'title': 'Second announcement',
		'content': 'Second test for announcements',
		'date_posted': 'Feburary 17, 2023'
	}
	
]

def front_page(request):
	context = {
		'announcements': announcements,
	}
	return render(request, 'home/home.html', context)

def about(request):
	return render(request, 'home/about.html', {'title': 'About'})