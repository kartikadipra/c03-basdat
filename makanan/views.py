from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def read_makanan(request):

    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM MAKANAN")

        result = namedtuplefetchall(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'daftar_makanan.html', {'result': result})

def create_makanan(request):

    if request.method == 'POST':

        form = createForm(request.POST)

        if form.is_valid():

            nama = form.cleaned_data['nama']
            harga = form.cleaned_data['harga']
            tingkat_energi = form.cleaned_data['tingkat_energi']
            tingkat_kelaparan = form.cleaned_data['tingkat_kelaparan']

            with connection.cursor() as c:

                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO MAKANAN VALUES ('{nama}', {harga},{tingkat_energi},{tingkat_kelaparan})")

        return HttpResponseRedirect(reverse('makanan:makanan'))

    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'create_makanan.html',response)



