# 🔬 Riset Benchmarking Ide Juara GEMASTIK & Peluang Subtema LOGICODIX 2026

Dokumen ini membedah studi kasus dan karya-karya pemenang **GEMASTIK (Pagelaran Mahasiswa Nasional Bidang TIK)** terbaru (Edisi XVII 2024 & XVIII 2025) pada divisi *Software Development*, *UX Design*, dan *Smart City*, serta merumuskan **daftar ide aplikatif (*applicable product ideas*)** yang dapat diimplementasikan oleh tim untuk memenangkan ajang **LOGICODIX 2026**.

---

## 📊 Matriks Relevansi Karya Juara GEMASTIK terhadap Subtema Logicodix 2026

| Subtema Logicodix 2026 | Karya Referensi Juara GEMASTIK | Institusi & Edisi | Inti Inovasi Pemenang | Kesesuaian Kriteria |
| :--- | :--- | :--- | :--- | :--- |
| **1. Inclusive Health & Well-being (Fokus Utama)** | **TB Vector** *(Juara 1 SoftDev)*<br>**RawatKasih** *(Juara 1 UX)*<br>**DisaBisa** *(Medali Perunggu UX)*<br>**GluCare** *(Medali Perak UX)* | ITS (2025)<br>ITS (2025)<br>UB (2024)<br>UB (2024) | - Pemantauan akustik batuk TBC via AI.<br>- Asisten perawat lansia di panti wreda.<br>- Pelatihan & kerja inklusif 5 ragam disabilitas.<br>- Pengelolaan diabetes tipe 2 terintegrasi sensor. | Inovasi Kesehatan Inklusif, Aksesibilitas, dan Dukungan Masyarakat Rentan. |
| **2. Local MSME & Creative Economy** | **NaviGo** *(Juara 1 SoftDev)* | UI (2024) | Platform Web App AI advis hukum & kepatuhan legal terpadu bagi UMKM & konten kreator. | Efisiensi operasional & daya saing UMKM di era ekonomi kreatif. |
| **3. Smart & Fun Education** | **Snailly** *(Juara 2 SoftDev)* | UNIKOM (2025) | Aplikasi pemantau dan filter konten internet ramah anak yang edukatif dan interaktif. | Edukasi aman, interaktif, dan ramah pengguna muda. |
| **4. Green Environment & Sustainability** | **SEMARAK** *(Juara Harapan Smart City)*<br>**Envest** *(Circular Waste UX)* | Undip (2025)<br>Nasional (2024) | - Infrastruktur bertenaga surya & monitor polusi.<br>- Ekonomi sirkular sampah berbasis AI classifier. | Green IT, pengurangan jejak karbon, & pengelolaan sumber daya. |
| **5. Civic Tech & Community Service** | **AERION** *(Medali Perunggu Smart City)*<br>**CrowdEase** *(Best Paper Smart City)* | UPI (2025)<br>ITB (2025) | - Lampu lalu lintas adaptif prioritas ambulans.<br>- Deteksi kepadatan transportasi publik AI/IoT. | Layanan publik responsif & kenyamanan mobilitas warga. |

---

## 💡 Daftar Ide Aplikatif per Subtema (*Applicable Product Ideas*)

Berikut adalah ide-ide produk konkret yang dirumuskan dari pola kemenangan nasional, siap diadaptasi menjadi MVP Logicodix 2026:

### 🏥 Subtema 1: Inclusive Health & Well-being (Rekomendasi Utama Tim)

#### Ide 1.1: InklusiCare — Platform Faskes & Antrean Sensorik Ramah Disabilitas
* **Inspirasi Juara:** RawatKasih (ITS 2025) + DisaBisa (UB 2024).
* **Masalah Riil:** Kurang dari 5% Puskesmas di Indonesia ramah disabilitas; antrean fisik bersuara keras memicu *sensory overload* pada anak autis dan menyulitkan lansia/tunanetra.
* **Fitur Utama MVP:**
  1. **Silent Queue & Sensory Token:** Sistem tiket antrean digital hening tanpa pengeras suara, digantikan getaran smartphone atau lampu visual warna.
  2. **Voice & Screen-Reader Assistant:** Navigasi faskes terintegrasi Web Speech API (Text-to-Speech) untuk pasien tunanetra.
  3. **Visual Medical Triage:** Panduan visual isyarat medis sederhana untuk pasien tunarungu saat menjelaskan keluhan ke nakes.
  4. **Peta Aksesibilitas Faskes:** Direktori Puskesmas dengan fasilitas ramp kursi roda, toilet difabel, dan poli ramah jiwa.

#### Ide 1.2: JiwaTenang — Tele-Screening AI & Pendampingan Krisis Mental Health
* **Inspirasi Juara:** GluCare (UB 2024) + TB Vector (ITS 2025).
* **Masalah Riil:** 87.3% penderita depresi di Indonesia tidak mendapatkan pengobatan (*treatment gap*) dan tingginya stigma sosial.
* **Fitur Utama MVP:**
  1. **AI Mood & Journaling Sentiment:** Deteksi dini indikasi stres/depresi via analisis teks percakapan aman.
  2. **Rujukan Faskes Jiwa BPJS:** Rekomendasi psikolog Puskesmas terdekat yang menanggung BPJS Kesehatan.
  3. **Panic Button & Emergency Contact:** Tombol bantuan instan terhubung ke narahubung darurat/keluarga.

