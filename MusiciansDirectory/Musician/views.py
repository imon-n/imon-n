from django.shortcuts import render , redirect
from . import forms
from .models import MusicianModel
# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        music_form = forms.MusicianForm(request.POST)
        if music_form.is_valid():
            music_form.save()
            return redirect('homepage')
    else:    
        music_form = forms.MusicianForm()
    return render(request,'add_musician.html',{'form':music_form})

def edit_musician(request,id):
    music = MusicianModel.objects.get(pk=id)
    music_form = forms.MusicianForm(instance=music)

    if request.method == 'POST':
        music_form = forms.MusicianForm(request.POST,instance=music)
        if music_form.is_valid():
            music_form.save()
            return redirect('homepage')
    return render(request,'add_musician.html',{'form':music_form})

