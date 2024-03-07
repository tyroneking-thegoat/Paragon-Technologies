from django.shortcuts import render
from .models import Thumbnail

# Create your views here.
from django.views.generic import TemplateView

def home(request):
    obj=Thumbnail.objects.all()
    return render(request, "course/home.html", {'thumbnail':obj})

