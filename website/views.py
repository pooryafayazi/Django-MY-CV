from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def education(request):
    return render(request,'about.html')

def skills(request):
    return render(request,'cycv.html')

def contact(request):
    return render(request,'contact.html')

