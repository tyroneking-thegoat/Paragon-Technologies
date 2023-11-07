from django.shortcuts import render
from django.http import HttpResponse
from csce4901 import settings

# Create your views here.
def home(request):
    
    return render(request, "course/home.html")

def courses(request):
    
    return render(request, "course/courses.html")