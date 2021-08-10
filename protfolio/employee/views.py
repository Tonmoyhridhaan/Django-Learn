from django.http import HttpResponse

def profile(request):
    profile = "This is our employee profile page"
    return HttpResponse(profile)

