from django.db import connection
from collections import namedtuple
from django.shortcuts import render
from django.db import connection
from collections import namedtuple

# Create your views here.
def index(request):
    return render(request, 'index.html')

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def index(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT USERNAME FROM AKUN")
        cursor.execute("SELECT USERNAME, EMAIL FROM PEMAIN")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'index.html', {'result': result})