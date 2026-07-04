from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
def home(request):
    return HttpResponse("Hello!")

def profile(request):
    student = Student.objects.get(id=1)
    context = {
        'student': student       # pass the whole object
    }
    return render(request, 'profile.html', context)

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'form': form,
                'error': 'User already exists!'
            })
        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

