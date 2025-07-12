def cari_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cari_kpk(a, b):
    return abs(a * b) // cari_fpb(a, b)

def mainToni():
    inputan1 = int(input("Ketik angka pertama\t: "))
    inputan2 = int(input("Ketik angka kedua\t: "))

    hasil_fpb = cari_fpb(inputan1, inputan2)
    hasil_kpk = cari_kpk(inputan1, inputan2)

    print("FPB dari", inputan1, "dan", inputan2, "adalah :", hasil_fpb)
    print("KPK dari", inputan1, "dan", inputan2, "adalah :", hasil_kpk)

mainToni()

