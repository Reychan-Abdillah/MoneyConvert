
# MoneyConvert

Aplikasi desktop untuk konversi mata uang yang dibangun menggunakan Python dan CustomTkinter, dengan Frankfurter API sebagai sumber data nilai tukar.

MoneyConvert dirancang untuk menyediakan pengalaman konversi mata uang yang sederhana melalui antarmuka grafis yang bersih dan mudah digunakan.

## Overview

MoneyConvert merupakan proyek pengembangan aplikasi desktop yang berfokus pada penerapan Python, pemrograman berorientasi objek (OOP), integrasi REST API, dan pemisahan tanggung jawab antarkomponen.

Aplikasi mengambil nilai tukar dari Frankfurter API, kemudian menggunakannya untuk menghitung hasil konversi berdasarkan nominal dan mata uang yang dipilih pengguna.

## Features

- Memilih mata uang asal dan mata uang tujuan.
- Memasukkan nominal uang yang ingin dikonversi.
- Mengambil nilai tukar melalui Frankfurter API.
- Menghitung dan menampilkan hasil konversi.
- Menampilkan informasi nilai tukar yang digunakan.
- Memvalidasi input nominal.
- Menangani kesalahan HTTP dan kegagalan permintaan API.

## Tech Stack

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| CustomTkinter | Membangun antarmuka grafis aplikasi desktop |
| Requests | Mengirim permintaan HTTP ke API |
| Frankfurter API | Menyediakan data nilai tukar mata uang |
| Git | Mengelola versi kode sumber |

## Project Structure

```text
convertet-money/
├── docs/
│   ├── architecture.md
│   └── test-plan.md
├── src/
│   ├── __init__.py
│   ├── api_client.py
│   └── converter.py
├── tests/
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### Struktur Komponen

- `main.py` — titik masuk aplikasi, pengelolaan antarmuka grafis, dan interaksi pengguna.
- `src/api_client.py` — menangani komunikasi dengan Frankfurter API.
- `src/converter.py` — menyediakan logika perhitungan konversi mata uang.
- `tests/` — direktori untuk pengujian aplikasi.
- `docs/` — menyimpan dokumentasi kebutuhan, arsitektur, dan rencana pengujian.
- `requirements.txt` — mencatat dependency Python yang diperlukan.
- `.gitignore` — menentukan file yang tidak disertakan dalam version control.

## Architecture

MoneyConvert menggunakan pendekatan modular untuk memisahkan tanggung jawab antarkomponen.

- **Presentation Layer:** `main.py` mengelola antarmuka grafis dan alur interaksi pengguna menggunakan CustomTkinter.
- **API Client:** `src/api_client.py` menangani permintaan HTTP dan pengambilan data nilai tukar.
- **Conversion Engine:** `src/converter.py` menyediakan logika bisnis untuk menghitung hasil konversi.

Pemisahan ini dirancang untuk meningkatkan keterbacaan kode, kemudahan pengujian, dan pemeliharaan aplikasi.

> Catatan: Pada implementasi saat ini, perhitungan konversi masih dilakukan di `main.py`. Integrasi `CurrencyConverter` ke alur utama aplikasi merupakan bagian pengembangan berikutnya.

## Installation

### 1. Clone Repository

Ganti `<repository-url>` dengan URL repository GitHub yang sebenarnya.

```bash
git clone <repository-url>
cd convertet-money
```

### 2. Buat Virtual Environment

```bash
python -m venv .venv
```

### 3. Aktifkan Virtual Environment

**Windows — Command Prompt:**

```bat
.venv\Scripts\activate.bat
```

**Windows — PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source .venv/Scripts/activate
```

### 4. Instal Dependencies

```bash
python -m pip install -r requirements.txt
```

Perintah tersebut akan memasang seluruh library yang tercantum dalam `requirements.txt`.

### 5. Jalankan Aplikasi

```bash
python main.py
```

Pastikan Python sudah terpasang dan komputer memiliki koneksi internet untuk mengambil data nilai tukar dari API.

## API Reference

MoneyConvert menggunakan [Frankfurter API](https://frankfurter.dev/) sebagai sumber data nilai tukar.

### Endpoint Nilai Tukar

```http
GET https://api.frankfurter.dev/v2/rate/{base}/{quote}
```

Parameter:

| Parameter | Deskripsi | Contoh |
|---|---|---|
| `base` | Kode mata uang asal | `USD` |
| `quote` | Kode mata uang tujuan | `IDR` |

Contoh endpoint:

```http
GET https://api.frankfurter.dev/v2/rate/USD/IDR
```

Aplikasi membaca nilai kurs dari properti `rate` pada respons API dan menggunakannya untuk menghitung hasil konversi.

### Endpoint Daftar Mata Uang

```http
GET https://api.frankfurter.dev/v2/currencies
```

Endpoint ini digunakan oleh metode `get_currencies()` untuk mengambil data mata uang. Integrasinya dengan pilihan mata uang pada antarmuka masih dapat dikembangkan lebih lanjut.

Informasi endpoint dan format respons dapat dilihat pada dokumentasi resmi Frankfurter API.

## Documentation

Dokumentasi teknis tersedia di direktori `docs/`:

- [Arsitektur Sistem](docs/architecture.md)
- [Rencana Pengujian](docs/test-plan.md)

## Project Status

**Status: In Development**

MoneyConvert dikembangkan secara bertahap sebagai proyek pembelajaran dan portofolio untuk memperdalam pemahaman tentang Python, OOP, integrasi API, antarmuka grafis, dan praktik pengembangan perangkat lunak.

## License

Lisensi proyek belum ditentukan.

Penggunaan, modifikasi, dan distribusi ulang kode oleh pihak lain perlu mengikuti lisensi yang nantinya dipilih oleh pemilik proyek.
