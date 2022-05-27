from django.shortcuts import render
from django.db import connection
from collections import namedtuple
from django.http import HttpResponseRedirect
from django.urls import reverse
#from .forms import createForm

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def read_misi_utama(request):

    cursor = connection.cursor()

    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT * FROM MISI, MISI_UTAMA WHERE  MISI.nama = MISI_UTAMA.nama")

        result = namedtuplefetchall(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render(request, 'daftar_misi_utama.html', {'result': result})


def create_misi_utama(request):

    if request.method == 'POST':

        form = createForm(request.POST)

        if form.is_valid():

            nama = form.cleaned_data['nama']
            efek_energi = form.cleaned_data['efek_energi']
            efek_hubungan_sosial = form.cleaned_data['efek_hubungan_sosial']
            efek_kelaparan = form.cleaned_data['efek_kelaparan']

            syarat_energi = form.cleaned_data['syarat_energi']
            syarat_hubungan_sosial = form.cleaned_data['syarat_hubungan_sosial']
            syarat_kelaparan = form.cleaned_data['syarat_kelaparan']

            completion_time = form.cleaned_data['completion_time']
            reward_koin = form.cleaned_data['reward_koin']
            reward_xp = form.cleaned_data['reward_xp ']

            deskripsi = form.cleaned_data['deskripsi']


            with connection.cursor() as c:

                c.execute("SET SEARCH_PATH TO THECIMS")
                c.execute(f"INSERT INTO MISI VALUES ('{nama}', {efek_energi},{efek_hubungan_sosial},{efek_kelaparan},{syarat_energi},{syarat_hubungan_sosial},{syarat_kelaparan},{completion_time},{reward_koin},{reward_xp},{deskripsi})")
                c.execute(f"INSERT INTO MISI_UTAMA VALUES ('{nama}')")
        return HttpResponseRedirect(reverse('makanan:makanan'))

    create_form = createForm()
    response = {'create_form':create_form}
    return render(request,'create_misi_utama.html',response)