from django import forms

class login_form(forms.Form):
    username = forms.CharField(label = '', max_length=20, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'username', 'placeholder': "Username"}))

    password = forms.CharField(label = '', max_length=225, widget = forms.TextInput(attrs={'class': 'form-control Font-Size-20',
        'id': 'password', 'placeholder': "Password"}))
