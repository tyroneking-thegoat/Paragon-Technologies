from django.shortcuts import render
# from .models import Thumbnail
from upload.models import PDFDocument, PDFFile

# Create your views here.
# from django.views.generic import TemplateView


def home(request):
    # obj=Thumbnail.objects.all()
    # return render(request, 'course/home.html', {'thumbnail':obj})

    # obj=PDFFile.objects.all()
    # return render(request, 'course/home.html', {'thumbnail':obj})


    uploads = PDFFile.objects.all().select_related('pdf_document')
    
    documents_with_files = {}
    for upload in uploads:
        document_name = upload.pdf_document
        if document_name not in documents_with_files:
            documents_with_files[document_name] = [upload]
        else:
            documents_with_files[document_name].append(upload)

    return render(request, 'course/home.html', {'uploads': uploads})
