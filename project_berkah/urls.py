from django.contrib import admin
from django.urls import path
from app_project_berkah.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # menu login - register
    path('login/', login),
    path('register_biodata_diri/', register),
    path('register_kredensial/', register_2),
    path('register_informasi_toko/', register_3),
    # --------------------
    path('index/', index),
    path('dashboard/', dashboard),
    # menu kasir
    path('kasir/', kasir),
    # menu transaksi penjualan
    path('transaksi_penjualan/', transaksi_penjualan),
    # menu input penjualan
    path('input_barang/', input_barang),
]
