from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request, 'homepage/index.html')

def homeAdmin(request):

	model = {
	'role': request.session['role'],
	'username': request.session['username']
	}
	return render(request, 'homepage/home_admin.html', model)

def homePemain(request):
	# model = {
	# 'username': request.session['username'],
	# 'email': request.session['email'],
	# 'no_hp': request.session['no_hp'],
	# 'koin': request.session['koin']

	# }
	return render(request, 'homepage/home_pemain.html')