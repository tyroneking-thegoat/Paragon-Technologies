from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from csce4901 import settings
from . tokens import make_token
import re, os
from auth.signals import create_user_info

# Create your views here.
def index(request):
    
    return render(request, "auth/index.html")

def signin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        
        user = authenticate(username = username, password = password1)
        
        if user is not None:
            login(request, user)
            return redirect('Course:home')
            
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect('signin') 
    
    return render(request, "auth/signin.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists.")
            return redirect('signup')
            
        if User.objects.filter(email = email):
            messages.error(request, "Email already registered.")
            return redirect('signup')
        
        email_domain = re.search(r"@[\w.]+", email)
        #print(email_domain)
        if email_domain.group() != "@my.unt.edu":
            messages.error(request, "Email is not a UNT email.")
            return redirect('signup')
        
        if password1 != password2:
            messages.error(request, "Passwords aren't matching.")
            return redirect('signup')
        
        user = User.objects.create_user(username, email, password1)

        user.is_active = False
        
        user.save()
        
        messages.success(request, "Account created. Confirmation email has been sent to your email in order to activate your account.")

        # Create the folder for user settings if it doesn't exist
        userSettings_folder = 'userSettings'
        if not os.path.exists(userSettings_folder):
            os.makedirs(userSettings_folder)

        # Create text file for the new user {can later move this to only create once account is verified}
        # Is also currently not linked to the django database (deleting a user in django won't delete the file locally)
        userSettings_file = open(f'{userSettings_folder}/{username}.txt', "w+")
        
        # Account Confirmation Email
        url = get_current_site(request)
        subject = "CSCE4901 - Paragon Technologies"
        body = render_to_string('email.html', {
            'user': user.username,
            'domain': url.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': make_token.make_token(user),
        })

        verified_sender_email = 'NoteTakerToolPlusBot2@outlook.com'
        email = EmailMessage(
            subject,
            body,
            verified_sender_email,
            [user.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')
    
    return render(request, "auth/signup.html")

def signout(request):
    
    logout(request)
    messages.success(request, "Logged Out.")
    
    return redirect('index')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None and make_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('signin')
    
    else:
        return render(request, 'email_fail.html')
    
def courses(request):
    
    return redirect('Course:courses')

def csce1030(request):
    
    return redirect('Course:csce1030')

def csce2100(request):
    
    return redirect('Course:csce2100')

def csce3600(request):
    
    return redirect('Course:csce3600')