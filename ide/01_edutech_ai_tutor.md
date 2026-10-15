# 🎓 Subtema 01: EduTech & AI Tutor (Smart & Fun Education)

Subtema ini berfokus pada pemanfaatan teknologi digital dan kecerdasan buatan (AI) untuk menciptakan pengalaman belajar yang menyenangkan, adaptif, interaktif, dan inklusif.

---

## 📌 Masalah Lapangan & Peluang Solusi

### 1. Fenomena "Jawaban Instan" AI Tanpa Nalar Kritis

* **Masalah:** Siswa dan mahasiswa sering memakai ChatGPT/AI hanya untuk menyalin jawaban tugas tanpa memahami alur berpikir logika (menurunkan daya analitis dan literasi kritis).
* **Ide Solusi (Socratic AI Tutor):**
  * Platform belajar di mana AI berperan sebagai **mentor Sokratik**: AI tidak memberikan jawaban langsung, melainkan memberikan pertanyaan pemandu, analogi interaktif, dan petunjuk langkah-demi-langkah hingga siswa menemukan solusi sendiri.
* **Fitur Kunci MVP:**
  * Mode dialog pemandu berpikir (guided step prompt).
  * Dashboard evaluasi nalar kritis siswa (memetakan bagian materi yang belum dipahami).
  * Generator latihan soal adaptif berdasarkan konsep yang paling lemah.

---

### 2. Kesenjangan Belajar & Gaya Belajar yang Berbeda (*Personalized Learning*)

* **Masalah:** Guru/dosen di kelas mengajar dengan satu kecepatan untuk 30–40 siswa, padahal kecepatan pemahaman masing-masing siswa berbeda. Siswa yang tertinggal merasa malu bertanya.
* **Ide Solusi (Adaptive Learning Path Generator):**
  * Aplikasi yang memecah topik materi rumit (misal: Aljabar, Fisika, Dasar Pemrograman) menjadi *micro-learning cards* dan kuis interaktif.
* **Fitur Kunci MVP:**
  * Diagnostic test kilat di awal untuk menentukan tingkat pemahaman awal.
  * AI yang otomatis menyesuaikan tingkat kesulitan latihan berdasarkan performa.
  * Ringkasan konsep dalam bentuk infografis atau analogi dunia nyata.

---

### 3. Rendahnya Minat Belajar Sains, Teknologi, Teknik & Matematika (STEM)

* **Masalah:** Materi sains dan matematika terasa abstrak, membosankan, dan teoritis tanpa visualisasi nyata.
* **Ide Solusi (Gamified Interactive Simulation Lab):**
  * Platform Web/Mobile berbasis simulasi mini-game interaktif (misalnya simulasi sirkuit listrik, reaksi kimia, gravitasi, atau visualisasi algoritma coding).
* **Fitur Kunci MVP:**
  * Simulator kanvas interaktif (drag-and-drop komponen).
  * Sistem quest, level, poin, dan leaderboard kelas.
  * Tantangan harian (*Daily Challenge*) dengan penjelasan logis di balik setiap simulasi.

---

### 4	. Keterbatasan Akses Media Belajar bagi Pelajar Berkebutuhan Khusus (Inklusivitas)

* **Masalah:** Materi pembelajaran digital di Indonesia sebagian besar belum ramah disleksia, tunanetra, atau tunarungu.
* **Ide Solusi (InkluBelajar - Inclusive Multimodal Learning):**
  * Aplikasi pembaca materi cerdas dengan mode multi-akses: font ramah disleksia (*OpenDyslexic*), Text-to-Speech ekspresif, ringkasan bahasa isyarat visual / animasi, dan penyederhanaan kalimat rumit.
* **Fitur Kunci MVP:**
  * Unggah dokumen PDF/modul sekolah -> otomatis dikonversi ke format audio ramah telinga dan visual berjarak lega.
  * Kuis interaktif dengan input suara untuk siswa dengan keterbatasan motorik.

---

## 🛠️ Rekomendasi Tech Stack untuk Hackathon

* **Frontend:** React / Next.js / Vue (Web) atau Flutter / React Native (Mobile).
* **Backend:** Node.js / FastAPI (Python) / Supabase.
* **AI API:** Google Gemini API / OpenAI API (dengan sistem *structured output* dan *system instructions* ketat).
