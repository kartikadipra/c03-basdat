from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse

from menggunakan_barang.form import barangForm
from django.shortcuts import redirect

#CR MENGGUNAKAN BARANG

#Create
def create(request):
	if (request.method == "POST"):
		form = barangForm(request.POST)
		if(form.is_valid()):
			with connection.cursor() as cursor:
				Nama_tokoh = request.POST['Nama_tokoh']
				Id_barang = request.POST['Id_barang']
				
				cursor.execute("INSERT INTO MENGGUNAKAN_BARANG VALUES(%s, %s)", [Nama_tokoh, Id_barang])

			return redirect("/menggunakan_barang/")

	form = barangForm()
	response = {}
	response["barang_form"] = form
	return render(request, 'menggunakan_barang/create.html', response)


#Read
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

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

