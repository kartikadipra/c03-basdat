from django.shortcuts import render
from django.db import connection
from collections import namedtuple

# Create your views here.
def index(request):
    return render(request, 'index.html')
