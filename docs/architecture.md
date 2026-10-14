STRUKTUR KOMPONEN


# Struktur Proyek
```t
convertet-money/
├── docs/
│   ├── architecture.md   # Dokumentasi arsitektur sistem
│   ├── requirements.md   # Kebutuhan dan batasan aplikasi
│   └── test-plan.md      # Rencana pengujian aplikasi
├── src/
│   ├── api_client.py     # Komunikasi dengan Frankfurter API
│   └── converter.py      # Logika perhitungan konversi
├── tests/                # Pengujian otomatis
├── .gitignore            # File yang dikecualikan dari Git
├── main.py               # Titik masuk aplikasi
└── README.md             # Dokumentasi utama proyek
```



# FILE UTAMA

# engine
# api_client.py -> 
Berfungsi sebagai lapisan komunikasi antara aplikasi dan Frankfurter API.

Tanggung jawab :
-Menentukan alamat endpoint API.
- Mengirim permintaan HTTP.
- Menerima dan mengolah respons API.
- Mengambil nilai tukar dari respons.
- Menangani kesalahan komunikasi dan respons HTTP.

<!-- Komponen ini tidak bertanggung jawab atas interaksi terminal 
atau perhitungan nilai konversi. -->
# Conversion Engine — src/converter.py

Berfungsi sebagai lapisan logika bisnis untuk menghitung konversi mata uang.

Tanggung jawab :
- Menerima jumlah uang dan nilai tukar.
- Menghitung nilai hasil konversi.
- Menggunakan tipe numerik yang sesuai untuk perhitungan uang.
- Mengembalikan hasil perhitungan kepada pemanggil.

<!-- Komponen ini tidak melakukan permintaan jaringan, membaca input terminal,
 atau menampilkan hasil secara langsung. -->



----------------------------------------------------------------------------------
# Antar Muka
# main.py -> 
sebagai titik masuk dan tampilan utama yang dilihat oleh pengguna
berfungsi mengatur alur kerja program 

Tanggung Jawab :
- menampilkan aplikasi antar muka
- mengambil input pengguna
- Mengatur pemanggilan komponen.    
- menampilkan hasil dari kurs


# Diagram
+---------------------------+
|          Pengguna         |
+---------------------------+
              |
              v
+---------------------------+
|          main.py          |
|   Pengatur Alur Aplikasi  |
+---------------------------+
              |
              v
+---------------------------+
|       api_client.py       |
|    Komunikasi dengan API  |
+---------------------------+
              |
              v
+---------------------------+
|     Frankfurter API       |
|       Data Nilai Tukar    |
+---------------------------+
              |
              v
+---------------------------+
|       Nilai Tukar         |
+---------------------------+
              |
              v
+---------------------------+
|       converter.py        |
|     Logika Konversi       |
+---------------------------+
              |
              v
+---------------------------+
|      Hasil Konversi       |
+---------------------------+
              |
              v
+---------------------------+
|      main.py / Terminal   |
+---------------------------+



Tugas dan Tanggung Jawab =:->

Setiap Komponen hanya menangani tugas yang sesuai peran nya
Logika konversi tidak bergantung pada jaringan atau layanan eksternal.
Komponen dapat diuji secara terpisah dengan masukan yang terkontrol.
Perubahan pada mekanisme komunikasi API tidak mengharuskan perubahan pada logika perhitungan, selama antarmuka antarkomponen tetap konsisten.
Struktur dapat diperluas apabila kebutuhan baru muncul, tanpa menambahkan lapisan arsitektur yang belum diperlukan.