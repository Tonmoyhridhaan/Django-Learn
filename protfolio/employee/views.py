from django.http import HttpResponse

def employee(request):
    employee = "This is our employee page check"
    return HttpResponse(employee)
def profile(request):
    profile = "This is my profile page"
    return HttpResponse(profile)
from django.http import HttpResponse

def employee(request):
    employee = "This is our employee page"
    return HttpResponse(employee)
