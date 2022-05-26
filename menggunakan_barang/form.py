from django import forms

class barangForm(forms.Form):
    nama_tokoh = forms.CharField(label='Nama Tokoh', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
        'id': 'nama-tokoh', 'placeholder': "Nama Tokoh"}))

    Barang = forms.CharField(label='Barang', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
        'id': 'barang', 'placeholder': "Barang"}))

