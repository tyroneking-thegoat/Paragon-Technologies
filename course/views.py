from django.shortcuts import render
from django.http import HttpResponse
from csce4901 import settings
from . models import Course

# Create your views here.
def home(request):
    
    return render(request, "course/home.html")

def courses(request):
    
    courseList = Course.objects.all
    
    return render(request, "course/courses.html", {'list': courseList})

def csce1030(request):
    
    return render(request, "course/CSCE1030.html")

def csce2100(request):
    
    return render(request, "course/CSCE2100.html")

def csce3600(request):
    
    return render(request, "course/CSCE3600.html")