from termcolor import cprint
import os

os.system('cls')

# Daftar warna valid
warna_valid = ["red", "green", "yellow", "blue", "magenta", "cyan"]

# Input nama
print("Input nama menggunakan huruf kapital!")
nama = input("Siapa yang ulang tahun? ")

# Tampilkan daftar warna secara manual
print("\nPilih warna kue dari:")
for i in warna_valid:
    print("-", i)
print("Pastikan penulisan warna benar ya!")

# Input warna (apa adanya)
warna = input("Masukkan warna kue: ")
if warna in warna_valid :
    warna_kue = "on_" + warna
else :
    warna_kue = "on_magenta"  # warna default kalau salah ketik

# Gambar lilin
cprint("\n    i   i   i", "yellow")
cprint("   | | | | | |", "blue")
cprint("    * * * * *", "red")

# Gambar kue
cprint(" "*5, end="")
cprint(" "*7, "white", "on_white")
for i in range (2):
    cprint(" "*5, end="")
    cprint(" "*7, "white", warna_kue)

cprint(" "*3, end="")
cprint(" "*11, "white", "on_white")
for i in range (2):
    cprint(" "*3, end="") 
    cprint(" "*11, "white", warna_kue)

cprint(" ", end="")
cprint(" "*15, "white", "on_white")
for i in range (4):
    cprint(" ", end="")
    cprint(" "*15, "white", warna_kue)

# Ucapan
print()
cprint(f"🎉 SELAMAT ULANG TAHUN, {nama}! 🎉", "yellow")
cprint("Semoga harimu semanis kue ini 🍰", "red")
