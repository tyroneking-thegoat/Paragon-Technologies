import os
from django.shortcuts import render
from django.http import Http404

def upload(request):
        return render(request, "upload/uploads.html")

# def is_pdf(file):
#     return file.name.lower().endswith('.pdf')

# def upload(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']
#         folder_name = request.POST.get('folder_name', 'default_folder')

#         if not is_pdf(uploaded_file):
#             return render(request, 'upload/pdf_error.html')

#         base_directory = r'C:\Users\mauro\Desktop\pdfs'

#         os.makedirs(base_directory, exist_ok=True)

#         upload_directory = os.path.join(base_directory, folder_name)

#         os.makedirs(upload_directory, exist_ok=True)

#         file_path = os.path.join(upload_directory, uploaded_file.name)

#         with open(file_path, 'wb') as destination:
#             for chunk in uploaded_file.chunks():
#                 destination.write(chunk)

#         return render(request, 'upload/success.html')

#     base_directory = r'C:\Users\mauro\Desktop\pdfs'
#     folder_names = os.listdir(base_directory)

#     return render(request, 'upload/uploads.html', {'folder_names': folder_names})
    
