from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from csce4901 import settings

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
            return render(request, "auth/home.html")
            
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
        
        if password1 != password2:
            messages.error(request, "Passwords aren't matching.")
            return redirect('signup')
        
        user = User.objects.create_user(username, email, password1)
        
        user.save()
        
        messages.success(request, "Account registered.")
        
        # Email
        subject = "CSCE4901 OCR"
        body = "Confirmation link to activate your account."
        sender = settings.EMAIL_HOST_USER
        recipient = [user.email]
        send_mail(subject, body, sender, recipient, fail_silently = True)
        
        return redirect('signin')
    
    return render(request, "auth/signup.html")

def home(request):
    
    return render(request, "auth/home.html")

def signout(request):
    
    logout(request)
    messages.success(request, "Logged Out.")
    
    return redirect('index')
