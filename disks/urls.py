from django.urls import path
from .views import *

urlpatterns = [
    path('albums/', albums, name="Albums"),
    path('album/<int:id>', album, name="Album"),
]