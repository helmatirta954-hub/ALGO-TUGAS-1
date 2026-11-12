BOBOT_TUGAS, BOBOT_UTS, BOBOT_UAS = 0.3, 0.3, 0.4


def hitung_nilai_akhir(tugas, uts, uas):
    return BOBOT_TUGAS * tugas + BOBOT_UTS * uts + BOBOT_UAS * uas


def nilai_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    return "E"


def kelulusan(huruf):
    return huruf in ["A", "B", "C"]


def hitung_rata_rata(akhir):
    return sum(akhir) / len(akhir)


def hitung_jumlah_lulus(akhir):
    return sum(1 for a in akhir if kelulusan(nilai_huruf(a)))


def cari_indeks_tertinggi(akhir):
    return akhir.index(max(akhir))


def tampilkan_rekap(nama, akhir):
    print(f"{'Nama':<8}{'Akhir':<8}{'Huruf':<8}Keterangan")
    print("-" * 36)
    for n, a in zip(nama, akhir):
        h = nilai_huruf(a)
        print(f"{n:<8}{a:<8.2f}{h:<8}{'Lulus' if kelulusan(h) else 'Tidak lulus'}")


def tampilkan_tertinggi(nama, akhir):
    i = cari_indeks_tertinggi(akhir)
    print(f"Nilai akhir tertinggi  : {nama[i]} ({akhir[i]:.2f})")


def main():
    nama = ["Andi", "Bunga", "Citra", "Dimas", "Eka"]
    tugas = [80, 90, 60, 75, 30]
    uts = [70, 85, 45, 80, 40]
    uas = [90, 88, 50, 65, 35]

    akhir = [hitung_nilai_akhir(t, u, s) for t, u, s in zip(tugas, uts, uas)]

    tampilkan_rekap(nama, akhir)
    print("-" * 36)
    print(f"Rata-rata kelas        : {hitung_rata_rata(akhir):.2f}")
    print(f"Jumlah mahasiswa lulus : {hitung_jumlah_lulus(akhir)}")
    tampilkan_tertinggi(nama, akhir)


if __name__ == "__main__":
    main()