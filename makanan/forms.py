from django import forms
from django.db import connection

class createForm(forms.Form):



    nama = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nama Makanan',
        'type' : 'text',
        'required': True,
    }))

    harga = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Harga Makanan',
        'type' : 'text',
        'required': True,
    }))

    tingkat_energi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tingkat Energi Makanan',
        'type' : 'text',
        'required': True,
    }))

    tingkat_kelaparan = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tingkat Kelaparan Makanan',
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