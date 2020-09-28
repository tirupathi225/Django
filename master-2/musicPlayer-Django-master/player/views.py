from django.http import HttpResponse
from django.shortcuts import render
from player.models import Music


def home(request):
    musics = Music.objects.all() # Nous sélectionnons tous nos musics
    return render(request, 'player/home.html', {'all_musics': musics})

def listen_music(request, id_music):
    return render(request, 'player/lecteur.html', locals())