from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    # return HttpResponse("You did it!")
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def stories(request):
    return render (request, 'stories.html')