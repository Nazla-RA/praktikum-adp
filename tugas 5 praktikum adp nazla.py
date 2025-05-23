print("=== Program Input Titik dan Hitung Jarak ===")

# Input jumlah titik
n = int(input("Masukkan jumlah titik: "))
titik = []

# Input titik satu per satu
for i in range(n):
    print(f"Titik ke-{i+1}:")

    # Input x
    while True:
        x = input("  Masukkan x: ")
        valid = True
        jumlah_desimal = 0

        if x == "":
            valid = False
        else:
            if x[0] == "-":
                if len(x) == 1:
                    valid = False
                else:
                    angka = x[1:]  # buang tanda minus
            else:
                angka = x  # bukan negatif

            if valid:
                for huruf in angka:
                    if huruf == ".":
                        jumlah_desimal += 1
                    elif huruf < '0' or huruf > '9':
                        valid = False
                        break
                if jumlah_desimal > 1:
                    valid = False

        if valid:
            x = float(x)
            break
        else:
            print("  x harus berupa angka!")

    # Input y
    while True:
        y = input("  Masukkan y: ")
        valid = True
        jumlah_desimal = 0

        if y == "":
            valid = False
        else:
            if y[0] == "-":
                if len(y) == 1:
                    valid = False
                else:
                    angka = y[1:]  # buang tanda minus
            else:
                angka = y  # bukan negatif

            if valid:
                for huruf in angka:
                    if huruf == ".":
                        jumlah_desimal += 1
                    elif huruf < '0' or huruf > '9':
                        valid = False
                        break
                if jumlah_desimal > 1:
                    valid = False

        if valid:
            y = float(y)
            break
        else:
            print("  y harus berupa angka!")

    titik.append([x, y])

# Tampilkan semua titik
print("\nTitik yang dimasukkan:")
for i in range(n):
    print(f"Titik ke-{i+1}: ({titik[i][0]}, {titik[i][1]})")

# Hitung dan tampilkan jarak antar titik
print("\nJarak antar titik:")
for i in range(n):
    for j in range(i+1, n):
        dx = titik[i][0] - titik[j][0]
        dy = titik[i][1] - titik[j][1]
        jarak = (dx * dx + dy * dy) ** 0.5
        print(f"Jarak Titik {i+1} ke Titik {j+1} = {jarak:.2f}")
