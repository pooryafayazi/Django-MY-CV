from django.contrib import admin
from django.urls import path

from website.views import index

urlpatterns = [
    path('', index)
]
