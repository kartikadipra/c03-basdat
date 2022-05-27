from django.shortcuts import render
from django.db import connection
from tools.tools import make_query
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Register your models here.
def create_page(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            return render(request, 'create_makanan.html')
        
        return HttpResponseRedirect('/makanan/daftar/')

    else:
        return HttpResponseRedirect('/login')
    
@csrf_exempt
def create_makanan(request):
    if request.session.has_key('username'):

        if request.session['role'] == 'admin':

            if request.method == 'POST':

                new_makanan = request.POST.get('new_makanan')
                harga = request.POST.get('harga')
                tingkat_energi = request.POST.get('tingkat_energi')
                tingkat_kelaparan = request.POST.get('tingkat_kelaparan')

                print(new_makanan)
                print(harga)
                print(tingkat_energi)
                print(tingkat_kelaparan)

        return HttpResponseRedirect('/makanan/daftar/')
        
    else:
        return HttpResponseRedirect('/login')


def read_makanan(request):



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


def delete_makanan(request, makanan_lama):

    print("makanan_lama : " + makanan_lama)
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            respon = make_query("SELECT * FROM MAKANAN;")

        return HttpResponseRedirect('makanan/daftar/')

    else:
        return HttpResponseRedirect('/login')

def page_update_makanan(request, makanan_lama):

    if request.session.has_key('username'):

        if request.session['role'] == 'admin':

            print("makanan_lama = " + makanan_lama)

            respon = make_query(f"SELECT * FROM MAKANAN WHERE MAKANAN = {makanan_lama};")
            print(respon)

            return render(request, 'update_makanan.html', {'result' : respon})

        else:
            return HttpResponseRedirect('/makanan/daftar/')

    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def update_makanan(request, harga_lama, energi_lama, kelaparan_lama ):

    print("harga_lama : " + harga_lama)
    print("energi_lama : " + energi_lama)
    print("kelaparan_lama : " + kelaparan_lama)

    if request.session.has_key('username'):

        if request.session['role'] == 'admin':
            
            if request.session['role'] == 'POST':
                harga_baru = request.POST.get('harga_baru')
                energi_baru = request.POST.get('energi_baru')
                kelaparan_baru = request.POST.get('kelaparan_baru')
                print(harga_baru)
                print(energi_baru)
                print(kelaparan_baru)
                respon = make_query("SELECT * FROM MAKANAN;")

        return HttpResponseRedirect('/makanan/daftar/')

    else:
        return HttpResponseRedirect('/login')
