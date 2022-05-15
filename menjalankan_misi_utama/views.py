from django.shortcuts import render

from urllib import response
from django.contrib import admin
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.db import connection
from tools.tools import make_query
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Register your models here.
def create_page(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            return render(request, 'create_melakukan_misi_utama.html')
        
        return HttpResponseRedirect('/melakukan_misi_utama/daftar/')

    else:
        return HttpResponseRedirect('/login')
    
@csrf_exempt
def create_melakukan_misi_utama(request):
    if request.session.has_key('username'):

        if request.session['role'] == 'admin':

            if request.method == 'POST':

                new_nama_tokoh = request.POST.get('new_nama_tokoh')
                new_nama_misi = request.POST.get('new_nama_misi')

                print(new_nama_tokoh)
                print(new_nama_misi)

        return HttpResponseRedirect('/melakukan_misi_utama/daftar/')
        
    else:
        return HttpResponseRedirect('/login')


def read_melakukan_misi_utama(request):

        if request.session.has_key('username'):
            res = make_query("SELECT * FROM MELAKUKAN_MISI_UTAMA")
            response = {
                'result' : res,
                'role' : request.session['role']
            }

            print(res)

            return render(request, 'daftar_melakukan_misi_utama.html',response)
            
        else:
            return HttpResponseRedirect('/login')


def page_update_melakukan_misi_utama(request, melakukan_misi_lama):

    if request.session.has_key('username'):

        if request.session['role'] == 'admin':

            print("melakukan_misi_lama = " + melakukan_misi_lama)

            respon = make_query(f"SELECT * FROM MELAKUKAN_MISI_UTAMA WHERE MELAKUKAN_MISI_UTAMA = {melakukan_misi_lama};")
            print(respon)

            return render(request, 'update_melakukan_misi_utama.html', {'result' : respon})

        else:
            return HttpResponseRedirect('/melakukan_misi_utama/daftar/')

    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def update_melakukan_misi_utama(request, status_lama):

    print("status_lama : " + status_lama)

    if request.session.has_key('username'):

        if request.session['role'] == 'admin':
            
            if request.session['role'] == 'POST':
                status_baru = request.POST.get('status_baru')
                print(status_baruu)
                respon = make_query("SELECT * FROM MELAKUKAN_MISI_UTAMA;")

        return HttpResponseRedirect('/melakukan_misi_utama/daftar/')

    else:
        return HttpResponseRedirect('/login')