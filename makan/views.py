from django.shortcuts import render
from django.db import connection
from tools.tools import make_query
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Register your models here.
def create_page(request):
    if request.session.has_key('username'):
        if request.session['role'] == 'admin':
            return render(request, 'create_makan.html')
        
        return HttpResponseRedirect('/makan/daftar/')

    else:
        return HttpResponseRedirect('/login')
    
@csrf_exempt
def create_makan(request):
    if request.session.has_key('username'):

        if request.session['role'] == 'admin':

            if request.method == 'POST':

                new_tokoh = request.POST.get('new_makanan')
                new_makanan = request.POST.get('new_makanan')

                print(new_tokoh)
                print(new_makanan)
                

        return HttpResponseRedirect('/makanan/daftar/')
        
    else:
        return HttpResponseRedirect('/login')


def read_makan(request):

        if request.session.has_key('username'):
            res = make_query("SELECT * FROM MAKAN")
            response = {
                'result' : res,
                'role' : request.session['role']
            }

            print(res)

            return render(request, 'daftar_makan.html',response)
            
        else:
            return HttpResponseRedirect('/login')