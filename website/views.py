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


def common_data(request):
       return {
        'name' : "Poorya",
        'surname' : "Fayazi",
        'email1' : "fayazipoorya@gmail.com",
        'email2' : "poorya189@gmail.com",
        'phone1' : "+989190104604",
        'phone2' : "+989937272005",
        'city' : "Tehran",
        'country' : "IRAN",
       }