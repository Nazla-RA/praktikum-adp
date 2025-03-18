n = int(input("Silahkan masukkan jumlah pasrtisi (n) : "))
b = 3
a = 1
dx = (b - a) / n

total = 0
for i in range (1, n +1) :
    xi = a + i*dx
    f_xi = xi**2 + 2*xi
    luas_partisi =  f_xi * dx
    total = total + luas_partisi

print(f"Luas daerah dari fungsi x^2+2x dengan batas daerah x= {b} dan x={a} dan jumlah partisi n={n} adalah {total}")
