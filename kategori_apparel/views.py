from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse

# def kategori_apparel(request):
#     with connection.cursor() as c:
#         c.execute("SELECT * FROM PRODUK_APOTEK")
#         res = dictfetchall(c)
#     response = {'data_produk_apotek':res}
#     return render(request,'rud_produk_apotek.html',response)

# def index(request):
#     return render(request, 'kategori_apparel/index.html')

def index(request):
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

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
