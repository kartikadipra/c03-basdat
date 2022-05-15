from django.urls import path
from .views import *

urlpatterns = [
    path('daftar/', read_pekerjaan),

    path('delete/<pekerjaan_lama>', delete_pekerjaan),

    path('update/<pekerjaan_lama>', update_pekerjaan),

    path('create/', create_page),

    path('create_pekerjaan_baru/', create_pekerjaan_baru),

    path('update_base_honor_baru/<old_pekerjaan>', update_base_honor),
]