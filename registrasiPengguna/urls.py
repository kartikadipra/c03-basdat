from django.urls import path
from login import views
from .views import *

app_name = 'registrasiPengguna'
urlpatterns = [
    path('RegistrasiAdmin', registadmin),
    path('RegistrasiPemain', registerPemain),
]