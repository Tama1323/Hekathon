# 🎤 Strategi Pitching, Storytelling, & Panduan Q&A Juri LOGICODIX 2026

Dokumen ini memuat panduan komprehensif bagi Tim untuk menyusun presentasi (*pitch deck* 7 menit) dan mengantisipasi pertanyaan dewan juri pada babak seleksi dan Grand Final offline di Universitas Negeri Surabaya (UNESA).

---

## ⏱️ 1. Struktur Slide Presentasi 7 Menit (Winning Formula)

```text
[Menit 00:00 - 01:30] 🎬 SLIDE 1 & 2: The Hook & Empathetic Problem
- Buka dengan video/cerita 10 detik: Seorang tunanetra di Surabaya berjalan di trotoar, tongkatnya tidak menyentuh dahan pohon rendah, kepalanya terbentur.
- Data riil: 3.7+ juta tunanetra di Indonesia, 90% trotoar membahayakan, dan tongkat putih buta terhadap rintangan kepala dan got terbuka.

[Menit 01:30 - 03:00] 💡 SLIDE 3 & 4: Inovasi Solusi NetraNav AI
- Perkenalkan NetraNav AI: Bukan menggantikan tongkat putih, tapi menjadi "Mata Digital Kedua" di saku mereka.
- 4 Pilar MVP: Deteksi bahaya on-device <100ms, Pola Getaran Haptic anti-pusing, Navigasi khusus trotoar, dan Deteksi Jatuh SOS.

[Menit 03:00 - 04:30] 💻 SLIDE 5 & 6: Live Demo & Software Engineering
- Tunjukkan kamera HP langsung mendeteksi kotak rintangan di panggung juri dan memicu getaran serta suara peringatan seketika.
- Tekankan Edge AI on-device: Tidak perlu sinyal internet, hemat kuota (Green IT), dan 100% stabil di localhost.

[Menit 04:30 - 05:45] 💼 SLIDE 7: Business Model & Sustainability
- Paparkan model B2G (Smart City trotoar data) dan B2B (stasiun KAI & mall berdasar UU No. 8/2016).
- Pengguna tunanetra 100% GRATIS; monetize dari institusi yang berkewajiban secara regulasi.

[Menit 05:45 - 07:00] 🏆 SLIDE 8: Team & Vision Closing
- Paparkan kompetensi 4 anggota tim (Hustler, Hacker, Hipster, QA).
- Kalimat penutup yang menggugah nurani juri: "Teknologi terbaik bukan yang paling rumit, tetapi yang mampu mengembalikan rasa aman dan kemandirian bagi mereka yang tak dapat melihat dunia."
```

---

## 🎯 2. Pemetaan Pemenuhan 4 Pilar Rubrik Guidebook

| Pilar Penilaian Guidebook | Target Skor | Strategi Tim |
| :--- | :---: | :--- |
| **1. Problem-Solution Fit (25%)** | **Maksimal** | Membawa data riil 3.7 juta tunanetra & fakta kegagalan fisik tongkat putih terhadap rintangan kepala dan open manhole di Indonesia. |
| **2. Technology Innovation & AI (25%)** | **Maksimal** | Bukan sekadar membungkus API cloud yang lambat, melainkan mengimplementasikan **Edge AI Vision on-device (<100ms)** dan **Haptic Sensory Fusion**. |
| **3. Software Engineering (25%)** | **Maksimal** | Kode bersih, tanpa framework berlebih, arsitektur modular, dan mampu berjalan offline di `localhost` panggung UNESA tanpa crash. |
| **4. UI/UX & Ethics / Green IT (25%)** | **Maksimal** | Menggunakan standar WCAG 2.2 AA, audio non-overload, ramah TalkBack, dan privasi video terjamin (video tidak diunggah ke server cloud). |

---

## 🛡️ 3. Bank Jawaban Antisipasi Pertanyaan Juri (Tough Q&A Guide)

### ❓ Pertanyaan Juri 1:
> *"Aplikasi seperti Google Lookout dan Microsoft Seeing AI sudah ada. Kenapa harus bikin lagi?"*
* **Jawaban Jawara:**  
  > *"Terima kasih atas pertanyaannya, Dewan Juri yang terhormat. Google Lookout dan Seeing AI dirancang untuk kebutuhan **statis di dalam ruangan**—seperti membaca buku, scan barcode, dan mengenali uang. Ketika dipakai berjalan di trotoar Indonesia, aplikasinya memiliki **latensi jeda 2 hingga 4 detik**, yang mana sangat fatal karena pengguna sudah keburu jatuh ke dalam got. Selain itu, aplikasi luar negeri terus-menerus bicara di telinga, menyebabkan *audio overload* yang berbahaya bagi pendengaran tunanetra. NetraNav AI hadir menutup celah fatal tersebut: **on-device inference berkecepatan 50ms**, menggunakan **sinyal getar haptic yang intuitif**, dan dilatih mengenali rintangan khas Indonesia seperti lubang got terbuka dan dahan pohon rendah."*

---

### ❓ Pertanyaan Juri 2:
> *"Bagaimana jika baterai HP pengguna cepat habis karena kamera dan AI menyala terus?"*
* **Jawaban Jawara:**  
  > *"Kami menerapkan prinsip **Green IT & Adaptive Sampling Rate**. Saat sensor akselerometer mendeteksi pengguna sedang berdiri diam, kamera menurunkan frame rate ke 2 FPS untuk menghemat daya. Begitu sensor mendeteksi langkah kaki berjalan, model AI baru beralih ke 15–20 FPS aktif. Pendekatan ini menghemat konsumsi baterai hingga 60% dibanding continuous recording."*

---

### ❓ Pertanyaan Juri 3:
> *"Apakah ada isu privasi saat kamera pengguna merekam orang lain di jalanan umum?"*
* **Jawaban Jawara:**  
  > *"Sangat aman dan patuh terhadap **UU Perlindungan Data Pribadi (UU PDP)**. Pemrosesan Computer Vision terjadi **100% lokal di dalam memori smartphone (Edge AI)**. Tidak ada satu pun rekaman video atau foto yang dikirimkan ke server cloud kami. Frame video langsung dibuang dari memori RAM setelah bounding box rintangan dihitung."*

---

### ❓ Pertanyaan Juri 4:
> *"Target pengguna Anda disabilitas yang sering kali berekonomi rentan. Dari mana bisnis Anda bisa untung?"*
* **Jawaban Jawara:**  
  > *"Kami tidak pernah membebankan biaya langganan kepada teman tunanetra demi dampak sosial maksimal. Sumber pendapatan kami berbasis **B2G**—menjual data pemetaan trotoar rusak ke Dinas PUPR Smart City yang setiap tahun memiliki anggaran miliaran rupiah untuk rehabilitasi trotoar. Selain itu, kami menawarkan lisensi **B2B** pemetaan navigasi indoor untuk Stasiun KAI, Bandara, dan Rumah Sakit guna pemenuhan kewajiban **UU No. 8 Tahun 2016** dan peningkatan skor ESG korporasi."*
