from django.urls import path
from .views import *

urlpatterns = [
    path('daftar/', read_level)
    path('create-level/', create_level_baru),
    path('update-level/', update_level),
    path('update-xp/', update_xp),
    path('delete-level/', delete_level),
]