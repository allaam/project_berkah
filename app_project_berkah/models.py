# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BiodataDiri(models.Model):
    id_pengguna = models.AutoField(primary_key=True)
    nama_lengkap = models.CharField(max_length=255)
    tgl_lahir = models.DateField()
    alamat = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=10)
    no_telp = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'biodata_diri'


class InformasiToko(models.Model):
    id_toko = models.IntegerField(primary_key=True)
    no_kredensial = models.ForeignKey(
        'Kredensial', models.DO_NOTHING, db_column='no_kredensial')
    nama_toko = models.CharField(max_length=50)
    alamat_toko = models.CharField(max_length=255)
    jenis_toko = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s %s %s %s' % (self.id_toko, self.no_kredensial, self.nama_toko, self.alamat_toko, self.jenis_toko)

    class Meta:
        managed = False
        db_table = 'informasi_toko'


class Kredensial(models.Model):
    no_kredensial = models.IntegerField(primary_key=True)
    id_pengguna = models.ForeignKey(
        BiodataDiri, models.DO_NOTHING, db_column='id_pengguna')
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return '%s %s %s %s %s' % (self.no_kredensial, self.id_pengguna, self.email, self.username, self.password)

    class Meta:
        managed = False
        db_table = 'kredensial'


class ListBarang(models.Model):
    id_barang = models.IntegerField(primary_key=True)
    id_toko = models.ForeignKey(
        InformasiToko, models.DO_NOTHING, db_column='id_toko')
    nama_barang = models.CharField(max_length=50, null=True)
    harga = models.IntegerField(null=True, blank=True)
    tgl_input = models.DateTimeField(null=True, blank=True)
    tgl_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id_barang, self.id_toko, self.nama_barang, self.harga, self.tgl_input, self.tgl_update)

    class Meta:
        managed = False
        db_table = 'list_barang'


class LogBarang(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_barang = models.IntegerField()
    status = models.CharField(max_length=255)
    tanggal = models.DateTimeField()

    def __str__(self):
        return '%s %s %s %s' % (self.id_log, self.id_barang, self.status, self.tanggal)

    class Meta:
        managed = False
        db_table = 'log_barang'


class Transaksi(models.Model):
    id_transaksi = models.IntegerField(primary_key=True)
    id_barang = models.IntegerField()
    qty = models.IntegerField()
    harga_total = models.IntegerField()
    jumlah_bayar = models.IntegerField()
    jumlah_kembali = models.IntegerField()
    tgl_transaksi = models.DateTimeField()

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.id_transaksi, self.id_barang, self.qty, self.harga_total, self.jumlah_bayar, self.jumlah_kembali, self.tgl_transaksi)

    class Meta:
        managed = False
        db_table = 'transaksi'
