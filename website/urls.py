from django.contrib import admin
from django.urls import path

from website.views import *

urlpatterns = [
    path('', index,name='home'),
    path('about', about,name='about'),
    path('cv', cv,name='cv'),
    path('contact', contact,name='contact'),
]
