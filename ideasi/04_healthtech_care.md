# 🩺 Subtema 04: HealthTech & Care (Inclusive Health & Well-being)

Subtema ini berfokus pada solusi aksesibilitas informasi kesehatan, pemantauan kesehatan mental, asistensi penyandang disabilitas, dan telemedicine komunitas yang inklusif.

> 📊 **Dokumen Riset & Analisis Data Terkini:** Baca analisis lengkap 4 krisis faskes inklusif di [ANALISIS_MASALAH_KESEHATAN_INKLUSIF.md](../research/ANALISIS_MASALAH_KESEHATAN_INKLUSIF.md).

---

## 📌 Masalah Lapangan & Peluang Solusi

### 1. Krisis Kesehatan Mental di Kalangan Mahasiswa & Pelajar
* **Masalah:** Tingginya tingkat stres akademik, kecemasan (*anxiety*), dan depresi pada generasi muda, namun terhambat stigma sosial, rasa takut bercerita, dan mahalnya biaya konsultasi psikolog profesional.
* **Ide Solusi (TemanCurhat AI - Empathetic First-Aid Mental Well-being Companion):**
  * Asisten interaktif berbasis teknik *Cognitive Behavioral Therapy (CBT)* yang menjadi tempat aman untuk meluapkan unek-unek, mendeteksi pola distorsi kognitif, dan menyediakan latihan mindfulness/pernapasan terpandu.
* **Fitur Kunci MVP:**
  * Jurnal emosi harian (*mood tracker*) dengan analisis tren pemicu stres mingguan.
  * Percakapan empati terarah yang tidak menghakimi (*guided self-reflection*).
  * Tombol darurat (*Emergency SOS SOS Hotline*) otomatis jika terdeteksi indikasi bahaya diri ke layanan pertolongan profesional atau konselor universitas.

---

### 2. Kelupaan Minum Obat Pasien Lansia & Penyakit Kronis (*Medication Adherence*)
* **Masalah:** Pasien hipertensi, diabetes, atau lansia sering lupa minum obat atau salah dosis, yang berisiko fatal terhadap kondisi kesehatan mereka. Keluarga sering kesulitan mengawasi kepatuhan minum obat dari jarak jauh.
* **Ide Solusi (CarePill - Smart Medication Companion & Caregiver Sync):**
  * Sistem pengingat jadwal minum obat cerdas yang terhubung langsung ke keluarga/pengasuh (*caregiver*) dengan sistem konfirmasi foto cepat atau notifikasi interaktif.
* **Fitur Kunci MVP:**
  * Scan resep atau kotak obat menggunakan kamera untuk input jadwal otomatis.
  * Pengingat audio bersuara ramah dan tombol "Sudah Minum".
  * Notifikasi peringatan ke WhatsApp anak/keluarga jika obat belum dikonfirmasi lewat dari 30 menit.

---

### 3. Keterlambatan Deteksi Stunting & Masalah Gizi Balita di Lingkup Posyandu
* **Masalah:** Pengukuran tinggi dan berat badan anak di Posyandu sering lambat dimasukkan ke sistem pusat, sehingga intervensi gizi buruk terlambat dilakukan oleh puskesmas setempat.
* **Ide Solusi (SiTumbuh - AI Stunting Early Detection & Nutrition Guide):**
  * Aplikasi pemantau kurva tumbuh kembang anak berbasis standar WHO dengan rekomendasi menu makanan padat gizi berbasis bahan pangan lokal yang murah dan mudah didapat.
* **Fitur Kunci MVP:**
  * Kalkulator z-score status gizi (tinggi menurut usia, berat menurut usia) instan.
  * Rekomendasi menu MPASI bernutrisi tinggi berbasis bahan lokal (misal: daun kelor, telur, tempe, ikan lele).
  * Dashboard rekapitulasi data anak untuk kader Posyandu/desa.

---

### 4. Keterbatasan Akses Layanan Pertolongan Pertama Medis Darurat (*First Responder*)
* **Masalah:** Waktu kedatangan ambulans di kota-kota padat sering memakan waktu lama (lebih dari 15–30 menit), sementara korban serangan jantung atau kecelakaan membutuhkan pertolongan pertama (CPR/pembidaian) dalam 5 menit emas (*Golden Period*).
* **Ide Solusi (ResQ-Citizen - Crowdsourced Volunteer First Responder Network):**
  * Platform yang menyiagakan sukarelawan terlatih P3K/CPR terdekat (dalam radius 500 meter) saat ada warga yang menekan tombol darurat medis, sembari ambulans resmi bergerak.
* **Fitur Kunci MVP:**
  * Tombol darurat satu sentuhan dengan transmisi lokasi GPS akurat.
  * Alert ke relawan medis bersertifikat terdekat.
  * Panduan visual langkah pertolongan pertama audio-visual di layar pemohon darurat.

---

## 🛠️ Rekomendasi Tech Stack untuk Hackathon
* **Frontend:** Mobile App (Flutter / React Native) atau Mobile-first Web App.
* **Backend:** Express.js / Django / Go dengan WebSockets untuk notifikasi real-time.
* **Privacy & Security:** Enkripsi data sensitif pengguna (kepatuhan UU Pelindungan Data Pribadi / UU PDP).
