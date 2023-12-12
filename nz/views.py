from django.shortcuts import render
from django.http import HttpResponse

def bolt(request):
    return HttpResponse('<h1><bold>powerplay bowler</bold></h1>')

# Create your views here.
