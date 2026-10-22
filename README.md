# 🚀 Logicodix 2026 — Hackathon Competition

<div align="center">

![Logicodix 2026](https://img.shields.io/badge/LOGICODIX-2026-6C5CE7?style=for-the-badge&logo=codeforces&logoColor=white)
![Status](https://img.shields.io/badge/Status-Ideation%20%26%20Research-00B894?style=for-the-badge)
![Category](https://img.shields.io/badge/Category-Hackathon%20MVP-0984E3?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Inclusive%20HealthTech-E17055?style=for-the-badge)

<br/>

> **"NextGen Digital Innovation: Crafting Creative Solutions for a Better Society"**  
> Repositori resmi riset, dokumentasi ideasi, arsitektur teknis, dan pengembangan Minimum Viable Product (MVP) Tim untuk ajang **LOGICODIX 2026** yang diselenggarakan oleh HIMTI / HMP TI Universitas Negeri Surabaya (UNESA).

</div>

---

## 📌 Ringkasan Proyek

Kompetisi ini berfokus pada pengembangan solusi digital inovatif berbasis **Web / Mobile (MVP)** yang menjawab permasalahan nyata masyarakat dengan integrasi **Artificial Intelligence (AI)** dan prinsip **Green IT & Aksesibilitas**.

* **Fokus Subtema Pilihan:** *Inclusive Health & Well-being* (Kesehatan Inklusif, Aksesibilitas Disabilitas & Mental Health)
* **Inovasi Produk:** **InklusiCare** — Platform integrasi fasilitas kesehatan ramah disabilitas, antrean sensorik (*silent queue token*), panduan suara disabilitas netra (TTS), dan pemetaan faskes inklusif.

---

<!-- TIMELINE_TRACKER:START -->
## ⏱️ Real-Time Timeline & Interactive Task Tracker

![Competition Progress](assets/timeline_progress.svg?v=1792653960)

*Buka Dashboard Web Interaktif di [`tracker/index.html`](tracker/index.html) untuk melihat hitung mundur live detik-demi-detik dan simulator timer pitching.*

### Interactive Task List (Click checkboxes directly on GitHub)

#### 1. Registrasi & Administrasi Tim (Batas: 06 November 2026, 23:59 WIB)
- [ ] Daftarkan akun tim InklusiCare di portal [logicodix2026.site/register](https://logicodix2026.site/register)
- [ ] Validasi data 4 anggota tim resmi: Tama1323 (Lead), Archygaze (Tech), relianxd (UI/UX), fundamantalist (AI/QA)
- [ ] Selesaikan pembayaran registrasi Batch 2 via QRIS resmi dan simpan bukti invoice/receipt
- [ ] Pastikan seluruh anggota tim bergabung ke grup WhatsApp resmi peserta lomba

#### 2. Sesi Mentoring Wajib Navasena (07 November 2026)
- [ ] Hadir tepat waktu pada sesi Daring Mentoring Navasena (Sabtu, 7 Nov 2026, 09.30 – 15.30 WIB)
- [ ] Konsultasikan arsitektur integrasi AI (Text-to-Speech & intent model) dengan mentor Navasena
- [ ] Validasi alur user experience dan pemenuhan standar aksesibilitas disabilitas
- [ ] Finalisasi spesifikasi fitur Minimum Viable Product (MVP) yang akan dibangun selama 7 hari

#### 3. Hacking Week — Pengembangan MVP InklusiCare (07 – 14 November 2026)
- [x] Inisialisasi struktur repositori GitHub dan `.gitignore` bersih (*Done*)
- [ ] **[Archygaze / Hacker]** Implementasi arsitektur sistem & integrasi backend/API MVP
- [ ] **[Archygaze / Hacker]** Bangun fitur **Silent Queue Token** (antrean visual sensorik ramah autisme & lansia)
- [ ] **[Archygaze / Hacker]** Bangun modul **Voice Guide / Text-to-Speech (TTS)** untuk disabilitas netra
- [ ] **[Archygaze / Hacker]** Integrasi peta fasilitas kesehatan ramah difabel (*Accessible Healthcare Mapping*)
- [ ] **[relianxd / Hipster]** Desain antarmuka berstandar **WCAG 2.2 AA** (rasio kontras 4.5:1, font disleksia, calming mode)
- [ ] **[relianxd / Hipster]** Audit navigasi keyboard & pembaca layar (*screen reader friendly*)
- [ ] **[fundamantalist / QA]** Validasi performa model AI & pengujian stabilitas anti-halusinasi data medis
- [ ] **[fundamantalist / QA]** Audit efisiensi Green IT & pengujian end-to-end tanpa bug kritis (*Zero Bug*)
- [ ] **[Tama1323 / Hustler]** Penyusunan slide presentasi (*pitch deck* 7 menit) berbasis data validasi Kemenkes

#### 4. Berkas Pengumpulan / Submission Wajib (Batas: 14 November 2026, 23:59 WIB)
- [ ] **[Wajib]** Rekam video demonstrasi aplikasi durasi **3 – 5 Menit** (murni demo fitur tanpa suara presentasi)
- [ ] Tampilkan integrasi Artificial Intelligence (AI) secara nyata pada rekaman video
- [ ] Unggah video ke YouTube (Unlisted/Public) atau Google Drive (akses publik)
- [ ] **[Wajib]** Freeze repositori GitHub sebelum 14 November 2026 pukul 23:59 WIB (kode dilarang diubah lagi)
- [ ] Submit tautan video demo & repositori ke formulir pengumpulan portal LOGICODIX 2026
- [ ] Konfirmasi pengumpulan ke narahubung panitia (Rohman: 08998713858 / Rivana: 083142142252)

#### 5. Persiapan Babak Final Luring (Top 8 Finalis — 29 November 2026)
- [ ] Pastikan aplikasi berjalan 100% stabil di environment **`localhost`** offline di depan juri
- [ ] Simulasi format waktu pitching ketat: 1 menit setup + 7 menit demo/pitch + 3 menit Q&A juri
- [ ] Siapkan laptop cadangan, converter HDMI, dan charger
- [ ] Hadir di Gedung Auditorium Utama UNESA Surabaya untuk Grand Final & Awarding

<!-- TIMELINE_TRACKER:END -->

---

## 📂 Peta & Struktur Repositori

```text
├── 📄 .gitignore                                     # Konfigurasi file pengabaian Git (Node, Python, OS, IDE)
├── 📄 README.md                                      # Dokumentasi utama & indeks repositori
│
├── 📁 docs/                                          # Dokumen & informasi resmi penyelenggara
│   ├── 📕 LOGICODIX-2026-Guidebook.pdf               # Buku panduan resmi lomba dari panitia
│   ├── 📄 hasil_scraping_logicodix_site.md           # Ekstraksi halaman web resmi kompetisi
│   └── 📄 hasil_scraping_logicodix_2026.md           # Informasi rilis & publikasi media sosial
│
├── 📁 tracker/                                       # Dashboard web interaktif real-time
│   └── 🌐 index.html                                 # Live countdown timers, checklist progress, & pitching simulator
│
├── 📁 management/                                    # Manajemen waktu, jadwal, & eksekusi tim
│   ├── 📋 TRACKER_DAN_TODO.md                        # Lembar kerja to-do & checklist kepatuhan guidebook
│   ├── 📄 TIMELINE_LOGICODIX_2026.md                 # Jadwal resmi & alokasi waktu kompetisi dari guidebook
│   └── 📄 TIMELINE_DAN_PEMBAGIAN_TUGAS.md            # Roadmap pengerjaan, Gantt chart, & peran anggota tim
│
├── 📁 research/                                      # Data validasi, benchmark juara, & rekam jejak
│   ├── 📄 ANALISIS_MASALAH_KESEHATAN_INKLUSIF.md     # Riset data validasi resmi (Kemenkes, SKI, Ombudsman)
│   ├── 📄 benchmark_ide.md                           # Analisis juara GEMASTIK, Imagine Cup, TreeHacks, dll.
│   └── 📁 track_record_juara/                        # Direktori bedah rekam jejak juara 2022–2025
│       ├── README.md                                 # Overview dan indeks riset historis
│       ├── 01_logicodix_2025.md                      # Analisis juara edisi 2025 (BPC & Web Dev)
│       ├── 02_logicodix_2024.md                      # Analisis edisi 2024 (Programming & Logic)
│       ├── 03_pre_logicodix_2023.md                  # Analisis juara UI/UX & inovasi digital (X-Project)
│       └── 04_analisis_pola_kemenangan_hackathon_2026.md # Formula kemenangan & strategi penilaian
│
├── 📁 ideasi/                                        # Direktori perumusan ide & subtema lomba
│   ├── 00_RINGKASAN_DAN_FRAMEWORK.md                 # Matriks komparasi & framework penilaian
│   ├── 01_edutech_ai_tutor.md                        # Subtema 1: Smart & Fun Education
│   ├── 02_green_it_climate.md                        # Subtema 2: Green Environment & Sustainability
│   ├── 03_digitalisasi_bisnis_umkm.md                # Subtema 3: Local MSME & Creative Economy
│   ├── 04_healthtech_care.md                         # Subtema 4: Inclusive Health & Well-being (Fokus Utama)
│   └── 05_pelayanan_publik_civic_tech.md             # Subtema 5: Civic Tech & Community Service
│
└── 📁 profile/                                       # Profil personal anggota tim
    └── 📄 GITHUB_PROFILE_README.md                   # Personal profile README Archygaze
```

---

## 👥 Tim & Pembagian Peran

| Anggota | GitHub Profile | Peran (*Role*) | Fokus Tanggung Jawab |
| :--- | :--- | :---: | :--- |
| **Tama1323** | [@Tama1323](https://github.com/Tama1323) | **Hustler (Lead)** | Validasi masalah sosial, perumusan narasi pitching, proposal, dan manajemen submission. |
| **Archygaze** | [@Archygaze](https://github.com/Archygaze) | **Hacker (Dev)** | Arsitektur teknis MVP, integrasi model AI/API, backend flow, dan pengujian performa sistem. |
| **relianxd** | [@relianxd](https://github.com/relianxd) | **Hipster (UI/UX)** | Desain inklusif standar WCAG 2.2 AA (kontras tinggi, ramah disleksia), prototyping, dan alur human-centered. |
| **fundamantalist** | [@fundamantalist](https://github.com/fundamantalist) | **AI & Data Specialist / QA** | Riset dataset kesehatan inklusif, validasi akurasi model AI, pengujian sistem (QA), dan penyusunan dokumentasi teknis. |

---

## ⏱️ Timeline & Jadwal Penting

| Tanggal | Agenda | Target Tim |
| :--- | :--- | :--- |
| **7 Sep – 6 Nov 2026** | Registrasi Batch 1 & 2 | Finalisasi pendaftaran & pembentukan tim. |
| **Sabtu, 7 Nov 2026** | Mentoring & Technical Meeting | Pembekalan teknis & pemetaan AI dari panitia. |
| **7 – 14 Nov 2026** | **Hacking Week (1 Minggu)** | Pengembangan MVP fungsional & integrasi AI. |
| **Sabtu, 14 Nov 2026** | **Last Submission** | Pengumpulan source code GitHub & Video Demo (3–5 menit). |
| **Sabtu, 21 Nov 2026** | Pengumuman Top 8 Finalis | Penilaian kurasi juri. |
| **Minggu, 29 Nov 2026** | **Grand Final & Seminar** | Live Pitching (15 menit per tim) & Demo di hadapan juri. |

* ⏱️ **Real-Time Web Dashboard:** Buka [`tracker/index.html`](tracker/index.html) di browser untuk melihat hitung mundur live, checklist to-do interaktif, dan simulator timer pitching 15 menit.
* 📋 **Worksheet Markdown To-Do:** Lembar kerja checklist to-do lengkap tersedia di [management/TRACKER_DAN_TODO.md](management/TRACKER_DAN_TODO.md).
* 📅 **Jadwal & Detail Pitching:** Rincian alokasi menit pitching tersedia di dokumen [management/TIMELINE_LOGICODIX_2026.md](management/TIMELINE_LOGICODIX_2026.md).

---

## 🎯 4 Pilar Penilaian Utama Juri (Berdasarkan Guidebook)

1. **Problem-Solution Fit (25%):** Ketajaman identifikasi masalah riil masyarakat dengan data resmi (bukan asumsi).
2. **Technology Innovation & AI (25%):** Pemanfaatan teknologi digital mutakhir dan integrasi AI yang aplikatif dan efisien.
3. **Software Engineering (25%):** Fungsionalitas MVP yang stabil saat live demo, arsitektur kode bersih, dan dokumentasi repositori rapi.
4. **UI/UX & Ethics (25%):** Desain inklusif yang ramah disabilitas (15%) dipadukan dengan prinsip *Green IT* & etika privasi data (10%).

---

## 🛠️ Tech Stack MVP (Planned)

* **Frontend:** HTML5 Semantic, Modern Vanilla CSS / Modern UI Component, JavaScript (ESNext).
* **Backend & API:** Lightweight REST API / Cloud Functions, Serverless integration.
* **AI & Machine Learning:** Open-source AI Models / Text-to-Speech (TTS) Web Speech API, Healthcare Intent Classification.
* **Aksesibilitas:** WCAG 2.2 AA Compliant, Screen Reader Friendly (ARIA), Dyslexia-Friendly Typography, High Contrast Theme.

---

<div align="center">
<b>Tim Logicodix 2026 • Crafted with passion for a better & more inclusive society</b>
</div>
