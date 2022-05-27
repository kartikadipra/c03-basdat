from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

def rud_koleksi(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM KOLEKSI")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'koleksi/index.html', {'result': result})

def c_koleksi(request):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            harga = form.cleaned_data['harga']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO KOLEKSI VALUES ('{id}', {harga})")
        return HttpResponseRedirect(reverse('koleksi:koleksi'))
    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'koleksi/create.html',response)

def d_koleksi(request, id, harga):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    with connection.cursor() as c:
        c.execute("SET SEARCH_PATH TO THECIMS")
        c.execute("DELETE FROM KOLEKSI WHERE id = %s AND harga = %s", [id, harga])
    return HttpResponseRedirect(reverse('koleksi:koleksi'))

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
