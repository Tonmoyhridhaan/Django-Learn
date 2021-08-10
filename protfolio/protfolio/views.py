from django.http import HttpResponse

def home(request):
    home = "This is our home page"
    return HttpResponse(home)

def about(request):
    about = "This is our about page"
    return HttpResponse(about)

def contact(request):
    contact = "This is our cntact page"
    return HttpResponse(contact)