---

### 💼 Subtema 2: Local MSME & Creative Economy

#### Ide 2.1: LegalitasKilat AI — Asisten Kepatuhan Hukum & Izin Usaha UMKM
* **Inspirasi Juara:** NaviGo (UI 2024).
* **Masalah Riil:** Jutaan UMKM mikro kesulitan mengurus sertifikasi halal, NIB (Nomor Induk Berusaha), dan perlindungan HKI merek karena kendala biaya dan ketidaktahuan hukum.
* **Fitur Utama MVP:**
  1. **AI Legal Document Generator:** Pembuatan otomatis draf surat izin usaha, perjanjian kerja sederhana, dan pendaftaran merek.
  2. **Checklist Kesiapan Sertifikasi Halal:** Audit mandiri bertahap berbasis kuesioner cerdas.
  3. **Kalkulator Pajak & Biaya Legal Usaha:** Estimasi biaya transparan tanpa calo.

#### Ide 2.2: KriyaInklusi — Marketplace Kurasi Produk Karya Difabel
* **Inspirasi Juara:** DisaBisa (UB 2024).
* **Masalah Riil:** Perajin disabilitas memiliki keahlian kriya tinggi namun minim akses pemasaran digital dan logistik mandiri.
* **Fitur Utama MVP:**
  1. **Voice-Assisted Product Listing:** Penjual difabel netra dapat mendaftarkan barang dagangan via perintah suara.
  2. **Storytelling Commerce:** Menampilkan narasi perjuangan perajin untuk meningkatkan konversi pembeli.

---

### 🎓 Subtema 3: Smart & Fun Education

#### Ide 3.1: DifableLearn / EduAdapt — Tutor Adaptif Siswa Berkebutuhan Khusus
* **Inspirasi Juara:** Snailly (UNIKOM 2025) + CARBO AR.
* **Masalah Riil:** Keterbatasan guru pendamping khusus di sekolah inklusi reguler.
* **Fitur Utama MVP:**
  1. **Dyslexia-Friendly Mode:** Tipografi khusus (OpenDyslexic) dengan kontras warna yang menenangkan.
  2. **Speech-to-Visual Companion:** Mengubah instruksi guru menjadi visual animasi bagi siswa tunarungu.

---

### 🌿 Subtema 4: Green Environment & Sustainability

#### Ide 4.1: WasteSort AI — Klasifikasi Sampah Cerdas Berbasis Browser
* **Inspirasi Juara:** SEMARAK (Undip 2025) + Envest (2024).
* **Masalah Riil:** Rendahnya pemilahan sampah rumah tangga di Indonesia (<10%).
* **Fitur Utama MVP:**
  1. **In-Browser Vision AI (TensorFlow.js):** Pengguna mengarahkan kamera HP ke sampah, AI otomatis mengklasifikasikan (organik, anorganik, B3) tanpa perlu upload server (Green Computing).
  2. **Bank Sampah Integrator:** Menghitung poin rupiah dari sampah anorganik yang disetor ke bank sampah terdekat.

---

### 🏛️ Subtema 5: Civic Tech & Community Service

#### Ide 5.1: FasumRamah — Peta & Pelaporan Kerusakan Fasilitas Publik Ramah Difabel
* **Inspirasi Juara:** AERION (UPI 2025) + CrowdEase (ITB 2025).
* **Masalah Riil:** Jalur pemandu (*guiding block*) trotoar dan ramp kursi roda sering rusak atau tertutup pedagang kaki lima tanpa kanal pelaporan efektif.
* **Fitur Utama MVP:**
  1. **Crowdsourced Accessibility Mapping:** Warga memotret trotoar/faskes yang ramah atau rusak.
  2. **Vision AI Severity Check:** Menilai tingkat kerusakan otomatis dari foto sebelum diteruskan ke dashboard instansi terkait.

---

## 🏆 Sintesis: 4 Resep Utama Pemenang Hackathon

Dari keberhasilan tim-tim GEMASTIK dan LOGICODIX tahun-tahun sebelumnya, terdapat pola kemenangan yang wajib diadopsi:

1. **Problem-Solution Fit berbasis Data Resmi (Bukan Asumsi):**
   * Pemenang selalu membuka presentasi dengan data statistik resmi (Kemenkes, BPS, Ombudsman, SKI) yang membuktikan besarnya urgensi masalah.
2. **Kesiapan MVP & Live Demo Tanpa Kendala:**
   * Juri tidak menghargai mockup gambar semata; aplikasi harus bisa didemokan fungsional alur utamanya (*happy path*).
3. **Penerapan Prinsip Aksesibilitas (WCAG 2.2):**
   * Desain bukan cuma estetik, tapi mudah digunakan (*human-centered*), memiliki kontras ramah disabilitas, dan navigasi yang bersih.
4. **Efisiensi Sumber Daya & Etika AI (*Green IT*):**
   * Menjelaskan bagaimana pemrosesan data dilakukan secara efisien, privasi pengguna terlindungi, dan AI diterapkan secara etis serta transparan.
