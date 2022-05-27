from django.urls import path
from .views import *

app_name = 'kategori_apparel'
urlpatterns = [
	path('', rud_kategori_apparel, name='kategori_apparel'),
	path('create/', c_kategori_apparel, name='c_kategori_apparel'),
	path('create/', c_kategori_apparel, name='c_kategori_apparel'),
	path('delete/<nama_kategori>/',d_kategori_apparel, name='d_kategori_apparel'),
	
]
