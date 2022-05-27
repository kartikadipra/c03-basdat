from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

def rud_menggunakan_apparel(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM MENGGUNAKAN_APPAREL")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'menggunakan_apparel/index.html', {'result': result})

def c_menggunakan_apparel(request):
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            username_pengguna = form.cleaned_data['username_pengguna']
            nama_tokoh = form.cleaned_data['nama_tokoh']
            id_koleksi = form.cleaned_data['id_koleksi']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute("INSERT INTO MENGGUNAKAN_APPAREL VALUES (%s, %s, %s)",
                            [username_pengguna, nama_tokoh, id_koleksi]
                )
        return HttpResponseRedirect(reverse('menggunakan_apparel:menggunakan_apparel'))
    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'menggunakan_apparel/create.html',response)

def d_menggunakan_apparel(request, username_pengguna, nama_tokoh, id_koleksi):
    with connection.cursor() as c:
        c.execute("SET SEARCH_PATH TO THECIMS")
        c.execute("DELETE FROM MENGGUNAKAN_APPAREL WHERE username_pengguna = %s AND nama_tokoh = %s AND id_koleksi = %s", [username_pengguna, nama_tokoh, id_koleksi])
    return HttpResponseRedirect(reverse('menggunakan_apparel:menggunakan_apparel'))


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
