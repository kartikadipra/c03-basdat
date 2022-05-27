from django.urls import path
from .views import *


app_name = 'makan'
urlpatterns = [

    path('', read_makan),

    path('create/', create_makan),


]
