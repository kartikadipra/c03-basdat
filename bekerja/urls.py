from django.urls import path
from .views import *

urlpatterns = [
    path('daftar/', reads_bekerja),
    path('create/', create_bekerja),
    path('mulai_bekerja/', mulai_bekerja),
]
