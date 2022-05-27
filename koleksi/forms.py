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

def get_id_koleksi():
    with connection.cursor() as c:
        c.execute(search_path)
        c.execute("SELECT id FROM KOLEKSI")
        res = dictfetchall(c)
    temp_res = [res[i]['id'] for i in range(len(res))]
    return [tuple([i,i]) for i in temp_res]

class createForm(forms.Form):

    # id = forms.CharField(label="ID", widget=forms.Select(choices=get_id_koleksi()))
    id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ID',
        'type' : 'text',
        'required': True,
    }))

    harga = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Harga',
        'type' : 'integer',
        'required': True,
    }))