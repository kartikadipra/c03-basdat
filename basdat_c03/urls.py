"""basdat_c03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import homepage.urls
import kategori_apparel.urls
import koleksi.urls
import koleksi_tokoh.urls
import registrasiPengguna.urls
import login.urls

#Karlina
import pekerjaan.urls
import bekerja.urls
import menggunakan_barang.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('login/', include(login.urls)),
    path('registrasiPengguna/', include(registrasiPengguna.urls)),
    path('kategori_apparel/', include(kategori_apparel.urls)),
    path('koleksi/', include(koleksi.urls)),
    path('koleksi_tokoh/', include(koleksi_tokoh.urls)),

    #Karlina
    path('pekerjaan/', include(pekerjaan.urls)),
    path('bekerja/', include(bekerja.urls)),
    path('menggunakan_barang/', include(menggunakan_barang.urls)),
]
