from django.shortcuts import render,HttpResponse
from .models import Album,Song

def index(request):
    all_album=Album.objects.all()
    context={'all_album': all_album}
    return render(request,'music/index.html',context)

def detail(request,album_id):
    return HttpResponse("<h1>The id is: " + str(album_id) + " <h2>" )