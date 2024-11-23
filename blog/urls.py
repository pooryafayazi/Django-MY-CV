from django.contrib import admin
from django.urls import path

from blog.views import blog

urlpatterns = [
    path('', blog)
]
