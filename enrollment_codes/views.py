from django.shortcuts import render
from django.http import JsonResponse
from .models import EnrollmentCode
import json
from django.http import JsonResponse
from .models import Course
from django.core.exceptions import ObjectDoesNotExist
import random
import string

def enroll(request):
    # Add your view logic here
    return render(request, 'enroll/enroll.html')

import logging

logger = logging.getLogger(__name__)



def create_class(request):
    logger.info('Received a request to create a class.')
    
    if request.method == 'POST':
        logger.debug('Request method is POST.')
        
        data = json.loads(request.body)
        class_name = data.get('name', '').upper()
        class_number = data.get('number')
        enrollment_code = data.get('enrollment_code', '')

        # Check for missing data (class_name or class_number)
        if not class_name:
            logger.error('Class name is required.')
            response_data = {'message': f'Class name is required.'}
            return JsonResponse(response_data)
        
        if not class_number:
            logger.error('Class number is required.')
            response_data = {'message': f'Class number is required.'}
            return JsonResponse(response_data)
        
        logger.debug('Class name and number are provided.')
        
        # Check if class_name is 4 characters long and consists only of letters
        if len(class_name) != 4 or not class_name.isalpha():
            logger.error('Class name must be 4 letters.')
            response_data = {'message': f'Class name must be 4 letters.'}
            return JsonResponse(response_data)

        logger.debug('Class name meets criteria.')
        
        # Check enrollment code conditions
        if enrollment_code:
            if len(enrollment_code) != 5 or not enrollment_code.isalnum():
                logger.error('Enroll code must be 5 alphanumeric characters.')
                response_data = {'message': f'Enroll code must be 5 alphanumeric characters.'}
                return JsonResponse(response_data)
            else:
                logger.debug('Enrollment code is provided.')
        else:
            logger.debug('Enrollment code is not provided. Generating random code.')
            # Generate enrollment code if not provided
            enrollment_code = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

        try:
            existing_course = Course.objects.get(name=class_name, number=class_number)
            existing_enrollment_code = EnrollmentCode.objects.filter(EnrollCode=enrollment_code).exists()
            if existing_enrollment_code:
                logger.error('This enrollment code already exists.')
                response_data = {'message': f'This enrollment code already exists.'}
                return JsonResponse(response_data)
            else:
                logger.debug('Creating new enrollment code object.')
                # Create enrollment code object
                EnrollmentCode.objects.create(EnrollCode=enrollment_code, course=existing_course)
                response_data = {'message': f'Enrollment code "{enrollment_code}" created successfully for existing course "{existing_course.name} {existing_course.number}".'}
                return JsonResponse(response_data)
        except Course.DoesNotExist:
            logger.debug('Creating new course and enrollment code object.')
            try:
                # Create new course
                course = Course.objects.create(name=class_name, number=class_number)
                # Create enrollment code object
                EnrollmentCode.objects.create(EnrollCode=enrollment_code, course=course)
                response_data = {'message': f'Class "{course.name} {course.number}" created successfully with enrollment code: {enrollment_code}.'}
                return JsonResponse(response_data)
            except Exception as e:
                logger.error(f'Error creating class: {str(e)}')
                return JsonResponse({'error': str(e)}, status=500)
    else:
        logger.error('Invalid request method.')
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

    # Default response if none of the conditions are met
    logger.error('Invalid request parameters.')
    return JsonResponse({'error': 'Invalid request parameters.'}, status=400)
    # Default response if none of the conditions are met
    logger.error('Invalid request parameters.')
    return JsonResponse({'error': 'Invalid request parameters.'}, status=400)


def check_enrollment(request):
    enroll_code = request.GET.get('enroll_code', None)
    user = request.user


    if enroll_code:
        try:
            enrollment = EnrollmentCode.objects.get(EnrollCode=enroll_code)
            course_name = enrollment.course.name
            course_number = enrollment.course.number
            response_data = {'message': f'{enroll_code} is linked to {course_name}{course_number}, you are now successfuly enrolled {user.username}.'}
            return JsonResponse(response_data, status=200)
        except EnrollmentCode.DoesNotExist:
            response_data = {'message': f'This enrollment code does not exist.'}
            return JsonResponse(response_data, status=200)
    else:
        response_data = {'message': f'Enrollment code not provided.'}
        return JsonResponse(response_data, status=200)