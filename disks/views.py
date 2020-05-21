from django.shortcuts import render
from .models import Album

# Create your views here.

def albums(request):
    albums = Album.objects.all()
    return render(request, "disks/albums.html", locals())

def album(request, id):
    album = Album.objects.get(id = id)
    return render(request, "disks/album.html", locals())