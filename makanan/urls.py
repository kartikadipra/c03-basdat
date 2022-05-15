from django.urls import path
from .views import *

urlpatterns = [

    path('daftar/', read_makanan),

    path('delete/<makanan_lama>', delete_makanan),

    path('update/<makanan_lama>', page_update_makanan),

    path('create/', create_page),

    path('create_makanan/', create_makanan),

    path('update_makanan_baru/<makanan_lama>', update_makanan),
]
