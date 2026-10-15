# 🌿 Subtema 02: Green IT & Climate (Green Environment & Sustainability)

Subtema ini berfokus pada teknologi hijau, pemantauan jejak lingkungan, mitigasi krisis iklim, efisiensi energi, dan pengelolaan sampah pintar (*smart waste management*).

---

## 📌 Masalah Lapangan & Peluang Solusi

### 1. Masalah *Food Waste* (Limbah Makanan) dari Restoran & Pasar Tradisional
* **Masalah:** Indonesia merupakan salah satu penghasil sampah makanan terbesar di dunia, sementara banyak masyarakat prasejahtera yang kekurangan asupan bergizi. Surplus makanan di resto/hotel/pasar sering langsung dibuang karena tidak ada jalur distribusi cepat sebelum kedaluwarsa.
* **Ide Solusi (SurplusFood Hub / FoodSaver P2P):**
  * Platform penghubung surplus makanan dari merchant (restoran, katering, toko roti, pasar) ke komunitas panti asuhan, bank makanan, peternak (pakan/maggot), atau pembeli diskon akhir hari.
* **Fitur Kunci MVP:**
  * Katalog makanan surplus waktu nyata (*flash sale countdown* / donasi gratis).
  * Geolocation map untuk penjemputan terdekat.
  * Pelacak dampak lingkungan (berapa kg makanan yang terselamatkan dan berapa kg emisi CO2 yang dicegah).

---

### 2. Kebingungan Pemilahan Sampah Rumah Tangga & Rendahnya Angka Daur Ulang
* **Masalah:** Masyarakat ingin mendaur ulang, namun sering tidak tahu apakah suatu barang termasuk sampah daur ulang, residu, atau B3. Bank sampah di sekitar lingkungan juga sulit ditemukan.
* **Ide Solusi (Smart EcoSnap - AI Waste Classifier & Bank Sampah Finder):**
  * Aplikasi Web/Mobile di mana warga cukup memotret sampah menggunakan kamera HP; AI Computer Vision mengenali jenis material (plastik PET, HDPE, kertas, kaleng) dan memberikan petunjuk cara penanganan serta nilai ekonomisnya.
* **Fitur Kunci MVP:**
  * Deteksi gambar sampah otomatis via AI (Computer Vision).
  * Peta direktori Bank Sampah & pengepul terdekat berserta estimasi harga jual/kg.
  * Sistem poin reward atau voucher ramah lingkungan untuk setiap aksi setor sampah terverifikasi.

---

### 3. *Carbon Footprint Awareness* untuk Generasi Muda & UMKM
* **Masalah:** Banyak orang dan bisnis kecil ingin menerapkan gaya hidup ramah lingkungan, namun tidak punya alat ukur sederhana untuk memantau konsumsi listrik, transportasi harian, dan sampah plastik.
* **Ide Solusi (GreenStep - Personal & Micro-Business Carbon Tracker):**
  * Pelacak jejak karbon harian dengan saran aksi nyata yang bisa langsung diterapkan untuk mereduksi pengeluaran energi dan biaya.
* **Fitur Kunci MVP:**
  * Kalkulator jejak karbon cepat (berdasarkan struk listrik, rute perjalanan, konsumsi mingguan).
  * AI Eco-Advisor: rekomendasi aksi harian yang menghemat uang sekaligus mengurangi emisi.
  * Lencana prestasi (*Green Badges*) dan kompetisi ramah lingkungan antar-kampus/komunitas.

---

### 4. Pemborosan Energi & Komputasi Berlebihan (*Green Software / Green Computing*)
* **Masalah:** Layanan digital dan server menghasilkan emisi karbon yang masif tanpa disadari oleh para pengembang dan pengelola sistem TI.
* **Ide Solusi (EcoCode / GreenWeb Audit):**
  * Tool audit performa situs web atau aplikasi yang menganalisis konsumsi data transfer dan estimasi emisi karbon per kunjungan laman, disertai rekomendasi kompresi aset dan optimasi kode.
* **Fitur Kunci MVP:**
  * Masukkan URL website -> Dapatkan skor efisiensi karbon (Gram CO2/Pageview).
  * Saran optimasi gambar, CSS/JS bloatware, dan caching efisien.

---

## 🛠️ Rekomendasi Tech Stack untuk Hackathon
* **Frontend:** Next.js / Vue / TailwindCSS.
* **AI & Vision:** TensorFlow.js / Google Gemini 1.5 Flash Vision API (analisis gambar sampah/makanan).
* **Maps & Geo:** Leaflet.js / Mapbox API / OpenStreetMap (gratis dan ringan).
