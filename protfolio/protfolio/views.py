from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def about(request):
    about = "This is our about page"
    return HttpResponse(about)

def contact(request):
    contact = "This is our contact page"
    return HttpResponse(contact)