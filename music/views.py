from django.shortcuts import render
from django.http import Http404
from .models import Album,Song

def index(request):
    all_album=Album.objects.all()
    return render(request,'music/index.html',{'all_album': all_album})

def detail(request,album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album doesn't exist")
    return render(request,'music/detail.html',{'album':album})