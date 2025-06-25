import os
import calendar
from termcolor import colored

os.system('cls')

nama_bulan_list = ["", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
singkatan_hari_list = ["S", "S", "R", "K", "J", "S", "M"]
daftar_warna_hari = ["yellow", "green", "blue", "magenta", "cyan", "red", "white"]

def format_baris_mingguan(minggu_data, data_kegiatan, tahun_val, bulan_val):
    hasil_minggu = []
    for tanggal_harian in minggu_data:
        if tanggal_harian == 0:
            hasil_minggu.append("   ")
        else:
            thn_str = str(tahun_val)
            bln_str = "0" + str(bulan_val) if bulan_val < 10 else str(bulan_val)
            hr_str = "0" + str(tanggal_harian) if tanggal_harian < 10 else str(tanggal_harian)
            tanggal_kunci = thn_str + "-" + bln_str + "-" + hr_str
            
            ada_kegiatan = False
            for kunci_kegiatan in data_kegiatan:
                if kunci_kegiatan == tanggal_kunci:
                    hari_teks = str(tanggal_harian)
                    if len(hari_teks) == 1:
                        hasil_minggu.append(colored(" " + hari_teks, "white", "on_" + data_kegiatan[kunci_kegiatan][1]) + " ")
                    else:
                        hasil_minggu.append(colored(hari_teks, "white", "on_" + data_kegiatan[kunci_kegiatan][1]) + " ")
                    ada_kegiatan = True
                    break
            if not ada_kegiatan:
                hari_teks = str(tanggal_harian)
                if len(hari_teks) == 1:
                    hasil_minggu.append(" " + hari_teks + " ")
                else:
                    hasil_minggu.append(hari_teks + " ")
    gabungan_string = ""
    for item_string in hasil_minggu:
        gabungan_string += item_string
    return gabungan_string

def buat_tampilan_bulan(tahun_val, bulan_val, data_kegiatan):
    hasil_tampilan_bulan = []
    judul_bulan = f"{nama_bulan_list[bulan_val]} {tahun_val}"
    lebar_sel_bulan = 21
    
    spasi_kiri_judul = (lebar_sel_bulan - len(judul_bulan)) // 2
    spasi_kanan_judul = lebar_sel_bulan - len(judul_bulan) - spasi_kiri_judul
    hasil_tampilan_bulan.append(" " * spasi_kiri_judul + judul_bulan + " " * spasi_kanan_judul)

    header_hari = ""
    for i in range(7):
        huruf_hari_ini = singkatan_hari_list[i]
        warna_hari_ini = daftar_warna_hari[i]
        header_hari += " " + colored(huruf_hari_ini, warna_hari_ini) + " " 
    hasil_tampilan_bulan.append(header_hari)

    kalender_bulan = calendar.monthcalendar(tahun_val, bulan_val)

    for minggu_data in kalender_bulan:
        hasil_tampilan_bulan.append(format_baris_mingguan(minggu_data, data_kegiatan, tahun_val, bulan_val))
    
    while len(hasil_tampilan_bulan) < 8:
        hasil_tampilan_bulan.append(" " * lebar_sel_bulan)

    return hasil_tampilan_bulan

def tampilkan_kalender_utama(tahun_val, data_kegiatan):
    lebar_sel_bulan = 21
    spasi_antar_kolom = 4
    total_lebar_tampilan = (lebar_sel_bulan + spasi_antar_kolom) * 4 - spasi_antar_kolom

    print("=" * total_lebar_tampilan)
    judul_utama = "MY ACTIVITY MARKER CALENDAR"
    spasi_kiri_judul_utama = (total_lebar_tampilan - len(judul_utama)) // 2
    spasi_kanan_judul_utama = total_lebar_tampilan - len(judul_utama) - spasi_kiri_judul_utama
    print(" " * spasi_kiri_judul_utama + judul_utama + " " * spasi_kanan_judul_utama)
    print("=" * total_lebar_tampilan)
    for baris_idx in range(3):
        data_baris_multi_kolom = [[] for _ in range(8)]
        for kolom_idx in range(4):
            bulan_ini = baris_idx * 4 + kolom_idx + 1
            blok_satu_bulan = buat_tampilan_bulan(tahun_val, bulan_ini, data_kegiatan)
            for i in range(8):
                data_baris_multi_kolom[i].append(blok_satu_bulan[i])
        for i in range(8):
            teks_baris_akhir = ""
            for j in range(len(data_baris_multi_kolom[i])):
                konten_kolom = data_baris_multi_kolom[i][j]
                teks_baris_akhir += konten_kolom
                if j < len(data_baris_multi_kolom[i]) - 1:
                    teks_baris_akhir += " " * spasi_antar_kolom
            print(teks_baris_akhir)
        print()

def baca_data_kegiatan():
    data_kegiatan_dict = {}
    
    file_buat_kosong = open("data_kegiatan.txt", "w")
    file_buat_kosong.close()

    file_baca = open("data_kegiatan.txt", "r") 
    semua_baris = file_baca.readlines()
    file_baca.close()

    for baris_data in semua_baris:
        baris_data = baris_data.strip()
        
        if not baris_data: continue
        
        bagian_baris = []
        bagian_saat_ini = ""
        for karakter in baris_data:
            if karakter == '|':
                bagian_baris.append(bagian_saat_ini)
                bagian_saat_ini = ""
            else:
                bagian_saat_ini += karakter
        bagian_baris.append(bagian_saat_ini)
        
        if len(bagian_baris) == 3:
            tanggal_k, kegiatan_k, warna_k = bagian_baris
            data_kegiatan_dict[tanggal_k] = [kegiatan_k, warna_k]
    return data_kegiatan_dict

def simpan_data_kegiatan(data_kegiatan_dict):
    file_tulis = open("data_kegiatan.txt", "w")
    for kunci_kegiatan in data_kegiatan_dict:
        file_tulis.write(kunci_kegiatan + "|" + data_kegiatan_dict[kunci_kegiatan][0] + "|" + data_kegiatan_dict[kunci_kegiatan][1] + "\n")
    file_tulis.close()

def tambah_entri_kegiatan(data_kegiatan_dict, tahun_val):
    os.system('cls')
    print("\nMasukkan nama bulan (1-12):")
    input_bulan_str = input("> ")
    input_bulan_int = int(input_bulan_str)

    tampilan_bulan_saja = buat_tampilan_bulan(tahun_val, input_bulan_int, data_kegiatan_dict)
    for baris_tampilan in tampilan_bulan_saja:
        print(baris_tampilan)
    print("Tanggal berapa ingin menambahkan kegiatan?")
    input_tanggal_str = input("> ")
    input_tanggal_int = int(input_tanggal_str)

    print("Kegiatan apa?")
    input_kegiatan = input("> ")
    print("Pilih warna: red, green, yellow, blue, magenta, cyan")
    input_warna = input("> ")

    bln_fmt = "0" + str(input_bulan_int) if input_bulan_int < 10 else str(input_bulan_int)
    tgl_fmt = "0" + str(input_tanggal_int) if input_tanggal_int < 10 else str(input_tanggal_int)
    tanggal_format_penuh = str(tahun_val) + "-" + bln_fmt + "-" + tgl_fmt
    data_kegiatan_dict[tanggal_format_penuh] = [input_kegiatan, input_warna]
    simpan_data_kegiatan(data_kegiatan_dict)
    print("Kegiatan ditambahkan!")
    input("Tekan Enter untuk melanjutkan...")

def hapus_entri_kegiatan(data_kegiatan_dict):
    os.system('cls')
    print("\nTanggal kegiatan yang ingin dihapus (formatYYYY-MM-DD):")
    tanggal_hapus = input("> ")
    if tanggal_hapus in data_kegiatan_dict:
        del data_kegiatan_dict[tanggal_hapus]
        simpan_data_kegiatan(data_kegiatan_dict)
        print("Kegiatan dihapus.")
    else:
        print("Tanggal tidak ditemukan dalam kegiatan.")
    input("Tekan Enter untuk melanjutkan...")
    return data_kegiatan_dict

def lihat_daftar_kegiatan(data_kegiatan_dict):
    os.system('cls')
    print("=" * 40)
    judul_daftar_kegiatan = "DAFTAR KEGIATAN"
    spasi_kiri_daftar_kegiatan = (40 - len(judul_daftar_kegiatan)) // 2
    spasi_kanan_daftar_kegiatan = 40 - len(judul_daftar_kegiatan) - spasi_kiri_daftar_kegiatan
    print(" " * spasi_kiri_daftar_kegiatan + judul_daftar_kegiatan + " " * spasi_kanan_daftar_kegiatan)
    print("=" * 40)
    if not data_kegiatan_dict:
        print("Belum ada kegiatan yang tercatat.")
    else:
        for tanggal_kunci, detail_kegiatan in data_kegiatan_dict.items():
            deskripsi_kegiatan = detail_kegiatan[0]
            warna_kegiatan = detail_kegiatan[1]
            print(f"{tanggal_kunci}: {colored(deskripsi_kegiatan, warna_kegiatan)}")
    print("=" * 40)
    input("Tekan Enter untuk kembali ke menu utama...")

tahun_saat_ini = 2025
data_kegiatan_global = baca_data_kegiatan()
os.system('cls')
tampilkan_kalender_utama(tahun_saat_ini, data_kegiatan_global)

while True:
    print("\n1. Tambah kegiatan")
    print("2. Hapus kegiatan")
    print("3. Lihat kegiatan")
    print("4. Selesai")
    pilihan_menu = input("> ")
    if pilihan_menu == "1":
        tambah_entri_kegiatan(data_kegiatan_global, tahun_saat_ini)
        os.system('cls')
        tampilkan_kalender_utama(tahun_saat_ini, data_kegiatan_global)
    elif pilihan_menu == "2":
        data_kegiatan_global = hapus_entri_kegiatan(data_kegiatan_global)
        os.system('cls')
        tampilkan_kalender_utama(tahun_saat_ini, data_kegiatan_global)
    elif pilihan_menu == "3":
        lihat_daftar_kegiatan(data_kegiatan_global)
        os.system('cls')
        tampilkan_kalender_utama(tahun_saat_ini, data_kegiatan_global)
    elif pilihan_menu == "4":
        break
    else: 
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        os.system('cls')
        tampilkan_kalender_utama(tahun_saat_ini, data_kegiatan_global)