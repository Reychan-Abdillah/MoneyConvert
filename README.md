# MoneyConvert

MoneyConvert adalah aplikasi desktop untuk mengonversi mata uang menggunakan nilai tukar dari [Frankfurter API](https://frankfurter.dev/). Aplikasi ini dibuat menggunakan Python dan CustomTkinter dengan antarmuka sederhana yang memudahkan pengguna memilih mata uang, memasukkan nominal, dan melihat hasil konversi.

Proyek ini dikembangkan sebagai sarana belajar Python sekaligus bagian dari portofolio pengembangan aplikasi.

## Fitur

- Konversi mata uang berdasarkan nilai tukar dari Frankfurter API.
- Pemilihan mata uang asal dan tujuan.
- Dropdown dengan fitur pencarian berdasarkan kode dan nama mata uang.
- Daftar mata uang yang diambil dari API, dengan batas maksimal 160 data.
- Validasi nominal agar nilai yang dikonversi lebih besar dari nol.
- Tampilan hasil konversi beserta nilai tukar.
- Penanganan kesalahan saat permintaan API gagal.

## Teknologi

- **Python** — bahasa pemrograman utama.
- **CustomTkinter** — membangun antarmuka desktop.
- **Requests** — mengirim permintaan HTTP ke API.
- **Frankfurter API** — menyediakan data nilai tukar dan daftar mata uang.
- **Git** — pengelolaan versi kode.

## Struktur Proyek

```text
convertet-money/
├── assets/
│   └── logoTeam.ico
├── docs/
│   ├── architecture.md
│   └── test-plan.md
├── src/
│   ├── api_client.py
│   ├── converter.py
│   ├── currency_list.py
│   └── searchable_dropdown.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Instalasi dan Menjalankan Aplikasi

Pastikan Python sudah terpasang di komputer. Klon repositori, lalu masuk ke direktori proyek.

```bash
git clone https://github.com/Reychan-Abdillah/MoneyConvert.git
cd MoneyConvert
```

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan virtual environment.

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source .venv/Scripts/activate
```

Pasang dependensi:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
python main.py
```

Pastikan komputer terhubung ke internet agar aplikasi dapat mengambil data nilai tukar dari API.

## Sumber Data API

MoneyConvert menggunakan Frankfurter API untuk mengambil nilai tukar dan daftar mata uang.

| Endpoint | Kegunaan |
|---|---|
| `GET /v2/rate/{base}/{quote}` | Mengambil nilai tukar antara dua mata uang. |
| `GET /v2/currencies` | Mengambil daftar mata uang yang tersedia. |

Base URL:

```text
https://api.frankfurter.dev/v2
```

Permintaan API menggunakan timeout 10 detik. Jika permintaan gagal, aplikasi akan menangani kesalahan dan menampilkan informasi pada antarmuka.

Informasi lebih lanjut tersedia di [dokumentasi Frankfurter API](https://frankfurter.dev/).

## Struktur Kode

- **`main.py`** — mengatur antarmuka, mengambil input pengguna, menjalankan konversi, dan menampilkan hasil.
- **`src/api_client.py`** — menangani permintaan ke Frankfurter API, termasuk pengambilan nilai tukar dan daftar mata uang.
- **`src/converter.py`** — menghitung hasil konversi berdasarkan nominal dan nilai tukar yang diperoleh dari API.
- **`src/currency_list.py`** — mengolah daftar mata uang dari API menjadi data kode dan nama yang digunakan aplikasi. Saat ini, maksimal 160 data pertama yang diproses.
- **`src/searchable_dropdown.py`** — menyediakan dropdown dengan fitur pencarian mata uang.
- **`assets/logoTeam.ico`** — ikon aplikasi.
- **`docs/architecture.md`** — dokumentasi arsitektur aplikasi.
- **`docs/test-plan.md`** — rencana pengujian manual.

## Pengujian

Pengujian dilakukan secara manual dengan menjalankan aplikasi dan memeriksa fungsi-fungsi utamanya, meliputi:

- Pengambilan nilai tukar dari API.
- Konversi nominal dan tampilan hasil.
- Pemilihan serta pencarian mata uang.
- Validasi input kosong, nol, atau negatif.
- Penanganan gangguan koneksi dan kegagalan permintaan API.

Rincian skenario pengujian tersedia di [`docs/test-plan.md`](docs/test-plan.md). Proyek ini belum menggunakan pengujian otomatis.

## Status Proyek

MoneyConvert sudah dapat menjalankan fungsi konversi mata uang. Pengembangan dan penyempurnaan antarmuka masih dapat dilanjutkan sesuai kebutuhan.

## Lisensi

MIT License

---

Dibuat sebagai proyek pembelajaran Python dan portofolio pengembangan aplikasi desktop.