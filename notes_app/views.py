from django.shortcuts import render
from django.http import HttpResponse
from . models import Note

# Create your views here.

def all_notes(request):
    #return HttpResponse('hello ammar')
    all_notes = Note.objects.all()

    return render(request,'all_notes.html',{'all_notes':all_notes})



def detail(request,slug):
    #return HttpResponse('<h1> hello werdani </h1>')
    note = Note.objects.get(slug=slug)
    return render (request,'note_deatil.html',{'note':note})