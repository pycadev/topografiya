# core/urls.py
from django.urls import path
from .views import home, problem_page

urlpatterns = [
    path('', home, name='home'),
    path('index<int:num>/', problem_page, name='index'),
]
