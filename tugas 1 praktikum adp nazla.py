print("Selamat Datang di Toserba Ci Mehong")

barang = {
    "Minyak Telon" : 73000,
    "Kecap Asin" : 50000,
    "Telor Asin" : 69000,
    "Gula Pasir" : 80000,
    "Bedak Bayi" : 75000,
    "Mie Gaga" : 65000,
    "Susu Sapi" : 98000,
    "Minyak Sayur" : 100000,
    "Nutrijel" : 70000,
    "Sabun Bayi" : 65000,
}

print("Daftar Barang yang Tersedia:")
print("1. Minyak Telon: Rp73000")
print("2. Kecap Asin: Rp50000")
print("3. Telor Asin: Rp69000")
print("4. Gula Pasir: Rp80000")
print("5. Bedak Bayi: Rp75000")
print("6. Mie Gaga: Rp65000")
print("7. Susu Sapi: Rp98000")
print("8. Minyak Sayur: Rp100000")
print("9. Nutrijel: Rp70000")
print("10. Sabun Bayi: Rp65000")

nama_barang = input("Masukkan Nama Barang: ")
kuantitas = int(input(f"Masukkan jumlah {nama_barang}: "))

if nama_barang == "Minyak Telon":
    harga_satuan = 73000
elif nama_barang == "Kecap Asin":
    harga_satuan = 50000
elif nama_barang == "Telor Asin":
    harga_satuan = 69000
elif nama_barang == "Gula Pasir":
    harga_satuan = 80000
elif nama_barang == "Bedak Bayi":
    harga_satuan = 75000
elif nama_barang == "Mie Gaga":
    harga_satuan = 65000
elif nama_barang == "Susu Sapi":
    harga_satuan = 98000
elif nama_barang == "Minyak Sayur":
    harga_satuan = 100000
elif nama_barang == "Nutrijel":
    harga_satuan = 70000
elif nama_barang == "Sabun Bayi":
    harga_satuan = 65000
else:
    harga_satuan = 0

harga_total = harga_satuan * kuantitas

if harga_total < 1000000:
    diskon = 0
elif 1000000 <= harga_total <= 1500000:
    diskon = 0.10 * harga_total
else:
    diskon = 0.15 * harga_total

total_bayar = harga_total - diskon

print(f"\nNama Barang     : {nama_barang}")
print(f"Kuantitas      : {kuantitas}")
print(f"Harga Satuan   : Rp{harga_satuan}")
print(f"Harga Total    : Rp{harga_total}")
print(f"Potongan Harga : Rp{diskon}")
print(f"Total Bayar    : Rp{total_bayar}")