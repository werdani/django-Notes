from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from . models import Note
from . forms import Noteform
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import Profile

 
# Create your views here.

def all_notes(request):
    #return HttpResponse('hello ammar')
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    all_notes = Note.objects.filter(user=user)
    context ={
        'all_notes':all_notes,
        'profile':profile

    }

    return render(request,'notes.html',context)



def detail(request,slug):
    #return HttpResponse('<h1> hello werdani </h1>')
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    note = Note.objects.get(slug=slug)
    context ={
        'note':note,
        'profile':profile

    }
    return render (request,'note_deatil.html',context)


def not_add(request):
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    if request.method == 'POST':
         form = Noteform(request.POST)
         if form.is_valid:
            new_form = form.save(commit=False)
            new_form.user = request.user
            form.save()
            messages.success(request, 'Profile details added.')
            return redirect('/')
    else:
        form = Noteform()
    context = {

        'form':form,
        'profile':profile,
    }

    return render(request,'add.html',context)

def edit(request,slug):
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    note = get_object_or_404(Note,slug=slug)
    if request.method == 'POST':
         form = Noteform(request.POST,instance=note)
         if form.is_valid:
            new_form = form.save(commit=False)
            new_form.user = request.user
            form.save()
            messages.success(request, 'Profile edited.')
            return redirect('/')
    else:
        form = Noteform(instance=note)
    context = {

        'form':form,
        'profile':profile,
    }

    return render(request,'edit.html',context)
