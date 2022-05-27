
from registrasiPengguna.forms import *
from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import *

def pilihakun(request):
    return render(request, "pilihanakun.html")

def checkUserExist(table, username, password=None):
    data = {}
    if password is not None:
        with connection.cursor() as c:
            c.execute("SELECT * FROM THECIMS.%s WHERE username=%s AND password=%s" % (table, '%s', '%s'),[username,password])
            data = dictfetchall(c)
    else:
        with connection.cursor() as c:
            c.execute("SELECT * FROM THECIMS.%s WHERE username=%s" % (table, '%s'),[username])
            data = dictfetchall(c)
    print(len(data))
    return len(data) > 0

def registerAkun(username):
    with connection.cursor() as c:
        c.execute("INSERT INTO THECIMS.akun VALUES (%s)", [username])

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

def registadmin(request):
    context = {}
    form = formadmin(request.POST or None)
    cursor = connection.cursor()

    if (form.is_valid() and request.method == 'POST'):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        if checkUserExist("admin", username) == False:
            registerAkun(username)
            cursor.execute("INSERT INTO THECIMS.ADMIN VALUES (%s , %s)"
            ,[username, password])
            request.session['role'] = 1
            return redirect('/') # arahin ke page login
        else:
            messages.error(request, 'Username sudah terdaftar')
            return redirect("/login")
    context['form'] = form

    return render(request, 'registadmin.html', context)

def registerPemain(request):
    context = {}
    form = formpemain(request.POST or None)
    cursor = connection.cursor()

    #Username: [isian]
    #Password: [isian]
    #Email: [isian]
    #No HP: [isian]
    if (form.is_valid() and request.method == 'POST'):

        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        noHp = form.cleaned_data['hp']


        if checkUserExist("pemain", username) == False:

            registerAkun(username)

            cursor.execute("INSERT INTO THECIMS.PEMAIN VALUES (%s , %s , %s, %s, %s)"
                           , [username, email, password, noHp, 0])
            request.session['role'] = 0
            return redirect('/')
        else:
            messages.error(request, 'Username sudah terdaftar')
            return redirect("/login")
    context['form'] = form

    return render(request, 'registerpemain.html', context)