from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('announcements/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('announcements/new/', PostCreateView.as_view(), name='post_create'),
    path('announcements/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('about/', views.about, name='about'),
]