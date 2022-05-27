from django import forms

class pekerjaanForm(forms.Form):
    nama_pekerjaan = forms.CharField(label='Nama Pekerjaan', widget=forms.TextInput(attrs={
        'class': 'form-control col-md-6',
        'id': 'nama-pekerjaan',
        'placeholder': "Nama Pekerjaan"}))

    base_honor = forms.IntegerField(label='Base Honor', widget=forms.NumberInput(attrs={
        'class': 'form-control col-md-6',
        'id': 'base-honor',
        'placeholder': "Base Honor"}))

