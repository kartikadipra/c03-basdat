from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import redirect

from pekerjaan.form import pekerjaanForm


#CRUD PEKERJAAN

#Create
def create_pekerjaan(request):
	if (request.method == "POST"):
		form = pekerjaanForm(request.POST)
		if(form.is_valid()):
			with connection.cursor() as cursor:
				nama_tokoh = request.POST['nama_tokoh']
				nama_pekerjaan = request.POST['nama_pekerjaan']
				base_salary = request.POST['base_salary']
				cursor.execute("INSERT INTO PEKERJAAN VALUES(%s, %s, %s)", [nama_tokoh, nama_pekerjaan, base_salary])

			return redirect("/pekerjaan/")

	form = pekerjaanForm()
	response = {}
	response["pekerjaan_form"] = form
	return render(request, 'pekerjaan/create.html', response)


#Read
def read(request):
    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM PEKERJAAN")

        result = namedtuplefetchall(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'pekerjaan/read.html', {'result': result})

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

#Update

#Delate


