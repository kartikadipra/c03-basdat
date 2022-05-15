from django.urls import path
from .views import *

urlpattern = [
    path('list/', read_misi_utama),
    path('delete/<misi_utama_lama>', delete_misi_utama),
    path('create/', create_page),
    path('create_new_misi_utama/',create_misi_utama),
]