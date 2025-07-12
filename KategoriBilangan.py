def kategori_bilangan(n):
    kategori = []

    # Bilangan Bulat (semua bilangan negatif, nol, dan positif tanpa koma)
    kategori.append("bulat")

    # Bilangan Cacah (0 dan semua bilangan asli/positif tanpa koma)
    if n >= 0:
        kategori.append("cacah")

    # Bilangan Asli (bilangan bulat positif >= 1)
    if n >= 1:
        kategori.append("asli")

    # Ganjil / Genap
    if n % 2 == 0: #jika hasil sisa bagi/modulus n di bagi 2 sama dengan nol
        kategori.append("genap")
    else:
        kategori.append("ganjil")

    # Bilangan Prima
    if n >= 2:
        is_prima = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prima = False
                break
        if is_prima:
            kategori.append("prima")
        else:
            kategori.append("komposit")
    elif n >= 1:
        kategori.append("komposit")

    return kategori

def mainToni():
    angka = int(input("Ketik angka : "))
    hasil = kategori_bilangan(angka)
    print(hasil)

if __name__ == "__main__":
    mainToni()
