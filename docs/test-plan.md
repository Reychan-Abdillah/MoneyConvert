# Rencana Pengujian (Test Plan)

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan aplikasi konversi mata uang berjalan dengan benar, dapat mengambil nilai tukar dari API Frankfurter, dan menangani kesalahan tanpa menghentikan aplikasi secara tiba-tiba.

## 2. Ruang Lingkup Pengujian

Pengujian mencakup:

- Pengambilan nilai tukar melalui API Frankfurter.
- Perhitungan konversi mata uang.
- Validasi input pengguna.
- Penanganan kesalahan jaringan dan API.
- Tampilan dan interaksi antarmuka aplikasi.

## 3. Lingkungan Pengujian

- Bahasa pemrograman: Python.
- Antarmuka: CustomTkinter.
- HTTP client: Requests.
- Sumber nilai tukar: Frankfurter API.
- Metode pengujian: Pengujian manual.

## 4. Skenario Pengujian

| ID | Skenario | Hasil yang Diharapkan |
|---|---|---|
| TC-01 | Mengambil nilai tukar USD ke IDR | API mengembalikan nilai tukar yang valid. |
| TC-02 | Mengonversi USD ke IDR | Hasil konversi sesuai dengan nilai tukar yang diperoleh. |
| TC-03 | Memasukkan jumlah uang nol | Aplikasi menangani input nol sesuai aturan aplikasi. |
| TC-04 | Memasukkan jumlah uang negatif | Aplikasi menolak input jika jumlah negatif tidak diizinkan. |
| TC-05 | Memasukkan teks pada kolom jumlah | Aplikasi menampilkan pesan validasi. |
| TC-06 | Memilih kode mata uang yang tidak didukung | Aplikasi menampilkan pesan kesalahan yang sesuai. |
| TC-07 | Tidak ada koneksi internet | Aplikasi menangani kesalahan jaringan dan tetap terkendali. |
| TC-08 | API mengembalikan kesalahan | Aplikasi menampilkan pesan kesalahan, bukan traceback kepada pengguna. |
| TC-09 | Menjalankan aplikasi | Jendela aplikasi tampil dan dapat digunakan. |
| TC-10 | Mengubah mata uang asal atau tujuan | Aplikasi menggunakan pilihan mata uang yang benar dalam konversi. |

## 5. Kriteria Keberhasilan

Pengujian dinyatakan berhasil apabila:

- Hasil konversi dihitung dengan benar berdasarkan nilai tukar API.
- Input yang tidak valid ditangani dengan baik.
- Kesalahan jaringan dan API tidak menyebabkan aplikasi berhenti secara tidak terkendali.
- Antarmuka dapat digunakan sesuai fungsi yang dirancang.

## 6. Dokumentasi Hasil Pengujian

Setiap pengujian dicatat dengan informasi berikut:

- ID pengujian.
- Tanggal pengujian.
- Data yang digunakan.
- Hasil yang diharapkan.
- Hasil aktual.
- Status pengujian: PASS atau FAIL.
- Catatan jika ditemukan masalah.

## 7. Catatan

Pengujian dilakukan secara manual selama tahap pengembangan. Pengujian otomatis dapat ditambahkan pada tahap berikutnya untuk meningkatkan konsistensi dan keandalan aplikasi.