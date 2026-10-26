
n = int(input())

if n == 0:
    print("Nol")
elif n < 10:
    print("Satuan")
elif n < 20:
    print("Belasan")
elif n < 100:
    print("Puluhan")
else:
    print("Anda Menginput Melebihi Limit Bilangan")
