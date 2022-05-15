from django.shortcuts import render
from django.db import connection
from tools.tools import make_query
from django.http.response import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def read_barang(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            respon = make_query(
                """
                select mb.username_pengguna, mb.nama_tokoh, mb.waktu, kjb.nama
                from menggunakan_barang mb, barang b, koleksi_jual_beli kjb
                where mb.ID_barang = b.ID_koleksi and b.ID_koleksi = kjb.ID_koleksi; 
                """
            )
        else:
            username_user = request.session['username']
            print(username_user)
            respon = make_query(
                f"""
                select mb.username_pengguna, mb.nama_tokoh, mb.waktu, kjb.nama
                from menggunakan_barang mb, barang b, koleksi_jual_beli kjb
                where mb.ID_barang = b.ID_koleksi and b.ID_koleksi = kjb.ID_koleksi and mb.username_pengguna = '{username_user}';
                """
            )
        response = {
            'result' : respon,
            'role': request.session['role']
        }
        print(respon)
        return render(request, 'daftar_barang.html', response)
    else:
        return HttpResponseRedirect('/login')

def create_barang(request):
    if request.session.has_key('username'):
        if request.session['role'] != 'admin':
            username_user = request.session['username']
            respon = make_query(
                f"""
                select nama_tokoh
                from menggunakan_barang
                where username_pengguna = '{username_user}'
                """
            )
            return render(request, 'create_barang.html', {'result' : respon})
        return HttpResponseRedirect('/use_item/list/')
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def create_barang_baru(request):
    if request.session.has_key('username'):
        if request.session['role'] != 'admin':
            if request.method == 'POST':
                username_user = request.session['username']
                pilihan_tokoh = request.POST.get('pilihan_tokoh')
                pilihan_id_item = request.POST.get('pilihan_id_item')
                print("username_user = " + username_user)
                print("pilihan_tokoh = " + pilihan_tokoh)
                print("pilihan_id_item = " + pilihan_id_item)
        return HttpResponseRedirect('/use_item/list/')
    else:
        return HttpResponseRedirect('/login')

def get_barang(request):
    if request.method == 'GET':
        pilihan_tokoh = request.GET['pilihan_tokoh']
        print(pilihan_tokoh)
        username_user = request.session['username']
        respon = make_query(
            f"""
            select id_koleksi 
            from koleksi_tokoh kt natural join barang ab
            where username_pengguna = '{username_user}' and nama_tokoh = '{pilihan_tokoh}';
            """
        )
        return JsonResponse({'result' : respon})