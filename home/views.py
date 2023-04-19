from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Announcements
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.

def front_page(request):
	context = {
		'announcements': Announcements.objects.all()
	}
	return render(request, 'home/home.html', context)

class PostListView(ListView):
	model = Announcements
	template_name = 'home/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'announcements'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Announcements

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Announcements
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True

class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Announcements
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request, 'home/about.html', {'title': 'About', 'about': True})