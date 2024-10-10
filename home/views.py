from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'sentences': "sentence is a good"
    }
    return render(request, "index.html",context)  # Corrected the arguments for render

def about(request):
    return HttpResponse("About")

def services(request):
    return HttpResponse("Services")

def contact(request):
    return HttpResponse("Contact: 0318-3704036")