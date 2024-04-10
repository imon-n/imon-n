from django.shortcuts import render
from Musician.models import MusicianModel
from Album.models import AlbumModel

# def home(request):
#     musician = MusicianModel.objects.all()
#     # print(musician)
#     return render(request, 'home.html', {'data' : musician})

def home(request):
    album = AlbumModel.objects.all()
    return render(request, 'home.html', {'data' : album})
