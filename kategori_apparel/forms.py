from django import forms
from django.db import connection

class createForm(forms.Form):

    nama_kategori = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nama Kategori',
        'type' : 'text',
        'required': True,
    }))

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]