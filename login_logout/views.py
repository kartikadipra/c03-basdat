from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from tools.tools import make_query

# Create your views here.
from django.views.decorators.csrf import csrf_exempt



def home(request):
    return render(request, 'home.html')
    
def homePage(request):

    #login
    if 'user' not in request.session:
        return HttpResponseRedirect('/login_page')

    isi = {
        'role': request.session['role'],
        'username': request.session['username']
    }

    #register
    if request.session['role'] == 'user':  # aslinya user
        isi['email'] = request.session['user']['email']
        isi['phone'] = request.session['user']['no_hp']
        isi['koin'] = request.session['user']['koin']

    return render(request, 'homepage.html', isi)



@csrf_exempt
def loginPage(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = "user"

        result = make_query(f"SELECT * FROM pemain WHERE username='{username}' and password='{password}'")
        
        # bisa di modif == null or ""
        if len(result) == 0:
            result = make_query(f"select * from admin where username='{username}' and password='{password}'")
            role = "admin"
            if len(result) == 0:
                return HttpResponseNotFound("User not found")

        request.session['user'] = hasil(result[0])
        request.session['role'] = role
        request.session['username'] = result[0].username


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")

def hasil(result):
    # pemain
    if len(result) == 5:
        map = {
            'username': result[0],
            'email': result[1],
            'password': result[2],
            'no_hp': result[3],
            'koin': result[4],
        }
        return map

    # admin
    map = {
        'username':result[0],
        'password': result[1],
    }
    return map

@csrf_exempt
def registerPemain(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        print(request.POST)

    return render(request, "registerPemain.html")

@csrf_exempt
def registerAdmin(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        print(request.POST)

    return render(request, "register_admin.html")

def daftar_tokoh(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')
    if request.session["role"] == "user":
        username = request.session["username"]
        tokoh = make_query(f"select * from tokoh where username_pengguna = '{username}'")
    else:
        tokoh = make_query("select * from tokoh")

    return render(request, "tokoh_list.html", {"tokoh":tokoh})

def detail_tokoh(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')

    username = request.GET.get("username")
    nama_tokoh = request.GET.get("nama_tokoh")

    tokoh = make_query(f"SELECT * FROM TOKOH WHERE username_pengguna='{username}' and nama='{nama_tokoh}'")

    return render(request, "tokoh_detail.html", {"tokoh":tokoh[0]})


def create_tokoh(request):
    if 'user' not in request.session or request.session['role'] == 'admin':
        return HttpResponseRedirect(LOGINURL)

    if request.method == "POST":
        print(request.POST)

    warna_kulit = make_query("SELECT * FROM warna_kulit")
    pekerjaan = make_query("SELECT nama FROM pekerjaan")

    return render(request, "create_tokoh.html", {"Kulit" : warna_kulit, "Pekerjaan" : pekerjaan})


def update_tokoh(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')

    if request.method == "POST":
        print(request.POST)

    username = request.session['username']
    nama_tokoh = request.GET.get('nama_tokoh')

    tokoh = make_query(f"SELECT * FROM TOKOH WHERE username_pengguna='{username}' AND nama='{nama_tokoh}'")
    return render(request, 'update_tokoh.html', {'tokoh':tokoh[0]})



def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def index(request):
    cursor = connection.cursor()
    try:
        cursor.execute("SET SEARCH_PATH TO THECIMS")
        cursor.execute("SELECT username FROM ADMIN")
        result = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'homepage.html', {'result': result})