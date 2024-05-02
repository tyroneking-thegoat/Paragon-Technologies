from django.shortcuts import render
from django.http import Http404
from .models import PDFDocument, PDFFile
from django.core.files.storage import FileSystemStorage
import os
from course.models import Course
from django.conf import settings
import uuid

def get_unique_filename(folder_path, filename):
    original_filename, file_extension = os.path.splitext(filename)
    unique_filename = f"{original_filename}_{uuid.uuid4().hex}{file_extension}"
    while os.path.exists(os.path.join(folder_path, unique_filename)):
        unique_filename = f"{original_filename}_{uuid.uuid4().hex}{file_extension}"
    return unique_filename

def is_pdf(file):
    return file.name.lower().endswith('.pdf')

def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        if not is_pdf(uploaded_file):
            return render(request, 'upload/pdf_error.html')
        
        folder_name = request.POST.get('folder_name')
        if folder_name == "other":
            folder_name = request.POST.get('other_course')

        folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        unique_filename = get_unique_filename(folder_path, uploaded_file.name)

        fs = FileSystemStorage(location=folder_path)
        filename = fs.save(unique_filename, uploaded_file)
        uploaded_file_url = fs.url(filename)
        
        # Try to get the PDFDocument instance for the folder
        try:
            pdf_document = PDFDocument.objects.get(title=folder_name)
        except PDFDocument.DoesNotExist:
            # If the PDFDocument instance doesn't exist, create a new one
            pdf_document = PDFDocument.objects.create(title=folder_name)
        except PDFDocument.MultipleObjectsReturned:
            # If multiple PDFDocument instances are found, choose one
            pdf_document = PDFDocument.objects.filter(title=folder_name).first()
        
        # Create and save a new PDFFile instance for the uploaded file
        pdf_file = PDFFile(pdf_document=pdf_document, title=uploaded_file.name, file=os.path.join(folder_name, filename))
        pdf_file.save()
        
        # Fetch course names from the database
        courses = Course.objects.all()
        course_names = [course.full_name() for course in courses]

        return render(request, 'upload/success.html', {'uploaded_file_url': uploaded_file_url, 'course_names': course_names})

    # Fetch course names from the database
    courses = Course.objects.all()
    course_names = [course.full_name() for course in courses]

    return render(request, 'upload/uploads.html', {'course_names': course_names})