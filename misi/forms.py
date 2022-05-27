from django import forms
from django.db import connection

class createForm(forms.Form):



    nama_misi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nama Misi',
        'type' : 'text',
        'required': True,
    }))

    efek_energi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Efek Energi',
        'type' : 'text',
        'required': True,
    }))

    efek_hubungan = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Efek Hubungan',
        'type' : 'text',
        'required': True,
    }))

    efek_kelaparan = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Efek Kelaparan',
        'type' : 'text',
        'required': True,
    }))

    syarat_energi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Syarat Energi',
        'type' : 'text',
        'required': True,
    }))

    syarat_hubungan_sosial = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Syarat Hubungan Sosial',
        'type' : 'text',
        'required': True,
    }))

    completion_time = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Completion Time',
        'type' : 'text',
        'required': True,
    }))

    reward_koin = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Reward Koin',
        'type' : 'text',
        'required': True,
    }))

    reward_xp = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Reward XP',
        'type' : 'text',
        'required': True,
    }))

    deskripsi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Deskripsi',
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