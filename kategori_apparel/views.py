from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

def rud_kategori_apparel(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM KATEGORI_APPAREL")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'kategori_apparel/index.html', {'result': result})

def c_kategori_apparel(request):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            nama_kategori = form.cleaned_data['nama_kategori']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute("INSERT INTO KATEGORI_APPAREL VALUES (%s)",
                            [nama_kategori]
                )
        return HttpResponseRedirect(reverse('kategori_apparel:kategori_apparel'))
    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'kategori_apparel/create.html',response)

def d_kategori_apparel(request, nama_kategori):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    with connection.cursor() as c:
        c.execute("SET SEARCH_PATH TO THECIMS")
        c.execute("DELETE FROM KATEGORI_APPAREL WHERE nama_kategori = %s", [nama_kategori])
    return HttpResponseRedirect(reverse('kategori_apparel:kategori_apparel'))


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]