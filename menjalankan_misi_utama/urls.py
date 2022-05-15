from django.urls import path
from .views import *

urlpattern = [
    path('list/', read_melakukan_misi_utama),
    path('update/<melalukan_misi_lama>', page_update_melakukan_misi_utama),
    path('update_makanan_baru/<melakukan_misi_lama>', update_melakukan_misi_utama),
    path('create/', create_page),
    path('create_new_misi_utama/',create_melakukan_misi_utama),
]




    