from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def teams(request):
    return render(request,'teams.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')
