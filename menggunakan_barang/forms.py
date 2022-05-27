from django import forms

class barangForm(forms.Form):
    username_pengguna = forms.CharField(label='username_pengguna', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
    'id': 'username_pengguna', 'placeholder': "username_pengguna"}))

    nama_tokoh = forms.CharField(label='Nama Tokoh', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
        'id': 'nama-tokoh', 'placeholder': "Nama Tokoh"}))

    waktu = forms.DateTimeField(label='waktu ', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
    'id': 'waktu ', 'placeholder': "waktu "}))

    id_barang = forms.CharField(label='id_barang', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
    'id': 'barang', 'placeholder': "Barang"}))