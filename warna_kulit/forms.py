from django import forms
from django.db import connection

search_path = "SET search_path to THECIMS"


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_kode_warna_kulit():
    with connection.cursor() as c:
        c.execute(search_path)
        c.execute("SELECT kode FROM WARNA_KULIT")
        res = dictfetchall(c)
    temp_res = [res[i]['kode'] for i in range(len(res))]
    return [tuple([i, i]) for i in temp_res]

class createForm(forms.Form):
    kode = forms.CharField(label="kode", widget=forms.Select(choices=get_kode_warna_kulit()))