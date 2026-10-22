# 🏛️ Subtema 05: Pelayanan Publik (Civic Tech & Community Service)

Subtema ini berfokus pada platform penghubung masyarakat dengan layanan publik, pelaporan fasilitas infrastruktur lingkungan, transparansi data, dan penguatan gotong royong digital warga.

---

## 📌 Masalah Lapangan & Peluang Solusi

### 1. Lambatnya Penanganan Masalah Fasilitas Lingkungan & Ketidakjelasan Status Laporan
* **Masalah:** Warga sering mengeluhkan jalan berlubang, lampu penerangan padam, tumpukan sampah liar, atau saluran mampet, namun bingung harus melapor ke mana, atau laporan sering "menggantung" tanpa kabar tindak lanjut.
* **Ide Solusi (LaporCepat Warga - Transparent Civic Issue Tracker):**
  * Platform pelaporan publik berbasis peta terbuka. Warga cukup memotret masalah (koordinat GPS dan waktu otomatis tersimpan); AI melakukan kategorisasi dinas terkait dan pengelompokan laporan ganda (*deduplication*).
* **Fitur Kunci MVP:**
  * Lapor dengan foto + auto-geotagging.
  * Status transparansi seperti tracking kurir belanja online (*Dilaporkan -> Diverifikasi -> Dikerjakan -> Selesai dengan Bukti Foto*).
  * Fitur *Upvote* warga lain: semakin banyak warga yang meng-upvote laporan yang sama, prioritas penanganan naik.

---

### 2. Rendahnya Partisipasi Warga dalam Musyawarah & Transparansi Iuran RT/RW
* **Masalah:** Pertemuan RT/RW tatap muka sering sepi karena warga sibuk bekerja, pembayaran iuran sampah/keamanan masih pakai kartu kertas manual, dan laporan pengeluaran kas lingkungan rawan dicurigai kurang transparan.
* **Ide Solusi (SmartRT - Digital Neighborhood Hub):**
  * Platform komunitas warga tingkat rukun tetangga untuk musyawarah digital, voting keputusan warga, transparansi kas masuk/keluar, dan broadcast pengumuman resmi.
* **Fitur Kunci MVP:**
  * E-Voting & Musyawarah Digital (survei keputusan warga dengan verifikasi 1 KK = 1 suara).
  * Buku Kas Transparan RT: grafik penerimaan iuran dan penggunaan dana kas secara terbuka.
  * Tombol Sirine Ronda / Tombol Darurat Keamanan Terpadu.

---

### 3. Kebingungan Akses Syarat Bantuan Sosial (Bansos) & Hoaks Informasi Publik
* **Masalah:** Warga miskin dan lansia sering tidak tahu apakah mereka memenuhi kriteria menerima bantuan program sosial pemerintah (PKH, KIP, BLT, BPJS PBI), dan sering menjadi korban penipuan/perantara liar yang meminta imbalan.
* **Ide Solusi (BansosNavigator - AI Civic Eligibility & Fact Guide):**
  * Asisten tanya-jawab hukum & bansos sederhana. Warga mengisi kuesioner singkat tanpa jargon hukum rumit, dan sistem menampilkan daftar program bantuan sosial yang berhak mereka ajukan beserta panduan langkah pengurusannya tanpa perantara.
* **Fitur Kunci MVP:**
  * Kuesioner kelayakan sosial ekonomi adaptif (*Eligibility Screener*).
  * Panduan berkas dokumen yang harus dibawa ke kantor kelurahan/desa.
  * Pengecek hoaks informasi bantuan pemerintah via integrasi fakta resmi.

---

### 4. Koordinasi Tanggap Bencana & Logistik Pengungsi Skala Komunitas
* **Masalah:** Saat terjadi bencana banjir atau gempa, distribusi logistik sering menumpuk di satu titik pengungsian, sementara titik lain kekurangan air bersih atau obat-obatan dasar.
* **Ide Solusi (BantuTanggap - Realtime Community Disaster & Relief Coordinator):**
  * Dashboard terbuka kebutuhan posko darurat bencana. Koordinator posko dapat memperbarui kebutuhan spesifik secara *real-time* (misal: butuh 50 selimut & popok bayi), sehingga donatur menyalurkan barang yang benar-benar dibutuhkan.
* **Fitur Kunci MVP:**
  * Peta posko pengungsian aktif dan persentase keterisian kapasitas.
  * Daftar kebutuhan mendesak (*Live Wishlist Logistik Posko*).
  * Verifikasi status donasi tersalurkan untuk menjaga akuntabilitas.

---

## 🛠️ Rekomendasi Tech Stack untuk Hackathon
* **Frontend:** Web responsif (React / Next.js) atau Mobile App (Flutter).
* **Mapping:** Leaflet.js / OpenStreetMap (ringan dan open-source).
* **Database & Realtime:** Supabase Realtime / PostgreSQL / Firebase Firestore.
