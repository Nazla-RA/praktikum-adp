n = int(input("Silahkan Input Jumlah Pendaftar : "))
print()

for i in range (n):
    print(f"Data Pendaftar ke-{i+1} ")
    nama =  input("Nama : ")
    mata_kuliah = input("Mata Kuliah yang diminati: ")
    
    wawancara = float(input("Nilai Wawancara (1-100): "))
    while wawancara < 1 or wawancara > 100 :
        print()
        print("Silahkan input nilai dari 1-100!")
        wawancara = float(input("Nilai Wawancara (1-100): "))

    tes_tulis = float(input("Nilai Tes Tulis (1-100): "))
    while tes_tulis < 1 or tes_tulis > 100 :
        print()
        print("Silahkan input nilai dari 1-100!")
        tes_tulis = float(input("Nilai Tes Tulis (1-100): "))

    mengajar = float(input("Nilai Mengajar (1-100): "))
    while mengajar < 1 or mengajar > 100 :
        print()
        print ("Silahkan input nilai dari 1-100!")
        mengajar = float(input("Nilai Mengajar (1-100): "))

    rata_rata = (wawancara + tes_tulis + mengajar)/3
    if rata_rata >= 80 :
        predikat = "LULUS"
    else :
        predikat = "TIDAK LULUS"
    print(f"Rata-rata: {rata_rata:.2f}")    
    print(predikat)
    print()
    
    





