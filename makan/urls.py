from django.urls import path
from .views import *

urlpatterns = [

    path('daftar/', read_makan),

    path('create/', create_page),

    path('create_makanan/', create_makan),

]
