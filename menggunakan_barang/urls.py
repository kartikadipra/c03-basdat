from django.urls import path
from .views import *

urlpatterns = [
    path('daftar/', read_barang),
    path('create/', create_barang),
    path('create_barang/', create_barang_baru),
    path('get_barang/', get_barang),
]
