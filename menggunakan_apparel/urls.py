from django.urls import path
from .views import *

app_name = 'kategori_apparel'
urlpatterns = [
    path('', rud_menggunakan_apparel, name='menggunakan_apparel'),
    path('create/', c_menggunakan_apparel, name='c_menggunakan_apparel'),
    path('delete/<username_pengguna>/<nama_tokoh>/<id_koleksi>/', d_menggunakan_apparel, name='d_menggunakan_apparel'),

]
