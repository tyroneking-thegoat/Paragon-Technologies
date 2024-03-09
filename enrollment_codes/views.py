from django.shortcuts import render
from django.http import JsonResponse
from .models import EnrollmentCode

def check_enrollment(request):
    # Extract the enrollment code from the request's query parameters
    enrollment_code = request.GET.get('code', None)

    # Query the database to check if the enrollment code exists
    if enrollment_code:
        enrollment_exists = EnrollmentCode.objects.filter(EnrollCode=enrollment_code).exists()
        if enrollment_exists:
            return JsonResponse({'message': f'Enrollment code {enrollment_code} exists'}, status=200)
        else:
            return JsonResponse({'message': f'Enrollment code {enrollment_code} does not exist'}, status=404)
    else:
        return JsonResponse({'message': 'Enrollment code not provided'}, status=400)

def enroll(request):
    return render(request, 'enroll/enroll.html')
