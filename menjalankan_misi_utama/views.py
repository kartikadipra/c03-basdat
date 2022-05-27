from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

from datetime import datetime

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def read_menjalankan_misi(request):

    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM MENJALANKAN_MISI")

        result = namedtuplefetchall(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'daftar_menjalankan_misi.html', {'result': result})


def create_menjalankan_misi(request):

    if request.method == 'POST':

        form = createForm(request.POST)

        if form.is_valid():


            username_pengguna = form.cleaned_data['username_pengguna']
            nama_misi = form.cleaned_data['nama_misi']
            nama_tokoh = form.cleaned_data['nama_tokoh']
            status = "In Progress"

            with connection.cursor() as c:

                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO MENJALANKAN_MISI VALUES ('{username_pengguna}', {nama_tokoh},{nama_misi},{status})")

        return HttpResponseRedirect(reverse('menjalankan_misi_utama:menjalankan_misi_utama'))

    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'create_menjalankan.html',response)