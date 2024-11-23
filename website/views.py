from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def cv(request):
    return render(request,'cycv.html')

def contact(request):
    return render(request,'contact.html')

