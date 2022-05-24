from django.shortcuts import render
from .forms import *
from django.db import connection
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import redirect
from django.forms import formset_factory


# Create your views here.
	
def login_page(request):
	response={}
	response['error'] = False
	form = login_form(request.POST or None)
	response['form'] = form
	if(request.method == 'POST' and form.is_valid):
		username = request.POST['username']
		password = request.POST['password']
		print("masuk kkkk")
		try:
			with connection.cursor() as cursor:
				print("aaaa")
				cursor.execute("SET search_path to THECIMS")
				cursor.execute("SELECT * FROM AKUN WHERE username= %s", [username])
				isExist = cursor.fetchone()

			if isExist:
				print("B")
				with connection.cursor() as cursor:
					cursor.execute("SET search_path to THECIMS")
					cursor.execute("SELECT * FROM ADMIN WHERE username= %s AND password = %s", [username, password])
					admin = cursor.fetchone()
					
					if admin:
						print("ini admin 2")
						print(username)
						request.session['username'] = admin[0][0]
						request.session['isLogin'] = True
						request.session['role'] = 'Admin'
						print("ini admin")
						
					else:
						request.session['username'] = username
						request.session['isLogin'] = True
						request.session['role'] = 'Pemain'
						print("ini pemain")

					return HttpResponseRedirect('/')
			else:
				form.add_error("username", "Akun ini tidak ada!")
				return render(request, 'login/index.html', response)
		except Exception as e:
			print(e)
			return render(request, 'login/index.html', response)
	else:
		form = login_form(request.POST or None)
		response['form'] = form
		return render(request,'login/index.html',response)



# def login_page(request):
# 	form = login_form()
# 	return render(request, 'login/index.html', {'form': form})

# def user_login(request):
# 	form = login_form(request.POST or None)
# 	if (request.method == "POST" and form.is_valid()):
# 			username = request.POST['username']
# 			password = request.POST['password']
# 			if (login(request, username, password)):
# 				if request.session['role'] == 'Admin':
# 					print("yaa allah bisa yaa allah")
# 					return redirect("/homepage")
# 				elif request.session['role'] == 'Pemain':
# 					return redirect("/homepage")
# 			else:
# 				form.add_error("username", "Akun ini tidak ada!")
# 				return render(request, 'login/index.html', {'form':form})

# def login(request, username, password):
# 	with connection.cursor() as cursor:
# 		cursor.execute("SET search_path to THECIMS"),
# 		cursor.execute("SELECT * FROM AKUN WHERE username = %s", [username])
# 		row = cursor.fetchone()

# 		# cursor.execute("SELECT * FROM ADMIN WHERE username = %s AND password = %s", [username, password])
# 		# pemain = cursor.fetchone()

# 		if (row != None):
# 			request.session['username'] = row[0]
# 			request.session['role'] = check_role(username, password)
# 			# if (request.session['role'] == "Pemain"):
# 			# 	alamats = get_alamat_user(no_ktp)
# 			# 	request.session['alamats'] = []
# 			# 	for alamat in alamats:
# 			# 		request.session['alamats'].append(alamat[1] + " - " + alamat[2] + " Street No. " \
# 			# 										  + str(alamat[3]) + ", " + alamat[4] + " City, " \
# 			# 										  + alamat[5])
# 			# 	cursor.execute("SELECT * FROM ANGGOTA WHERE no_ktp = %s", [no_ktp])
# 			# 	row = cursor.fetchone()
# 			# 	request.session['poin'] = row[1]
# 			# 	request.session['level'] = row[2]
# 			return True
# 		elif (row == None):
# 			return False

# def check_availability(username):
# 	available = [True]

# 	with connection.cursor() as cursor:
# 		cursor.execute("SET search_path to THECIMS"),
# 		cursor.execute("SELECT * FROM AKUN WHERE username = %s", [username])
# 		username_row = cursor.fetchone()
# 		if username_row != None:
# 			available[0] = False

# 	print(available)
# 	return available

# def check_role(username, password):
# 	with connection.cursor() as cursor:
# 		cursor.execute("SET search_path to THECIMS"),
# 		cursor.execute("SELECT * FROM ADMIN WHERE username = %s and password = %s", [username, password])
# 		if (cursor.fetchone() != None):
# 			return "Admin"
# 		return "Pemain"
