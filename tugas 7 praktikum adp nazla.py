NAMA_FILE = "catatan.txt"

f = open(NAMA_FILE, "a")
f.close()  

def baca_catatan():
    catatan = {}
    with open(NAMA_FILE, "r") as file:
        while True:
            judul = file.readline()
            if not judul:  
                break
            judul = judul.strip() 
            isi = file.readline()
            if not isi: 
                break
            isi = isi.strip() 
            pemisah = file.readline()
            if not pemisah.strip() == "---" :
               print(f"Peringatan: Format file tidak sesuai setelah judul '{judul}'.")
               continue 
            catatan[judul] = isi
    return catatan

def simpan_catatan(judul, isi):
    with open(NAMA_FILE, "a") as file:
        file.write(f"{judul}\n{isi}\n---\n")

def buat_catatan_baru():
    print("\n=== Buat Catatan Baru ===")
    judul = input("Masukkan judul catatan: ")
    isi = input("Masukkan isi catatan: ")
    simpan_catatan(judul, isi)
    print("Catatan berhasil disimpan!\n")

def lihat_catatan():
    catatan = baca_catatan()
    if len(catatan) == 0:
        print("Belum ada catatan yang tersedia.\n")
        return

    print("\n=== Daftar Judul Catatan ===")
    for judul in catatan:
        print(f"- {judul}")

    pilihan = input("\nMasukkan judul catatan yang ingin dibuka: ")
    if pilihan in catatan:
        print(f"\nIsi catatan '{pilihan}':\n{catatan[pilihan]}\n")
    else:
        print("Data tidak ditemukan.\n")

def main():
    while True:
        print("=== MENU UTAMA ===")
        print("1. Lihat catatan yang tersedia")
        print("2. Buat catatan baru")
        print("3. Exit")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            lihat_catatan()
        elif pilihan == "2":
            buat_catatan_baru()
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

main()
