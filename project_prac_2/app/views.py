from django.shortcuts import render
from .forms import MyForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = MyForm()
    return render(request,'home.html',{'form':form})