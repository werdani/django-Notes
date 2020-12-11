from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Note
from . forms import Noteform
from django.contrib.auth.models import User
 
# Create your views here.

def all_notes(request):
    #return HttpResponse('hello ammar')
    all_notes = Note.objects.all()

    return render(request,'all_notes.html',{'all_notes':all_notes})



def detail(request,slug):
    #return HttpResponse('<h1> hello werdani </h1>')
    note = Note.objects.get(slug=slug)
    return render (request,'note_deatil.html',{'note':note})


def not_add(request):
    if request.method == 'POST':
         form = Noteform(request.POST)
         if form.is_valid:
            new_form = form.save(commit=False)
            new_form.user = request.user
            form.save()
            return redirect('/')
    else:
        form = Noteform()
    context = {

        'form':form,
    }

    return render(request,'add.html',context)