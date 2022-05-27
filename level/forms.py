from django import forms
from django.db import connection

search_path = "SET search_path to THECIMS"

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_lev_level():
    with connection.cursor() as c:
        c.execute(search_path)
        c.execute("SELECT Level FROM LEVEL")
        res = dictfetchall(c)
    temp_res = [res[i]['level'] for i in range(len(res))]
    return [tuple([i,i]) for i in temp_res]

class createForm(forms.Form):
    level = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Level',
        'type' : 'integer',
        'required': True,
    }))

    xp = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'XP',
        'type' : 'integer',
        'required': True,
    }))
