from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

def rud_warna_kulit(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM WARNA_KULIT")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'warna_kulit/index.html', {'result': result})

def c_warna_kulit(request):
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            kode = form.cleaned_data['kode']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO WARNA_KULIT VALUES ('{kode}'")
        return HttpResponseRedirect(reverse('warna_kulit:warna_kulit'))

    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'warna_kulit/create.html', response)

def d_warna_kulit(request, kode):
    with connection.cursor() as c:
        c.execute("SET SEARCH_PATH TO THECIMS")
        c.execute("DELETE FROM WARNA_KULIT WHERE kode = %s", [kode])
    return HttpResponseRedirect(reverse('warna_kulit:warna_kulit'))

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
