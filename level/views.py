from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
from tools.tools import make_query
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


# def index(request):
#     return render(request, 'index.html')

def create_page(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            return render(request, 'create_level.html')

        return HttpResponseRedirect('/level/daftar')
    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def create_level_baru(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            if request.method == 'POST':
                new_level = request.POST.get('new_level')
                new_xp = request.POST.get('new_xp')

                print(new_level)
                print(new_xp)

            return HttpResponseRedirect('/level/daftar')
        else:
            return HttpResponseRedirect('/login')

def read_level(request):
    if request.session.has_key('username'):
        res = make_query("select * from level;")
        response = {
            'result' : res,
            'role' : request.session['role']
        }

        print(res)

        return render(request, 'daftar_level.html', response)

    else:
        return HttpResponseRedirect('/login')

def update_level(request, level_lama):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            print("level_lama = " + level_lama)
            res = make_query(f"select * from level where level = {level_lama};")
            print(res)

            return render(request, 'update_level.html', {'result':res})

        else:
            return HttpResponseRedirect('/level/daftar')

    else:
        return HttpResponseRedirect('/login')

@csrf_exempt
def update_xp(request, xp_lama):
    print("xp_lama = " + xp_lama)
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            if request.method == 'POST':
                new_xp = request.POST.get('new_xp')
                print(new_xp)
                res = make_query("select * from level;")

        return HttpResponseRedirect('/level/daftar')

    else:
        return HttpResponseRedirect('/login')

def delete_level(request, level_lama):
    print("level_lama = " + level_lama)
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            res = make_query("select * from level;")

            return HttpResponseRedirect('/level/daftar')

        else:
            return HttpResponseRedirect('/login')



