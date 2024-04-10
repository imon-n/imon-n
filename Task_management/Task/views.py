from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    else:
        task_form = TaskForm()
    return render(request,'add_task.html',{'form':task_form})


def edit_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    return render(request,'add_task.html',{'form':task_form})


def delete_task(request,id):
    task_form = TaskModel.objects.get(pk=id)
    task_form.delete()
    return redirect('homepage')


def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    if request.method == 'POST':
        task.is_completed = True 
        task.save()
        return redirect('homepage')
    return render(request, 'complete_task.html', {'form': task})