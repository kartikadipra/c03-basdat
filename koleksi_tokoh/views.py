from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

def rud_koleksi_tokoh(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM KOLEKSI_TOKOH")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'koleksi_tokoh/index.html', {'result': result})

def c_koleksi_tokoh(request):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            id_koleksi = form.cleaned_data['id_koleksi']
            username_pengguna = form.cleaned_data['username_pengguna']
            nama_tokoh = form.cleaned_data['nama_tokoh']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO KOLEKSI_TOKOH VALUES ('{id_koleksi}', '{username_pengguna}', '{nama_tokoh}')")
        return HttpResponseRedirect(reverse('koleksi_tokoh:koleksi_tokoh'))

    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'koleksi_tokoh/create.html', response)

def d_koleksi_tokoh(request, id_koleksi, username_pengguna, nama_tokoh):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    with connection.cursor() as c:
        c.execute("SET SEARCH_PATH TO THECIMS")
        c.execute("DELETE FROM KOLEKSI_TOKOH WHERE id_koleksi = %s AND username_pengguna = %s AND nama_tokoh = %s", [id_koleksi, username_pengguna, nama_tokoh])
    return HttpResponseRedirect(reverse('koleksi_tokoh:koleksi_tokoh'))

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
