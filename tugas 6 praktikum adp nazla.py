def hitung_tagihan_listrik(pemakaian_kwh, golongan=3):
    tarif_awal = [1500, 2500, 4000, 5000]
    tarif_lanjut = [2000, 3000, 5000, 7000]

    index = golongan - 1
    tarif_pertama = tarif_awal[index]
    tarif_kedua = tarif_lanjut[index]

    if pemakaian_kwh <= 100:
        total = pemakaian_kwh * tarif_pertama
    else:
        total = (100 * tarif_pertama) + ((pemakaian_kwh - 100) * tarif_kedua)

    return total

# Input jumlah pemakaian listrik
pemakaian = int(input("Masukkan jumlah pemakaian listrik (kWh): "))

# Input golongan (boleh kosong)
input_golongan = input("Masukkan golongan (1-4): ")

# Tentukan golongan: pakai default 3 kalau kosong
if input_golongan == "":
    golongan = 3
else:
    golongan = int(input_golongan)

# Hitung dan tampilkan hasil
total_tagihan = hitung_tagihan_listrik(pemakaian, golongan)
print("Total tagihan listrik: Rp", total_tagihan) 
