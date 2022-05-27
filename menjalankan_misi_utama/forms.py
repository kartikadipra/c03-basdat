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


def get_nama_misi():
    with connection.cursor() as c:
        c.execute(search_path)
        c.execute("SELECT nama FROM MISI")
        res = dictfetchall(c)
    temp_res = [res[i]['nama'] for i in range(len(res))]
    return [tuple([i, i]) for i in temp_res]


def get_username_pemain():
    with connection.cursor() as c:
        c.execute(search_path)
        c.execute("SELECT username FROM PEMAIN")
        res = dictfetchall(c)
    temp_res = [res[i]['username'] for i in range(len(res))]
    return [tuple([i, i]) for i in temp_res]


def get_nama_tokoh():
    with connection.cursor() as c:
        c.execute(search_path)
        c.execute("SELECT nama FROM TOKOH")
        res = dictfetchall(c)
    temp_res = [res[i]['nama'] for i in range(len(res))]
    return [tuple([i, i]) for i in temp_res]


class createForm(forms.Form):
    nama_misi = forms.CharField(label="Nama Misi", widget=forms.Select(choices=get_nama_misi()))

    username_pengguna = forms.CharField(label="Username Pengguna", widget=forms.Select(choices=get_username_pemain()))

    nama_tokoh = forms.CharField(label="Nama Tokoh", widget=forms.Select(choices=get_nama_tokoh()))