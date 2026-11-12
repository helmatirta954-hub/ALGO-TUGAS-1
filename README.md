# ALGO-TUGAS-1

SOAL 1
BOBOT_TUGAS, BOBOT_UTS, BOBOT_UAS = 0.3, 0.3, 0.4
(Bobot 30%, 30%, 40% disimpan di satu tempat. Kalau bobot berubah, cukup ubah baris ini)

return BOBOT_TUGAS * tugas + BOBOT_UTS * uts + BOBOT_UAS * uas
(Mengalikan tiap nilai dengan bobotnya lalu menjumlahkan. Untuk Andi: 0,3×80 + 0,3×70 + 0,4×90 = 81)
Tentukan_huruf(nilai
(Mengecek dari batas tertinggi ke terendah: ≥85 A, ≥70 B, ≥55 C, ≥40 D, sisanya E. Karena dicek berurutan, nilai 81 gagal di syarat A, lalu lolos di syarat B, sehingga hasilnya B. Syarat bawah (misalnya “< 85”) tidak perlu ditulis, sebab nilai yang sampai ke baris itu pasti sudah gagal di syarat sebelumnya)

apakah_lulus(huruf)
return huruf in ("A", "B", "C")
(Mengembalikan True jika huruf A, B, atau C, dan False jika D atau E)

hitung_rata_rata(akhir)
sum(akhir) / len(akhir): jumlah semua nilai dibagi banyaknya mahasiswa.
hitung_jumlah_lulus(akhir)
return sum(1 for a in akhir if apakah_lulus(tentukan_huruf(a)))
(Untuk setiap nilai, diubah dulu menjadi huruf, dicek lulus atau tidak, dan setiap yang lulus dihitung 1. Hasil akhirnya adalah banyaknya mahasiswa lulus)

cari_indeks_tertinggi(akhir)
max(akhir) mencari nilai terbesar, lalu .index(...) mengambil posisinya di daftar. Posisi ini dipakai untuk mengambil nama yang sesuai.

tampilkan_rekap(nama, akhir) (void)
(Mencetak judul kolom, lalu mengulang setiap mahasiswa. zip(nama, akhir) memasangkan nama dengan nilainya. Di tiap baris dihitung huruf dan keterangannya. Format {a:<8.2f} berarti rata kiri, lebar 8 karakter, dua angka desimal. Fungsi ini tidak punya return karena tugasnya hanya mencetak)

tampilkan_tertinggi(nama, akhir) (void)
(Memanggil cari_indeks_tertinggi, lalu mencetak nama dan nilai pada posisi itu)

Alur di main()
1. Menyimpan data dalam empat daftar: nama, tugas, uts, uas. Urutannya sejajar, jadi indeks     0 adalah Andi di keempatnya.
2. Menghitung nilai akhir semua mahasiswa sekaligus:
   akhir = [hitung_nilai_akhir(t, u, s) for t, u, s in zip(tugas, uts, uas)]
3. Mencetak tabel rekap.
4. Mencetak rata-rata, jumlah lulus, dan mahasiswa tertinggi.

Baris terakhir if __name__ == "__main__": main() menjalankan program hanya saat file dijalankan langsung.


SOAL 2

Konstanta
BATAS_JARAK dan BIAYA_JARAK menyimpan aturan jarak di satu tempat, jadi kalau kebijakan berubah cukup ubah dua baris ini.

Fungsi yang mengembalikan nilai
rupiah(angka): mengubah angka jadi teks berformat Rp10.000.
biaya_berat(berat): Rp10.000 dasar, ditambah Rp4.000 untuk tiap kg di atas 2. max(0, berat - 2) memastikan paket 1 kg atau 2 kg tidak kena biaya tambahan.
biaya_jarak(jarak): Rp5.000 jika jarak lebih dari 20 km, selain itu 0.
potongan(ongkos, anggota): 10% dari ongkos jika anggota, selain itu 0. // 10 adalah pembagian bulat supaya hasilnya tidak berkoma.
ongkos_akhir(berat, jarak, anggota): biaya berat + biaya jarak, dikurangi potongan.

Fungsi void
cetak_struk(...): hanya mencetak satu struk (nama, biaya berat, biaya jarak, potongan kalau ada, ongkos akhir). Tidak punya return.

Alur main()
Menyimpan data pesanan dalam daftar tuple (nama, berat, jarak, anggota).
Mengulang tiap pesanan: mencetak struk, lalu menambahkan ongkos akhirnya ke total.
Mencetak total pendapatan: Rp108.800.

