from django.shortcuts import render,get_object_or_404
from notes_app.models import Note
from accounts.models import Profile
# Create your views here.



def allnotes(request):
    notes = Note.objects.all()
    user = request.user
    profile = get_object_or_404(Profile,user=user)
    context={
        'all_notes':notes,
        'profile' : profile

    }

    return render(request,'home.html',context)