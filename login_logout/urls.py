from django.urls import path
from .views import create_tokoh, daftar_tokoh, detail_tokoh, homePage, index, login_page, home_page, loginPage, logout, register_admin, register_player, create_character, \
    character_list, character_detail, registerAdmin, registerPemain, update_character, update_tokoh

urlpatterns = [

    #home
    path('', index, name='home'),

    #homepage
    path('home/', homePage),

    #login
    path('login/', loginPage),
    #logout
    path('logout/', logout),

    #register 
    path('registerPemain/', registerPemain),
    path('registerAdmin/', registerAdmin),

    #tokoh
    path('tokoh', daftar_tokoh),
    path('tokoh/create', create_tokoh),
    path('tokoh/detail', detail_tokoh),
    path('tokoh/update', update_tokoh)
]
