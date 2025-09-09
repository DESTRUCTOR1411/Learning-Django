from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def services(request):
    return HttpResponse("This is our services page")

def about(request):
    return HttpResponse("This is our about page")

def contacts(request):
    return HttpResponse("This is our contacts page")