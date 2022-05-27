from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import redirect

from pekerjaan.forms import pekerjaanForm


#CRUD PEKERJAAN

				# cursor.execute("INSERT INTO PEKERJAAN VALUES(%s, %s)", [nama_pekerjaan, base_salary])
#Create
# def create_pekerjaan(request):
# 	if (request.method == "POST"):
# 		form = pekerjaanForm(request.POST)
# 		if (form.is_valid()):
# 			with connection.cursor() as c:
# 				nama_pekerjaan = request.POST['nama_pekerjaan']
# 				base_salary = request.POST['base_salary']
#                 c.execute(f"INSERT INTO PEKERJAAN VALUES ('{nama_pekerjaan}', {base_salary})")

# 			return redirect("/pekerjaan/")

# 	form = pekerjaanForm()
# 	response = {}
# 	response["pekerjaan_form"] = form
# 	return render(request, 'pekerjaan/create.html', response)

def create_pekerjaan(request):
    # if request.session['role'] != 'admin':
    #     return HttpResponseRedirect(reverse('/'))
    if request.method == 'POST':
        form = pekerjaanForm(request.POST)
        if form.is_valid():
            nama_pekerjaan = form.cleaned_data['nama_pekerjaan']
            base_honor = form.cleaned_data['base_honor']
            with connection.cursor() as c:
                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO PEKERJAAN VALUES ('{nama_pekerjaan}', {base_honor})")
        return HttpResponseRedirect(reverse('pekerjaan:read'))
    create_form = pekerjaanForm()
    response = {'create_form':create_form}
    return render(request,'pekerjaan/create.html',response)


#Read
def read(request):
    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("""SELECT *, case when nama in 
            (select p.nama from pekerjaan p, tokoh t, bekerja b, apparel a
            where p.nama = b.nama_pekerjaan and p.nama = t.pekerjaan and p.nama = a.nama_pekerjaan)
        then false
        else true
        end as deleteable
        from pekerjaan
        order by nama asc;""")

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
def update(request, pekerjaan):
    return render(request,'pekerjaan/update.html')
    # cursor = connection.cursor()
    # if request.session.has_key('username'):
    #     if request.session.role == 'Admin':
    #         print("pekerjaan = " + pekerjaan)
    #         res = cursor.execute(f"select * from pekerjaan where nama = '{pekerjaan}';")
            
    #         print(res[0])
    #         return render(request, 'update_job.html', {'result' : res[0]})
        
    #     else:
    #         return HttpResponseRedirect('/pekerjaan/')

    # else:
    #     return HttpResponseRedirect('/login')

#Delete
def delete(request, nama_pekerjaan) :
    print("delete  = " + nama_pekerjaan)

    if request.session.has_key ('username') :
        with connection.cursor() as cursor:
            if request.session['role'] == 'Admin' :
                cursor.execute (f"DELETE FROM PEKERJAAN WHERE nama = '{nama_pekerjaan}';")

            return redirect("/pekerjaan/")

    else:
        return HttpResponseRedirect('/login')