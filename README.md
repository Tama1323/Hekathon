# 🚀 Logicodix 2026 — InklusiCare Hackathon Repository

<div align="center">

![Logicodix 2026](https://img.shields.io/badge/LOGICODIX-2026-6C5CE7?style=for-the-badge&logo=codeforces&logoColor=white)
![Host](https://img.shields.io/badge/HIMTI-UNESA-0984E3?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Ideation%20%26%20Research-00B894?style=for-the-badge)
![Subtema](https://img.shields.io/badge/Focus-Inclusive%20HealthTech-E17055?style=for-the-badge)
![Standard](https://img.shields.io/badge/Accessibility-WCAG%202.2%20AA-2ED573?style=for-the-badge)

<br/>

> **"NextGen Digital Innovation: Crafting Creative Solutions for a Better Society"**  
> Repositori resmi riset, dokumentasi ideasi, arsitektur teknis, dan pengembangan Minimum Viable Product (MVP) Tim **InklusiCare** untuk ajang **LOGICODIX 2026** yang diselenggarakan oleh HMP TI / HIMTI Universitas Negeri Surabaya (UNESA).

</div>

---

## 📌 Ringkasan Proyek

Kompetisi **LOGICODIX 2026** menantang pengembang muda untuk menciptakan solusi digital berbasis **Web / Mobile (MVP)** yang menjawab krisis nyata masyarakat melalui pemanfaatan **Artificial Intelligence (AI)**, aksesibilitas inklusif, dan efisiensi **Green IT**.

* **Subtema Pilihan:** *Inclusive Health & Well-being* (Kesehatan Inklusif, Aksesibilitas Disabilitas & Mental Health)
* **Inovasi Produk:** **InklusiCare** — Platform integrasi layanan faskes ramah disabilitas pertama yang menggabungkan sistem antrean sensorik (*silent queue token*), panduan suara berbasis Speech AI untuk disabilitas netra, dan kurasi direktori fasilitas kesehatan ramah difabel.

---

## 🚨 Latar Belakang & Validasi Masalah (Problem-Solution Fit)

Berdasarkan analisis data sekunder resmi dari Kementerian Kesehatan RI (Kemenkes), Survei Kesehatan Indonesia (SKI), dan Ombudsman RI:

1. **Keterbatasan Faskes Inklusif:** Kurang dari 5% Puskesmas dan fasilitas pelayanan kesehatan primer di Indonesia yang memiliki infrastruktur fisik dan digital yang ramah penyandang disabilitas secara komprehensif.
2. **Kekurangan Aksesibilitas Antrean:** Panggilan antrean di klinik/rumah sakit masih mengandalkan pengeras suara (hambatan bagi teman Tuli) atau papan layar teks statis (hambatan bagi teman Netra).
3. **Krisis Sensorik di Ruang Tunggu:** Tingkat kebisingan dan kerumunan di ruang tunggu faskes kerap memicu *sensory overload* bagi pasien autisme, disabilitas sensorik, serta lansia berkebutuhan khusus.

---

## 💡 Fitur Kunci & Inovasi MVP InklusiCare

* 🎫 **Silent Queue Token (Antrean Ramah Sensorik):** Sistem nomor antrean digital langsung di browser ponsel pengguna dengan sinyal getar (haptic feedback) dan notifikasi visual kontras tinggi, menghilangkan kecemasan ruang tunggu.
* 🎙️ **AI Voice Guide (Speech-to-Text & Text-to-Speech):** Panduan suara interaktif berbasis Web Speech API dan Natural Language Processing untuk membantu pasien disabilitas netra memahami prosedur dan jadwal dokter tanpa bantuan pihak ketiga.
* 🗺️ **Accessible Healthcare Directory & Map:** Kurasi peta faskes terdekat yang dilengkapi informasi fasilitas ramah kursi roda, juru bahasa isyarat (JBI), dan poli khusus ramah sensorik.
* 🌿 **Green IT & Lightweight Architecture:** Kode tanpa framework berat, konsumsi memori minimal, emisi transfer data sangat rendah, dan dapat berjalan 100% offline di `localhost` saat penjurian luring.

---

## 📂 Peta & Struktur Repositori

```text
├── 📄 .gitignore                                     # Konfigurasi pengabaian Git (Node, Python, Cache, OS)
├── 📄 README.md                                      # Dokumentasi utama proyek & ringkasan kompetisi
│
├── 📁 docs/                                          # Dokumen & regulasi resmi panitia
│   ├── 📕 LOGICODIX-2026-Guidebook.pdf               # Buku panduan resmi kompetisi LOGICODIX 2026
│   ├── 📄 hasil_scraping_logicodix_site.md           # Ekstraksi informasi dari portal resmi kompetisi
│   └── 📄 hasil_scraping_logicodix_2026.md           # Rilis informasi media sosial & pengumuman
│
├── 📁 tracker/                                       # Command center interaktif tim
│   └── 🌐 index.html                                 # Dashboard web hitung mundur, checklist, & pitching timer
│
├── 📁 management/                                    # Perencanaan, jadwal, & eksekusi tim
│   ├── 📋 TRACKER_DAN_TODO.md                        # Lembar kerja to-do checklist kepatuhan guidebook
│   ├── 📄 TIMELINE_LOGICODIX_2026.md                 # Jadwal resmi & alokasi waktu kompetisi dari panitia
│   └── 📄 TIMELINE_DAN_PEMBAGIAN_TUGAS.md            # Roadmap pengerjaan, Gantt chart, & peran anggota tim
│
├── 📁 research/                                      # Data validasi masalah & benchmark juara
│   ├── 📄 ANALISIS_MASALAH_KESEHATAN_INKLUSIF.md     # Riset data validasi resmi (Kemenkes, SKI, Ombudsman)
│   ├── 📄 benchmark_ide.md                           # Analisis juara GEMASTIK, Imagine Cup, TreeHacks, dll.
│   └── 📁 track_record_juara/                        # Bedah rekam jejak juara edisi 2022–2025
│       ├── README.md                                 # Indeks riset historis juara
│       ├── 01_logicodix_2025.md                      # Analisis edisi 2025 (BPC & Web Dev)
│       ├── 02_logicodix_2024.md                      # Analisis edisi 2024 (Programming & Logic)
│       ├── 03_pre_logicodix_2023.md                  # Analisis edisi 2023 (UI/UX & X-Project)
│       └── 04_analisis_pola_kemenangan_hackathon_2026.md # Formula kemenangan & rubrik juri
│
└── 📁 ideasi/                                        # Matriks komparasi & evaluasi subtema lomba
    ├── 00_RINGKASAN_DAN_FRAMEWORK.md                 # Matriks komparasi 5 subtema & scoring
    ├── 01_edutech_ai_tutor.md                        # Subtema 1: Smart & Fun Education
    ├── 02_green_it_climate.md                        # Subtema 2: Green Environment & Sustainability
    ├── 03_digitalisasi_bisnis_umkm.md                # Subtema 3: Local MSME & Creative Economy
    ├── 04_healthtech_care.md                         # Subtema 4: Inclusive Health (Fokus Utama)
    └── 05_pelayanan_publik_civic_tech.md             # Subtema 5: Civic Tech & Community Service
```

---

## 👥 Tim & Pembagian Peran

| Anggota | GitHub Profile | Peran (*Role*) | Tanggung Jawab Utama |
| :--- | :--- | :---: | :--- |
| **Tama1323** | [@Tama1323](https://github.com/Tama1323) | **Hustler (Lead)** | Validasi masalah sosial, perumusan narasi pitching, proposal, dan manajemen submission. |
| **Archygaze** | [@Archygaze](https://github.com/Archygaze) | **Hacker (Dev)** | Arsitektur teknis MVP, integrasi model AI/API, backend flow, dan pengujian performa sistem. |
| **relianxd** | [@relianxd](https://github.com/relianxd) | **Hipster (UI/UX)** | Desain inklusif standar WCAG 2.2 AA (kontras tinggi, ramah disleksia), prototyping, dan alur human-centered. |
| **fundamantalist** | [@fundamantalist](https://github.com/fundamantalist) | **AI & QA Specialist** | Riset dataset kesehatan inklusif, validasi akurasi model AI, pengujian sistem (QA), dan dokumentasi teknis. |

---

## ⏱️ Timeline & Jadwal Penting Kompetisi

| Tanggal | Tahapan Agenda | Sasaran Capaian Tim |
| :--- | :--- | :--- |
| **7 Sep – 6 Nov 2026** | Pendaftaran Batch 1 & 2 | Finalisasi administrasi dan registrasi tim di portal lomba. |
| **Sabtu, 7 Nov 2026** | Mentoring & Technical Meeting | Sesi pembekalan online dengan mentor industri Navasena. |
| **7 – 14 Nov 2026** | **Hacking Week (7 Hari)** | Pengembangan MVP fungsional InklusiCare & integrasi AI. |
| **Sabtu, 14 Nov 2026** | **Last Submission (23:59 WIB)** | Freeze source code repositori GitHub & submit video demo 3–5 menit. |
| **Sabtu, 21 Nov 2026** | Pengumuman Top 8 Finalis | Pengumuman tim yang lolos ke babak Grand Final. |
| **Minggu, 29 Nov 2026** | **Grand Final & Seminar** | Live Demo offline di `localhost` & pitching 15 menit @ Auditorium UNESA. |

* *🛠️ Command Center Tim:* Buka [`tracker/index.html`](tracker/index.html) langsung di browser untuk melihat countdown live dan simulator timer presentasi.
* *📋 Checklist To-Do Lengkap:* Pantau rincian tugas setiap peran di [management/TRACKER_DAN_TODO.md](management/TRACKER_DAN_TODO.md).

---

## 🎯 4 Pilar Penilaian Utama Juri (Berdasarkan Guidebook)

1. **Problem-Solution Fit (25%):** Ketajaman identifikasi masalah riil masyarakat dengan data resmi (bukan asumsi).
2. **Technology Innovation & AI (25%):** Pemanfaatan teknologi digital mutakhir dan integrasi AI yang aplikatif dan efisien.
3. **Software Engineering (25%):** Fungsionalitas MVP yang stabil saat live demo, arsitektur kode bersih, dan dokumentasi repositori rapi.
4. **UI/UX & Ethics (25%):** Desain inklusif yang ramah disabilitas (15%) dipadukan dengan prinsip *Green IT* & etika privasi data (10%).

---

## 🛠️ Rencana Tech Stack MVP

* **Frontend:** Semantic HTML5, Modern Vanilla CSS (WCAG 2.2 AA tokens), Modern JavaScript (ESNext).
* **AI & Voice Engine:** Web Speech API (SpeechSynthesis & SpeechRecognition), Lightweight Natural Language Classifier.
* **Aksesibilitas:** ARIA Landmarks, Screen Reader Compatibility, Dyslexia Font Support, Calming Sensory Mode.
* **Lingkungan Demo:** 100% mandiri (*self-contained*), siap dijalankan langsung di lingkungan offline `localhost` juri.

---

<div align="center">
<b>Tim InklusiCare • LOGICODIX 2026 Universitas Negeri Surabaya</b><br/>
<i>Crafted with passion for a better, healthier, and more inclusive society</i>
</div>
