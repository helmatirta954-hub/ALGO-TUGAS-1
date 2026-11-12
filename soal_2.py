BATAS_JARAK = 20
BIAYA_JARAK = 5000


def biaya_berat(berat):
    return 10000 + max(0, berat - 2) * 4000


def biaya_jarak(jarak):
    return BIAYA_JARAK if jarak > BATAS_JARAK else 0


def potongan(ongkos, anggota):
    return ongkos // 10 if anggota else 0


def ongkos_akhir(berat, jarak, anggota):
    ongkos = biaya_berat(berat) + biaya_jarak(jarak)
    return ongkos - potongan(ongkos, anggota)


def cetak_struk(nama, berat, jarak, anggota):
    b1 = biaya_berat(berat)
    b2 = biaya_jarak(jarak)
    p = potongan(b1 + b2, anggota)

    print(f"\nPelanggan    : {nama}")
    print(f"Biaya berat  : Rp{b1:,}")
    print(f"Biaya jarak  : Rp{b2:,}")
    if p > 0:
        print(f"Potongan     : -Rp{p:,}")
    print(f"Ongkos akhir : Rp{ongkos_akhir(berat, jarak, anggota):,}")


def main():
    pesanan = [("Rina", 1, 10, False), ("Sari", 5, 25, False),
               ("Tono", 5, 25, True), ("Umar", 2, 30, True),
               ("Vina", 8, 15, False)]

    total = 0
    for nama, berat, jarak, anggota in pesanan:
        cetak_struk(nama, berat, jarak, anggota)
        total += ongkos_akhir(berat, jarak, anggota)

    print(f"\nTotal pendapatan ongkos kirim hari ini: Rp{total:,}")


if __name__ == "__main__":
    main()