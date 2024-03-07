from django.shortcuts import render

def enroll_view(request):
    return render(request, 'enroll/enroll.html')