from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

# Create your views here.
def home(request): 
    pass

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user) when login creat
            return redirect('/')
    return render(request,'signup.html',{'form':form})

def login(request): 

    return render(request,'login.html',{})

def change_pass(request):
    return render (request,'change_pass.html',{})


def profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)

    return render(request,'profile.html',{'profile':profile})

