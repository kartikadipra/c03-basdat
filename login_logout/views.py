from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from tools.tools import make_query

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

HOMEURL = "/home"
LOGINURL = "/login"

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def login_page(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = "user"

        result = make_query(f"select * from pemain where username='{username}' and password='{password}'")
        # bisa di modif == null or ""
        if len(result) == 0:
            result = make_query(f"select * from admin where username='{username}' and password='{password}'")
            role = "admin"
            if len(result) == 0:
                return HttpResponseNotFound("User not found")

        request.session['user'] = user_result(result[0])
        request.session['role'] = role
        request.session['username'] = result[0].username

def home_page(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')

    model = {
        'role': request.session['role'],
        'username': request.session['username']
    }

    if request.session['role'] == 'user':
        model['email'] = request.session['user']['email']
        model['phone'] = request.session['user']['no_hp']
        model['koin'] = request.session['user']['koin']

    return render(request, 'homepage.html', model)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")

def user_result(result):
    # pemain
    if len(result) == 5:
        result_map = {
            'username': result[0],
            'email': result[1],
            'password': result[2],
            'no_hp': result[3],
            'koin': result[4],
        }
        return result_map

    # admin
    result_map = {
        'username':result[0],
        'password': result[1],
    }
    return result_map

@csrf_exempt
def register_player(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        print(request.POST)

    return render(request, "register-player.html")

@csrf_exempt
def register_admin(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/home')

    if request.method == "POST":
        print(request.POST)

    return render(request, "register-admin.html")

def tokoh_list(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')
    if request.session["role"] == "user":
        username = request.session["username"]
        tokoh = make_query(f"select * from tokoh where username_pengguna = '{username}'")
    else:
        tokoh = make_query("select * from tokoh")

    return render(request, "tokoh-list.html", {"tokoh":tokoh})

def tokoh_detail(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')

    username = request.GET.get("username")
    nama_tokoh = request.GET.get("nama_tokoh")

    tokoh = make_query(f"select * from tokoh where username_pengguna='{username}' and nama='{nama_tokoh}'")

    return render(request, "tokoh-detail.html", {"tokoh":tokoh[0]})


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

    tokoh = make_query(f"select * from tokoh where username_pengguna='{username}' and nama='{nama_tokoh}'")
    return render(request, 'update-tokoh.html', {'tokoh':tokoh[0]})

