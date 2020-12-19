from django.shortcuts import render
from notes_app.models import Note
# Create your views here.



def allnotes(request):
    notes = Note.objects.all()

    return render(request,'home.html',{'all_notes':notes})