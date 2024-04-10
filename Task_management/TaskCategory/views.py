from django.shortcuts import render , redirect
from .forms import CategoryForm
from .models import CategoryModel

# Create your views here

def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('homepage')
    else:
        category_form = CategoryForm()
    return render(request,'add_category.html',{'form':category_form})


def delete_category(request,id):
    cat_form = CategoryModel.objects.get(pk=id)
    cat_form.delete()
    return redirect('homepage')
