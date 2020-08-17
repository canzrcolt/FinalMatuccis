from django.contrib import admin
from django.urls import path

from .views import contactView, successView, indexView

urlpatterns = [
	path('', indexView, name='index'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]