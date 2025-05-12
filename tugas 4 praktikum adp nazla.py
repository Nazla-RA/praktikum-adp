no_pelanggan = []
nama_pelanggan = []
total_belanja = []

while True :
    print("\n===== Menu Toko =====")
    print("1. Tambah Data Pelanggan")
    print("2. Hapus Data Pelanggan")
    print("3. Cetak Data Pelanggan")
    print("4. Keluar")
    print("=========================")

    pilihan = input ("Masukkan Pilihan Anda: ")

    if pilihan == '1' :
        print("\n--- Tambah Data Pelanggan ---")
        no = int(input("No. Pelanggan: "))
        nama = str(input("Nama Pelanggan: "))
        belanja = float(input("Total Belanja: "))
        no_pelanggan.append(no)
        nama_pelanggan.append(nama)
        total_belanja.append(belanja)
        print("Pelanggan Berhasil Ditambahkan.")
    elif pilihan == '2' :
        print("\n--- Hapus Data Pelanggan ---")
        cari_no = int(input("Masukkan No. Pelanggan yang ingin dihapus: "))
        if cari_no in no_pelanggan :
            x = no_pelanggan.index(cari_no)
            del no_pelanggan[x]
            del nama_pelanggan[x]
            del total_belanja[x]
            print("Data Pelanggan Berhasil Dihapus.")
        else :
            print("No. Pelanggan tidak ditemukan.")
    elif pilihan == '3' :
        print("\n--- Data Pelanggan ---")
        print()
        if not no_pelanggan :
            print("Belum ada data pelanggan.")
        else :
            print(f"{'No' : <5} | {'Nama' : <20} | {'Belanja' :<10}")
            for i in range (len(no_pelanggan)) :
                print(f"{no_pelanggan[i] :<5} | {nama_pelanggan[i] :<20} | {total_belanja[i] :<,.2f}")
    elif pilihan == '4' :
        print("Terima kasih!")
        break
    else :
        print("Pilihan tidak valid. Silahkan coba lagi.")