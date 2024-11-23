from django.contrib import admin
from django.urls import path

from website.views import *

urlpatterns = [
    path('', index,name='home'),
    path('education', education,name='education'),
    path('skills', skills,name='skills'),
    path('contact', contact,name='contact'),
]
