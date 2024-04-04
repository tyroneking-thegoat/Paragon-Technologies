import os
from django.shortcuts import render
from django.http import HttpResponse
from csce4901 import settings
from . models import Course
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from upload.models import PDFDocument
from upload.models import PDFFile

# Create your views here.
def home(request):
    
    return render(request, "course/home.html")

# Create your views here.
def courses(request):
    # Get the current directory of the views.py file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Assuming 'pdfs' folder is in the same directory as views.py
    base_directory = os.path.join(current_directory, 'pdfs')

    if not os.path.exists(base_directory):
        os.mkdir('course/pdfs')
        raise FileNotFoundError(f"The directory '{base_directory}' does not exist.")

    folders_with_files = {}
    
    for folder in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder)
        if os.path.isdir(folder_path):
            files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
            folders_with_files[folder] = files

    return render(request, 'course/courses.html', {'folders_with_files': folders_with_files})

# def courses(request):
#     return render(request, "course/courses.html")

def csce1030(request):
    
    return render(request, "course/CSCE1030.html")

def csce2100(request):
    
    return render(request, "course/CSCE2100.html")

def csce3600(request):
    
    return render(request, "course/CSCE3600.html")

def courses(request):
    # Query all PDFFile instances
    uploads = PDFFile.objects.all()

    # Pass the instances to the template
    return render(request, 'course/courses.html', {'uploads': uploads})

def courses(request):
    uploads = PDFFile.objects.all().select_related('pdf_document')  # Assuming a ForeignKey relationship

    return render(request, 'course/courses.html', {'uploads': uploads})

def coursetitle(request):
    uploads = PDFDocument

def view_pdf(request, pdf_id):
    # Fetch the PDFFile instance from the database
    pdf_file = get_object_or_404(PDFFile, id=pdf_id)  # Using ID to fetch; adjust as needed

    # Serve the PDF file
    if pdf_file.file and pdf_file.file.url.endswith('.pdf'):
        try:
            with pdf_file.file.open('rb') as f:
                response = HttpResponse(f.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="{pdf_file.name}"'
                return response
        except Exception as e:
            print(f"Error while reading the file: {e}")
            raise Http404("PDF file cannot be opened")
    else:
        raise Http404("PDF file not found")
