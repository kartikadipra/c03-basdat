from django.shortcuts import render
from django.db import connection
from tools.tools import make_query
from django.http.response import HttpResponseRedirect, JsonResponse

# Create your views here.
def reads_bekerja(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            respon = make_query(
                """
                SELECT *
                FROM bekerja;
                """
            )
        else:
            username_user = request.session['username']
            print(username_user)
            respon = make_query(
                f"""
                SELECT *
                FROM bekerja
                WHERE username_pengguna = '{username_user}';
                """
            )
        response = {
            'hasil' : respon,
            'role': request.session['role']
        }
        print(respon)
        return render(request, 'daftar_bekerja.html', response)
    else:
        return HttpResponseRedirect('/login')

def create_bekerja(request):
    if request.session.has_key('username'):
        if request.session['role'] != 'admin':
            username_user = request.session['username']
            respon = make_query(
                f"""
                SELECT *
                FROM bekerja natural join pekerjaan 
                WHERE username_pengguna = '{username_user}'
                """
            )
            return render(request, 'create_bekerja.html', {'hasil' : respon})
        return HttpResponseRedirect('/bekerja/daftar/')
    else:
        return HttpResponseRedirect('/login')

def mulai_bekerja(request):
    if request.session.has_key('username'):
        if request.session['role'] != 'admin':
            username_user = request.session['username']
            respon = make_query(
                f"""
                select *
                from bekerja
                where username_pengguna = '{username_user}';
                """
            )
            response = {
                'hasil' : respon,
                'role': request.session['role']
            }
            print(respon)    
            return render(request, 'mulai_bekerja.html', response)
        else:
            return HttpResponseRedirect('/bekerja/daftar/')
    else:
        return HttpResponseRedirect('/login')