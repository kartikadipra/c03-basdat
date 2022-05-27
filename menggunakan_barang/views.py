from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse

from menggunakan_barang.forms import barangForm
from django.shortcuts import redirect

#CR MENGGUNAKAN BARANG

# #Create
# def create(request):
# 	if (request.method == "POST"):
# 		form = barangForm(request.POST)
# 		if(form.is_valid()):
# 			with connection.cursor() as cursor:
# 				Nama_tokoh = request.POST['Nama_tokoh']
# 				Id_barang = request.POST['Id_barang']
				
# 				cursor.execute("INSERT INTO MENGGUNAKAN_BARANG VALUES(%s, %s)", [Nama_tokoh, Id_barang])

# 			return redirect("/menggunakan_barang/")

# 	form = barangForm()
# 	response = {}
# 	response["barang_form"] = form
# 	return render(request, 'menggunakan_barang/create.html', response)

def create(request):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    if request.method == 'POST':
        form = barangForm(request.POST)
        if form.is_valid():
            username_pengguna= form.cleaned_data['username_pengguna']
            nama_tokoh = form.cleaned_data['nama_tokoh']
            waktu= form.cleaned_data['waktu']
            id_barang = form.cleaned_data['id_barang']
            

            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO MENGGUNAKAN_BARANG VALUES ('{username_pengguna}','{nama_tokoh}', '{waktu}','{id_barang}')")
        return HttpResponseRedirect(reverse('menggunakan_barang:read'))
    create_form = barangForm()
    response = {'create_form':create_form}
    return render(request,'menggunakan_barang/create.html',response)

#Create
# def create(request):
#     if request.session.has_key('username'):
#         if request.session['role'] != 'Admin':
#             with connection.cursor() as cursor:
#                 user = request.session['username']
#                 tokoh = (f" select nama from tokoh where username_pengguna = '{user}';")
#                 item = (f"""
#                     select distinct b.id_koleksi 
#                     from koleksi_tokoh k, barang b 
#                     where k.id_koleksi = b.id_koleksi and k.username_pengguna = '{user}';""")

#             return render(request, 'menggunakan_barang/create.html', {'tokoh' : tokoh, 'item' : item})
#         return HttpResponseRedirect('/menggunakan_barang/read/')

#     else:
#         return HttpResponseRedirect('/login')


# Read
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def read(request):
    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM MENGGUNAKAN_BARANG")

        result = namedtuplefetchall(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'menggunakan_barang/read.html', {'result': result})


# def read(request):
#     cursor = connection.cursor()

#     try:
#         if request.session.role == 'admin':
#             with connection.cursor() as cursor:
#                 cursor.execute("SET SEARCH_PATH TO THECIMS")
#                 cursor.execute("""select mb.username_pengguna, mb.nama_tokoh, mb.waktu, kjb.nama
#                     from menggunakan_barang mb, barang b, koleksi_jual_beli kjb
#                     where mb.ID_barang = b.ID_koleksi and b.ID_koleksi = kjb.ID_koleksi
#                     order by mb.username_pengguna asc;
#                     """)

#                 result = namedtuplefetchall(cursor)
        
#         else :
#             pemain = request.session['username']
#             print(pemain)
#             with connection.cursor() as cursor:
#                 cursor.execute("SET SEARCH_PATH TO THECIMS")
#                 cursor.execute( f"""select mb.nama_tokoh, mb.waktu, kjb.nama
#                     from menggunakan_barang mb, barang b, koleksi_jual_beli kjb
#                     where mb.ID_barang = b.ID_koleksi and b.ID_koleksi = kjb.ID_koleksi and mb.username_pengguna = '{pemain}'
#                     order by mb.nama_tokoh asc;
#                     """) 
#                 result = namedtuplefetchall(cursor)

#     except Exception as e:
#         print(e)

#     finally:
#         cursor.close()

#     return render(request, 'menggunakan_barang/read.html', {'result': result})