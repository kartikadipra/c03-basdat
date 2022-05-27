from django.urls import path
from login import views
from .views import *

app_name = 'registrasiPengguna'
urlpatterns = [
    #path('', user_reg_page, name='user_reg'),


    path('Registrasi', pilihakun),
    path('RegistrasiAdmin', registadmin),
    path('RegistrasiPemain', registerPemain),
]