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

def read_makan(request):

    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM MAKAN")

        result = namedtuplefetchall(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'daftar_makan.html', {'result': result})

def create_makan(request):

    if request.method == 'POST':

        form = createForm(request.POST)

        if form.is_valid():


            username_pengguna = form.cleaned_data['username_pengguna']
            nama_makanan = form.cleaned_data['nama_makanan']
            nama_tokoh = form.cleaned_data['nama_tokoh']
            waktu = datetime.now()

            with connection.cursor() as c:

                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO MAKAN VALUES ('{username_pengguna}', {nama_tokoh},{waktu},{nama_makanan})")

        return HttpResponseRedirect(reverse('makan:makan'))

    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'create_makan.html',response)

