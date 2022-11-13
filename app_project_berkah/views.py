from django.shortcuts import render
from datetime import date

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register/register_1.html')

def register_2(request):
    return render(request, 'register/register_2.html')

def register_3(request):
    return render(request, 'register/register_3.html')

def index(request): 
    return render(request, 'index.html')

def dashboard(request):
    # load expoert jupter notebook
    return render(request, 'dashboard.html')

def kasir(request):

    today = date.today()
    print(today)
    context = {
        'today' : today
    }
    return render(request, 'kasir.html', context)

def transaksi_penjualan(request):
    return render(request, 'transaksi_penjualan.html')

def input_barang(request):
    return render(request, 'input_barang.html')
