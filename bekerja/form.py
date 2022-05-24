from django import forms

class bekerjaForm(forms.Form):
    nama_tokoh = forms.TextField(label='Nama Tokoh', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
    'id': 'nama-tokoh', 'placeholder': "Nama Tokoh"}))

    nama_pekerjaan = forms.TextField(label='Nama Pekerjaan', widget=forms.TextInput(attrs={'class': 'form-control col-md-6',
        'id': 'nama-pekerjaan', 'placeholder': "Nama Pekerjaan"}))

    base_salary = forms.IntegerField(label='Base Honor', widget=forms.NumberInput(attrs={'class': 'form-control col-md-6',
        'id': 'base-salary', 'placeholder': "Base Salary"}))
