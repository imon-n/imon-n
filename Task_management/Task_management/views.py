from django.shortcuts import render
from Task.models import TaskModel
from TaskCategory.models import CategoryModel

def home(request):
    task_data = TaskModel.objects.all()
    return render(request, 'home.html', {'data' : task_data})

def home(request):
    data = CategoryModel.objects.all()
    return render(request, 'home.html', {'data' : data})