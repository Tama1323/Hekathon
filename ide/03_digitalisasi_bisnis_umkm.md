# 🏪 Subtema 03: Digitalisasi Bisnis (Local MSME & Creative Economy)

Subtema ini berfokus pada otomasi operasional bisnis mikro, perluasan akses pasar UMKM, kasir digital (*smart POS*), pencatatan keuangan, dan akselerasi ekonomi kreatif lokal.

---

## 📌 Masalah Lapangan & Peluang Solusi

### 1. Pembukuan Keuangan Manual & Manajemen Stok Warung yang Berantakan
* **Masalah:** Mayoritas pedagang kecil, warung sembako, dan pemilik gerai kuliner mencatat piutang dan stok di buku tulis lusuh, sering lupa menagih utang pelanggan (*bon*), dan sulit mengetahui laba/rugi bersih harian.
* **Ide Solusi (Voice-Assisted Micro POS & Buku Kas Pintar):**
  * Aplikasi kasir ultra-sederhana dengan integrasi input suara dan pemindaian struk (OCR). Pedagang cukup berbicara: *"Telur 2 kg, beras 5 kg, dibayar 100 ribu"* dan transaksi langsung tercatat rapi.
* **Fitur Kunci MVP:**
  * Voice-to-Transaction (input transaksi dengan suara bahasa Indonesia santai).
  * Manajemen utang (*buku kasbon*) dengan fitur kirim reminder tagihan WhatsApp otomatis satu klik.
  * Laporan laba/rugi harian dan status stok barang menipis (*low stock alert*).

---

### 2. UMKM Kesulitan Membuat Konten Pemasaran & Foto Produk yang Menarik
* **Masalah:** Pelaku UMKM lokal tidak memiliki keahlian desain grafis atau dana untuk menyewa fotografer profesional studio, sehingga postingan promosi di media sosial kurang memikat pembeli.
* **Ide Solusi (LokalKreatif - AI Studio & Marketing Generator untuk UMKM):**
  * Platform pembuatan aset promosi kilat. Pengguna cukup mengunggah foto produk biasa dengan latar belakang apa saja; AI akan menghapus background, menggantinya dengan studio estetik, dan membuatkan *copywriting* promosi serta hashtag sesuai target audiens.
* **Fitur Kunci MVP:**
  * Background remover otomatis & penempatan mockup produk profesional.
  * AI Copywriter dalam Bahasa Indonesia (pilihan tone: santai, profesional, promo diskon, edukatif).
  * Jadwal posting konten rekomendasi mingguan.

---

### 3. Pemborosan Stok & Kerusakan Bahan Baku Kuliner (*Dead Stock*)
* **Masalah:** Pemilik usaha kuliner sering bingung memperkirakan berapa banyak porsi bahan yang harus dibeli setiap hari, berujung pada bahan yang membusuk terbuang atau justru kehabisan bahan saat ramai.
* **Ide Solusi (PredikStok - Smart Demand & Supply Forecaster):**
  * Tool perkiraan kebutuhan bahan baku mingguan berbasis pola penjualan masa lalu, perkiraan cuaca lokal, dan siklus hari libur/gajian.
* **Fitur Kunci MVP:**
  * Rekomendasi belanja bahan harian dengan perhitungan estimasi biaya.
  * Peringatan kedaluwarsa bahan baku dalam inventaris.
  * Analisis menu paling menguntungkan (*menu engineering matrix*).

---

### 4. Sulitnya Akses Pembiayaan & Pinjaman Modal Usaha Akibat Minimnya Laporan Formal
* **Masalah:** Lembaga keuangan enggan memberikan pinjaman modal ke warung/UMKM mikro karena mereka tidak memiliki laporan keuangan terstandardisasi atau riwayat BI checking/SLIK.
* **Ide Solusi (FinScore Mikro - Alternative Financial Health Score):**
  * Platform yang mengolah ringkasan riwayat transaksi harian warung menjadi dokumen skor kesehatan finansial yang siap diajukan ke program KUR atau koperasi mitra.
* **Fitur Kunci MVP:**
  * Ekspor ringkasan arus kas format standar perbankan / akuntansi sederhana.
  * Indikator skor kelayakan kredit berbasis konsistensi arus kas (*Cash Flow Health Index*).

---

## 🛠️ Rekomendasi Tech Stack untuk Hackathon
* **Frontend:** PWA (Progressive Web App) dengan TailwindCSS agar ringan dibuka di HP spek rendah.
* **Voice & OCR:** Web Speech API (bawaan browser) + Tesseract.js / Cloud Vision API.
* **Database & Auth:** Supabase / Firebase (mudah, cepat di-setup, dan mendukung offline data sync).
