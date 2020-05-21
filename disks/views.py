from django.shortcuts import render
from .models import Album, Track
from .forms import SearchForm
from django.db.models import Q


# Create your views here.

def albums(request):
    form = SearchForm(request.POST or None)
    alb = Album.objects.all()
    if form.is_valid():
        alb = Album.objects.filter(Q(Title__contains=form.cleaned_data['Rechercher']) | Q(Artist__Name__contains=form.cleaned_data['Rechercher']))
    return render(request, "disks/albums.html", locals())


def concatenate(l1, l2):
    for elt in l2:
        if elt not in l1:
            l1.append(elt)
    return l1


def album(request, id):
    album = Album.objects.get(id=id)
    tracks = Track.objects.filter(Album=album)
    return render(request, "disks/album.html", locals())
