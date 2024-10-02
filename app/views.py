from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is home Page")

def about(request):
    return HttpResponse("This is About Page")
def contact(request):
    return HttpResponse("This is Contact Page")