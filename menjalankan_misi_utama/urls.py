from django.urls import path
from .views import *

urlpattern = [
    path('', read_menjalankan_misi),
    path('create/', create_menjalankan_misi),

]




    