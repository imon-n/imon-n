from django.shortcuts import render
# from . forms import contactForm
from . forms import ExampleForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def form(request):
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request,'form.html',{'name' : name , 'email' : email})
    else:
        return render(request,'form.html')


def dj_form(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request,'d_form.html', {'form' : form})