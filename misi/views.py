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
            return render(request, 'create_misi_utama.html')
        
        return HttpResponseRedirect('/misi_utama/daftar/')

    else:
        return HttpResponseRedirect('/login')
    
@csrf_exempt
def create_misi_utama(request):
    if request.session.has_key('username'):

        if request.session['role'] == 'admin':

            if request.method == 'POST':

                new_misi_utama = request.POST.get('new_misi_utama')
                new_efek_energi = request.POST.get('new_efek_energi')
                new_efek_hubungan = request.POST.get('new_efek_sosial')
                new_efek_kelaparan = request.POST.get('new_efek_kelaparan')

                new_syarat_energi = request.POST.get('new_syarat_energi')
                new_syarat_hubungan = request.POST.get('new_syarat_sosial')
                new_syarat_kelaparan = request.POST.get('new_syarat_kelaparan')

                completion_time = request.POST.get('completion_time')
                reward_koin = request.POST.get('reward_koin')
                reward_xp = request.POST.get('reward_xp')
                deskripsi = request.POST.get('deskripsi')

                print(new_misi_utama)
                print(new_efek_energi)
                print(new_efek_hubungan)
                print(new_efek_kelaparan)

                print(new_syarat_energi)
                print(new_syarat_hubungan)
                print(new_syarat_kelaparan)

                print(completion_time)
                print(reward_koin)
                print(reward_xp)
                print(deskripsi)

        return HttpResponseRedirect('/misi_utama/daftar/')
        
    else:
        return HttpResponseRedirect('/login')


def read_misi_utama(request):

        if request.session.has_key('username'):
            res = make_query("SELECT * FROM MISI_UTAMA")
            response = {
                'result' : res,
                'role' : request.session['role']
            }

            print(res)

            return render(request, 'daftar_misi_utama.html',response)
            
        else:
            return HttpResponseRedirect('/login')

def delete_misi_utama(request, misi_utama_lama):

    print("misi_utama_lama : " + misi_utama_lama)
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            respon = make_query("SELECT * FROM MISI_UTAMA;")

        return HttpResponseRedirect('misi_utama/daftar/')

    else:
        return HttpResponseRedirect('/login')
