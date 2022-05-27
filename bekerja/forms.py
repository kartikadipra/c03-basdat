import datetime
from django import forms

class bekerjaForm(forms.Form):
    username_pengguna = forms.CharField(label='Username Pengguna' , widget=forms.TextInput(attrs={
        'class': 'form-control col-md-6',
        'id': 'username-pengguna', 
        'placeholder': "Username Pengguna"}))

    nama_tokoh = forms.CharField(label='Nama Tokoh', widget=forms.TextInput(attrs={
        'class': 'form-control col-md-6',
        'id': 'nama-tokoh', 
        'placeholder': "Nama Tokoh"}))
        
    timestamp = forms.DateField(initial=datetime.date.today)

    nama_pekerjaan = forms.CharField(label='Nama Pekerjaan', widget=forms.TextInput(attrs={
        'class': 'form-control col-md-6',
        'id': 'nama-pekerjaan',
        'placeholder': "Nama Pekerjaan"}))
        
    jumlah_keberangkatan = forms.CharField(label='Jumlah Keberangkatan', widget=forms.TextInput(attrs={
        'class': 'form-control col-md-6',
        'id': 'jumlah-keberangkatan',
        'placeholder': "Jumlah Keberangkatan"}))

    honor = forms.IntegerField(label='Honor', widget=forms.NumberInput(attrs={
        'class': 'form-control col-md-6',
        'id': 'honor', 
        'placeholder': "Base Honor"}))
