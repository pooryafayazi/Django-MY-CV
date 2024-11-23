from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse


def index(request):
    return HttpResponse('index')