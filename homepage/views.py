from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request, 'homepage/index.html')

def homeAdmin(request):
	return render(request, 'homepage/home_admin.html')

def homePemain(request):
	return render(request, 'homepage/home_pemain.html')