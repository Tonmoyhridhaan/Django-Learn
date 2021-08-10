from django.http import HttpResponse

def profile(request):
    profile = "This is our employee profile page"
    return HttpResponse(profile)
def employee(request):
    profile = "This is our employee Home page"
    return HttpResponse(profile)

