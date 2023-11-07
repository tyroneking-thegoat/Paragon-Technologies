from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

def home(request):
    
    return render(request, "course/home.html")