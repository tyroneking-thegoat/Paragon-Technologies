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
import re

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
            #return render(request, "course/home.html")
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
        
        # Account Confirmation Email
        url = get_current_site(request)
        subject = "CSCE4901 - Paragon Technologies"
        body = render_to_string('email.html', {
            'user': user.username,
            'domain': url.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': make_token.make_token(user),
        })
  
        email = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('signin')
    
    return render(request, "auth/signup.html")

#def home(request):
    
    return render(request, "auth/home.html")

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