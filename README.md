Aplikasi Konversi Mata uang berbasis Aplikasi
yang dibangun menggunakan python
frankfurter api untuk mengambil nilai mata uang
tx untuk menampilkan aplikasi dengan tampilan menarik

Overview


Features
- Mendukung Pemilihan mata uang asal dan tujuan yang ingin di konversikan
- mengisi nilai mata uang yang ingin dikonversikan
- menghitung hasil konversi berdasarkan nilai tukar yang di peroleh
- menangani response HTTP dari API

Tech Stack
- python --- Sebagai bahasa pemrograman utama
- FrakFurter API -- sebagai penyediaan data nilai mata uang realtime
- request mengirim http ke api 


Project Struktur
```t
convertet-money/
├── docs/
│   ├── architecture.md
│   ├── requirements.md
│   └── test-plan.md
├── src/
│   ├── api_client.py
│   └── converter.py
├── tests/
├── main.py
├── README.md
└── .gitignore
```



Architecture

Aplikasi menggunakan pemisahan tanggung jawab agar kode lebih mudah dipahami, diuji, dan dikembangkan.

main.py — mengelola alur utama aplikasi dan interaksi pengguna.

src/api_client.py — menangani komunikasi dengan Frankfurter API.

src/converter.py — menangani perhitungan konversi mata uang.

tests/ — tempat pengujian aplikasi.

docs/ — dokumentasi kebutuhan, arsitektur, dan rencana pengujian.


Installation
# 1. Clone Repository
```t
git clone <repository-url>
cd convertet-money
```



# 2. Create Virtual Environment
```t
python -m venv .venv
```
# Aktifkan virtual environment di Windows:
```t
.venv\Scripts\activate
```

# 3. Install Dependencies
```t
pip install requests
```
# 4. Run the Application
```t
python main.py
```



# API Reference
Proyek ini menggunakan Frankfurter API.

Endpoint yang digunakan untuk mengambil nilai tukar:
GET https://api.frankfurter.dev/v2/rate/{base}/{quote}

Respons API menyediakan informasi nilai tukar, termasuk mata uang asal, mata uang tujuan, tanggal, dan nilai kurs.




# Documentation

Dokumentasi proyek tersedia di direktori docs/:
- Architecture
- Requirements
- Test Plan


# Project Status
In Development

Proyek ini sedang dikembangkan secara bertahap sebagai sarana mempelajari Python, OOP, integrasi API, dan praktik pengembangan perangkat lunak.

__License__
! Belum ditentukan.
