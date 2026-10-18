# Chatbot Akademik

Chatbot Akademik adalah aplikasi chatbot berbasis web yang dirancang untuk membantu mahasiswa mendapatkan informasi akademik secara lebih mudah dan interaktif. Chatbot ini menggunakan Natural Language Processing (NLP), Machine Learning, dan pendekatan Hybrid Rule-Based untuk mengenali maksud pertanyaan pengguna dan memberikan jawaban yang sesuai.

## Fitur Utama

- **Informasi akademik:** Menjawab pertanyaan terkait jadwal perkuliahan, UTS, UAS, persyaratan wisuda, pendaftaran wisuda, cuti kuliah, izin kuliah, dan poin Sispema.
- **Natural Language Processing (NLP):** Memproses teks pertanyaan sebelum dianalisis oleh model.
- **Hybrid Rule-Based dan Machine Learning:** Menggabungkan pencocokan aturan dengan prediksi model untuk mengenali intent pertanyaan.
- **Klasifikasi intent:** Menggunakan TF-IDF dan Logistic Regression untuk mengidentifikasi kategori pertanyaan.
- **Antarmuka web interaktif:** Menampilkan percakapan dalam bentuk gelembung chat antara pengguna dan chatbot.
- **Penanganan pertanyaan tidak dikenal:** Memberikan respons ketika sistem belum dapat mengenali maksud pertanyaan.

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| Flask | Framework untuk backend dan server web |
| Scikit-learn | Implementasi TF-IDF dan Logistic Regression |
| Sastrawi | Stemming dan pemrosesan teks bahasa Indonesia |
| Joblib | Menyimpan dan memuat model |
| HTML | Struktur halaman web |
| CSS | Tampilan antarmuka chatbot |
| JavaScript | Interaksi dan pengiriman pesan pada halaman chat |
| JSON | Menyimpan data intent, pola pertanyaan, dan respons |

## Metode yang Digunakan

### 1. Natural Language Processing (NLP)

NLP digunakan untuk membantu sistem memproses dan memahami teks pertanyaan pengguna. Tahap pemrosesan mencakup normalisasi teks dan stemming menggunakan Sastrawi.

### 2. TF-IDF

TF-IDF mengubah teks menjadi representasi numerik berdasarkan bobot kata sehingga dapat diproses oleh algoritma Machine Learning.

### 3. Logistic Regression

Logistic Regression digunakan untuk mengklasifikasikan pertanyaan ke dalam intent berdasarkan pola yang dipelajari dari data training.

### 4. Hybrid Rule-Based dan Machine Learning

Sistem memeriksa aturan atau kata kunci tertentu terlebih dahulu. Jika tidak ada aturan yang cocok, sistem menggunakan model Machine Learning untuk memprediksi intent pertanyaan.

## Alur Kerja Sistem

1. Pengguna memasukkan pertanyaan melalui website.
2. Backend Flask menerima pesan.
3. Sistem melakukan preprocessing terhadap teks.
4. Sistem memeriksa aturan berdasarkan kata kunci.
5. Jika tidak ada aturan yang cocok, teks diproses menggunakan TF-IDF dan diprediksi oleh Logistic Regression.
6. Sistem menentukan intent pertanyaan.
7. Jawaban yang sesuai diambil dari `intents.json`.
8. Jawaban ditampilkan kembali pada antarmuka chat.

## Struktur Folder

```text
chatbot_akademik/
├── data/
│   └── intents.json
├── model/
│   ├── chatbot_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── intent_tags.pkl
├── src/
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── main.py
├── train.py
├── requirements.txt
└── README.md
```

Keterangan:
- `data/intents.json`: Menyimpan kumpulan intent, pola pertanyaan, dan respons chatbot.
- `model/`: Menyimpan model Machine Learning dan komponen yang digunakan saat prediksi.
- `templates/index.html`: Menyimpan halaman utama chatbot.
- `static/style.css`: Mengatur tampilan halaman web.
- `main.py`: Menjalankan backend Flask dan logika chatbot.
- `train.py`: Melatih model menggunakan data intent.
- `requirements.txt`: Daftar library Python yang dibutuhkan.

## Persyaratan

Pastikan perangkat telah memiliki:
- Python 3.10 atau versi yang kompatibel dengan seluruh library yang digunakan.
- pip untuk menginstal library Python.
- Git (opsional, untuk mengambil repository).

## Instalasi dan Menjalankan Proyek

### 1. Clone repository

```bash
git clone https://github.com/ahmadalfnsyh/Project_Chatbot_Akademik.git
cd Project_Chatbot_Akademik
```

### 2. Buat virtual environment

Windows:

```powershell
python -m venv venv
```

Aktifkan virtual environment:

```powershell
venv\Scripts\activate
```

### 3. Instal library

```bash
python -m pip install -r requirements.txt
```

### 4. Latih model

```bash
python train.py
```

Tahap ini digunakan untuk melatih model berdasarkan data yang tersedia dan menyimpan hasilnya ke folder `model/`.

Jika model yang sudah tersedia ingin digunakan tanpa melatih ulang, pastikan file model yang dibutuhkan sudah ada dan sesuai dengan kode aplikasi.

### 5. Jalankan chatbot

```bash
python main.py
```

Buka browser dan akses:

```text
http://127.0.0.1:5000
```

Untuk menghentikan server, tekan `Ctrl + C` pada terminal.

## Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:
- Menambah variasi pertanyaan untuk setiap intent.
- Menambahkan normalisasi bahasa sehari-hari dan fitur koreksi typo.
- Meningkatkan akurasi melalui pengujian menggunakan pertanyaan baru.
- Memperbaiki penanganan pertanyaan yang belum dikenali.
- Menyempurnakan antarmuka agar lebih responsif.
- Menambahkan database untuk menyimpan riwayat percakapan jika diperlukan.
- Melakukan deployment agar chatbot dapat diakses secara online.

## Catatan

Chatbot ini masih dalam tahap pengembangan. Kemampuan mengenali pertanyaan bergantung pada kualitas data training, aturan yang tersedia, dan hasil prediksi model. Evaluasi menggunakan data pengujian belum tentu mencerminkan performa pada semua pertanyaan pengguna.

## Lisensi

Lisensi proyek belum ditentukan. Penggunaan atau distribusi ulang kode dapat diatur setelah lisensi proyek ditetapkan.
