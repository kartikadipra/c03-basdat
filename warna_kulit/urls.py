from django.urls import path
from .views import *

app_name = 'warna_kulit'
urlpatterns = [
	path('', rud_warna_kulit, name='warna_kulit'),
	path('create/', c_warna_kulit, name='c_warna_kulit'),
	path('delete/<kode>/',d_warna_kulit, name='d_warna_kulit'),

]
