from django import forms
from crispy_forms.helper import FormHelper
from django.db import connection


def ubahketuple(par):
    hasil = []
    for i in range(len(par)):
        hasil.append(tuple([par[i][0], par[i][1]]))
    return tuple(hasil)

class formpemain(forms.Form):
    #Username: [isian]
    #Password: [isian]
    #Email: [isian]
    #No HP: [isian]

    def __init__(self, *args, **kuser):
        super().__init__(*args, **kuser)
        self.helper = FormHelper(self)
        self.helper.form_show_errors = False

    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    hp = forms.CharField(label='No. HP')



class formadmin(forms.Form):

    def __init__(self, *args, **kuser):
        super().__init__(*args, **kuser)
        self.helper = FormHelper(self)
        self.helper.form_show_errors = False

    username = forms.CharField()
    password = forms.CharField()