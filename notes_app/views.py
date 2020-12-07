from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_notes(request):
    return HttpResponse('hello ammar')


def detail(request):
    return HttpResponse('<h1> hello werdani </h1>')