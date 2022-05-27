from django import forms
from django.db import connection

class createForm(forms.Form):

    username_pengguna = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username Pengguna',
        'type' : 'text',
        'required': True,
    }))

    nama_tokoh = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nama Tokoh',
        'type': 'text',
        'required': True,
    }))

    id_koleksi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ID Koleksi',
        'type': 'text',
        'required': True,
    }))

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
