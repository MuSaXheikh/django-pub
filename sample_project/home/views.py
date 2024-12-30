from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return HttpResponse("this is my responce")