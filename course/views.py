import os
from django.shortcuts import render
from django.http import HttpResponse
from csce4901 import settings
from . models import Course
from django.http import FileResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    
    return render(request, "course/home.html")

def courses(request):
    base_directory = r'C:\Users\mauro\Desktop\pdfs'
    folders = [folder for folder in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, folder))]
    folder_files = {}
    
    for folder in folders:
        folder_path = os.path.join(base_directory, folder)
        files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        folder_files[folder] = files

    # Zip folders and folder_files.values() together
    folders_with_files = zip(folders, folder_files.values())

    return render(request, 'course/courses.html', {'folders_with_files': folders_with_files})

def csce1030(request):
    
    return render(request, "course/CSCE1030.html")

def csce2100(request):
    
    return render(request, "course/CSCE2100.html")

def csce3600(request):
    
    return render(request, "course/CSCE3600.html")

def view_pdf(request, folder, filename):
    base_directory = r'C:\Users\mauro\Desktop\pdfs'
    file_path = os.path.join(base_directory, folder, filename)

    if os.path.exists(file_path) and filename.endswith('.pdf'):
        # Open the file and read its contents
        try:
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="{filename}"'
                return response
        except Exception as e:
            # Handle exceptions if any
            print(f"Error while reading the file: {e}")
            raise Http404("PDF file cannot be opened")
    else:
        raise Http404("PDF file not found")