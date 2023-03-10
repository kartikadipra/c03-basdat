from datetime import timezone, datetime
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse


from bekerja.forms import bekerjaForm

#CR BEKERJA

#Create
# def create(request, nama_tokoh, pekerjaan, base_honor):
#     print("nama_tokoh = " + nama_tokoh)
#     print("nama pekerjaan = " + pekerjaan)
#     print("base honor = " + base_honor)

#     cursor = connection.cursor()

#     try:
#         cursor.execute("SET SEARCH_PATH TO THECIMS")
#         cursor.execute("SELECT * FROM BEKERJA")

#         result = namedtuplefetchall(cursor)

#     except Exception as e:
#         print(e)

#     finally:
#         cursor.close()

#     return render(request, 'bekerja/create.html', {'result': result})

def create(request):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    if request.method == 'POST':
        form = bekerjaForm(request.POST)
        if form.is_valid():
            username_pengguna = form.cleaned_data['username_pengguna']
            nama_tokoh = form.cleaned_data['nama_tokoh']
            timestamp = form.cleaned_data['timestamp']
            nama_pekerjaan = form.cleaned_data['nama_pekerjaan']
            jumlah_keberangkatan = form.cleaned_data['jumlah_keberangkatan']
            honor = form.cleaned_data['honor']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO BEKERJA VALUES ('{username_pengguna}', '{nama_tokoh}', '{timestamp}', '{nama_pekerjaan}', '{jumlah_keberangkatan}', '{honor}')")
        return HttpResponseRedirect(reverse('bekerja:read'))
    create_form = bekerjaForm()
    response = {'create_form':create_form}
    return render(request,'bekerja/create.html',response)

#Read
def read(request):
    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM BEKERJA")

        result = namedtuplefetchall(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'bekerja/read.html', {'result': result})

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# def read(request):
#     cursor = connection.cursor()

#     if request.session.has_key('username'):
#         try:
#             if request.session['role'] == 'Admin':
#                 cursor.execute("SET SEARCH_PATH TO THECIMS")
#                 res = cursor.execute("""
#                     select username_pengguna, nama_tokoh, nama_pekerjaan, timestamp, jumlah_keberangkatan, honor
#                     from bekerja;""")

#                 # result = namedtuplefetchall(cursor)

#             else:
#                 pemain = request.session['pemain']
#                 print(pemain)

#                 cursor.execute("SET SEARCH_PATH TO THECIMS")

#                 res = cursor.execute(
#                 f"""
#                 select username_pengguna, nama_tokoh, nama_pekerjaan, timestamp, jumlah_keberangkatan, honor
#                 from bekerja
#                 where username_pengguna = '{pemain}';""")
                
#                 # result = namedtuplefetchall(cursor) 

#         except Exception as e:
#             print(e)

#         finally:
#             cursor.close()

#     response = {
#         'result' : res,
#         'role': request.session['role']
#     }

#     print(res)
#     return render(request, 'bekerja/read.html', {'result': response})