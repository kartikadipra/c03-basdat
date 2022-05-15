from django.shortcuts import render
from django.db import connection
from tools.tools import make_query
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def read_pekerjaan(request):
    if request.session.has_key('username'):
        respon = make_query("select * from pekerjaan;")
        response = {
            'result' : respon,
            'role' : request.session['role']
        }

        print(respon)
        return render(request, 'daftar_pekerjaan.html', response)

    else:
        return HttpResponseRedirect('/login')

def create_page(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            return render(request, 'create_pekerjaan.html')

        return HttpResponseRedirect('/pekerjaan/daftar/')

    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def create_pekerjaan_baru(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            if request.method == 'POST':
                pekerjaan_baru = request.POST.get('pekerjaan_baru')
                base_honor_baru = request.POST.get('base_honor_baru')

                print(pekerjaan_baru)
                print(base_honor_baru)
        return HttpResponseRedirect('pekerjaan/daftar/')

    else:
        return HttpResponseRedirect('/login')

def delete_pekerjaan(request, old_pekerjaan):
    print("pekerjaan_lama : " + pekerjaan_lama)
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            respon = make_query("select * from pekerjaan;")

        return HttpResponseRedirect('pekerjaan/daftar/')

    else:
        return HttpResponseRedirect('/login')

def update_pekerjaan(request, old_pekerjaan):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            print("pekerjaan_lama = " + pekerjaan_lama)
            respon = make_query(f"select * from pekerjaan where pekerjaan = {pekerjaan_lama};")
            print(respon)

            return render(request, 'update_pekerjaan.html', {'result' : respon})

        else:
            return HttpResponseRedirect('/pekerjaan/daftar/')
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def update_base_honor(request, old_honor):
    print("honor_lama : " + honor_lama)
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            if request.session['role'] == 'POST':
                honor_baru = request.POST.get('honor_baru')
                print(honr_baru)
                respon = make_query("select * from pekerjaan;")

        return HttpResponseRedirect('/pekerjaan/daftar/')

    else:
        return HttpResponseRedirect('/login')







            