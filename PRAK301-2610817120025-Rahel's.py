
angka = list(map(int, input().split()))

if len(angka) > 1 and angka[0] > angka[1]:
    angka[0], angka[1] = angka[1], angka[0]

if len(angka) > 2 and angka[1] > angka[2]:
    angka[1], angka[2] = angka[2], angka[1]

if len(angka) > 2 and angka[0] > angka[1]:
    angka[0], angka[1] = angka[1], angka[0]

print(*angka)
