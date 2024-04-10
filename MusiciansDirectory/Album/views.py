from django.shortcuts import render , redirect
from . import forms
from .models import AlbumModel

def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:    
        album_form = forms.AlbumForm()
    return render(request,'add_album.html',{'form':album_form})

def edit_albm(request,id):
    album = AlbumModel.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request, 'add_album.html', {'form' : album_form})


def delete_albm(request,id):
    album = AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect('homepage')