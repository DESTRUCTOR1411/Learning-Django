 
from django.shortcuts import render, HttpResponse

from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def services(request):
   return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contacts(request):
    if request.method=="POST":
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Email = request.POST.get('Email')
        PhoneNumber = request.POST.get('PhoneNumber')
        City = request.POST.get('City')
        Gender = request.POST.get('Gender')
        Goals = request.POST.get('Goals')
        contact=Contact(First_Name=First_Name,Last_Name=Last_Name, Email=Email,
                        PhoneNumber=PhoneNumber, City=City, Gender=Gender, Goals=Goals)
        contact.save()
    return render(request,'contacts.html')