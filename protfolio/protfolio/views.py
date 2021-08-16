from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = {
        'name' : 'Tonmoy Barua',
        'age' : 22,
        'phone' : '01777303837',
        'skills' : ['CP','PS','DEV']
    }
    return render(request,'index.html',text)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')