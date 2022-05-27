from django.urls import path
from misi.views import *

app_name = 'misi'
urlpattern = [
    path('', read_misi_utama),
    path('create/', create_misi_utama),
]