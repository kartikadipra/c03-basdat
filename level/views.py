from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import createForm

def rud_level(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM LEVEL")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'level/index.html', {'result': result})

def c_level(request):
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            xp = form.cleaned_data['xp']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO LEVEL VALUES ('{level}', {xp})")
        return HttpResponseRedirect(reverse('level:level'))
    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'level/create.html',response)

def d_level(request, level, xp):
    with connection.cursor() as c:
        c.execute("SET SEARCH_PATH TO THECIMS")
        c.execute("DELETE FROM LEVEL WHERE Level = %s AND XP = %s", [level, xp])
    return HttpResponseRedirect(reverse('level:level'))

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
