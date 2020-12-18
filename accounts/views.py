from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from .forms import SignUpForm , UserForm , ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile
from django.contrib import messages

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
            messages.success(request, 'your accounte is created.')
            return redirect('/')
    return render(request,'signup.html',{'form':form})


def profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)

    return render(request,'profile.html',{'profile':profile})

def edit_profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    if request.method == "POST":
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile) #FILES >>becoust i used image
        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save()
            new_profile = profile_form.save()
            #new_profile.user=request.user
            #new_profile.save()
            messages.success(request, 'Profile edited.')
            return redirect('/')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        context = {
            'user_form':user_form,
            'profile_form':profile_form,

        }
    return render(request,'editprofile.html',context)

def change_password(request, slug):

    profile = get_object_or_404(Profile,slug=slug)

    if request.method =='POST':
       password_form = PasswordChangeForm(request.user,request.POST)
       if password_form.is_valid():
           password_form.save()
           messages.success(request, 'password change succesfuly.')
           return redirect('/')


    else:
        password_form = PasswordChangeForm(request.user)

    return render(request,'changepass.html',{'password_form':password_form})
