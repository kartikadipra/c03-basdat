from django.urls import path
from .views import *

urlpattern = [
    path('', read_misi_utama),
    path('delete/<misi_utama_lama>', delete_misi_utama),
    path('create/', create_misi_utama),
]