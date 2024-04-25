from django.shortcuts import render
# from .models import Thumbnail
from upload.models import PDFDocument, PDFFile

# Create your views here.
# from django.views.generic import TemplateView


def home(request):

    docs = PDFFile.objects.all().select_related('pdf_document')

    return render(request, 'course/home.html', {'docs': docs})
