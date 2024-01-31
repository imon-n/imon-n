from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def details(request):
    return render(request,'details.html')
    
def contact(request):
    return render(request,'contact.html')
    