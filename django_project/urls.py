"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from chartjs import views
from chartjs.views import SurveyCreateView
from theme import views as theme_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', theme_views.ChartData.as_view()),
    path('chart/', theme_views.HomeView.as_view(), name='graph'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('survey/', views.survey, name='survey'),
    path('surveySubmit/(<int:mood>)-(<int:grasp>)', views.surveySubmit, name='surveySubmit'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('classroom/', theme_views.baseView, name='classroom'),
    path('', theme_views.home, name='front_page'),
    path('profile_view/', theme_views.profile_view, name='profile_view'),
    path('user_registration/', theme_views.register, name='user_registration'),
    path('user_login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('user_logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('classes/', theme_views.classes, name='classes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
