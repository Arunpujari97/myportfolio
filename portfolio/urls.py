from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask_user_type, name='ask_user_type'),
    path('recruiter/', views.recruiter_form, name='recruiter_form'),
    path('home/', views.home, name='home'),
]