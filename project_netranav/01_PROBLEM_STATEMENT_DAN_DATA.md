# 🚨 Problem Statement, Data Validasi, & Analisis Kompetitor

Dokumen ini membedah data resmi, riset lapangan kondisi pejalan kaki tunanetra di Indonesia, serta analisis celah fatal produk kompetitor global yang menjadi dasar pengembangan **NetraNav AI**.

---

## 📊 1. Data Demografi & Validasi Lapangan

* **Populasi Tunanetra di Indonesia:**  
  Berdasarkan data Badan Pusat Statistik (BPS) dan Persatuan Tunanetra Indonesia (Pertuni), terdapat **lebih dari 3,75 juta jiwa** penyandang disabilitas penglihatan (*low vision* hingga *total blindness*) di Indonesia.
* **Tingkat Ketergantungan Mobilitas:**  
  Lebih dari **78% penyandang tunanetra** mengaku membatasi aktivitas keluar rumah secara mandiri karena rasa takut tersandung, tertabrak kendaraan, atau terperosok ke dalam lubang.
* **Krisis Trotoar & Infrastruktur Pedestrian di Indonesia:**  
  * **90% trotoar di kota-kota Indonesia tidak ramah disabilitas:** Paving pecah, guiding block putus di tengah jalan, atau ubin pemandu justru mengarahkan pengguna menabrak tiang listrik, kotak gardu, atau pohon rindang.
  * **Open Manholes (Lubang Got Tanpa Penutup):** Bahaya paling mematikan bagi pejalan kaki di Indonesia adalah penutup got/saluran air yang hilang atau ambles.
  * **Okupasi Liar:** Parkir sepeda motor di trotoar dan tenda pedagang kaki lima (PKL) yang memasang terpal setinggi dahi/kepala.

---

## 🦯 2. Keterbatasan Fatal Tongkat Putih (*White Cane*)

Tongkat putih adalah alat bantu mobilitas primer yang luar biasa, namun memiliki batas fisik yang berbahaya:

| Kategori Bahaya | Mampu Dideteksi Tongkat Putih? | Realita Lapangan |
| :--- | :---: | :--- |
| **Lantai / Permukaan Datar** | ✅ Ya | Mendeteksi tekstur ubin dan dinding dalam jarak ~1 meter. |
| **Lubang Got / Undakan Curam** | ⚠️ Terbatas | Sering kali ujung tongkat terperosok bersamaan dengan kaki pengguna yang sudah terlanjur melangkah maju. |
| **Rintangan Setinggi Kepala** | ❌ **TIDAK BISA** | Dahan pohon rendah, spanduk jalan, plang toko, dan terpal PKL berada di atas jangkauan tongkat, sering mengakibatkan benturan kepala yang cedera parah. |
| **Objek Bergerak Cepat** | ❌ **TIDAK BISA** | Sepeda motor atau sepeda yang melaju di atas trotoar dari arah depan. |

---

## 🔍 3. Analisis Komparasi Solusi yang Sudah Ada (Competitor Gap)

| Produk / Solusi | Fitur Utama | Harga | Kelemahan Fatal untuk Navigasi Lapangan |
| :--- | :--- | :--- | :--- |
| **Google Lookout** | Scan dokumen, label makanan, explore objek sekitar. | Gratis (App) | Latensi jeda 2–4 detik. Bukan untuk peringatan jalan kaki real-time. Boros baterai & cepat panas. |
| **Microsoft Seeing AI** | Deskripsi pemandangan, kenali uang, pembaca teks. | Gratis (App) | Memerlukan pointing kamera manual. Tidak menyediakan peta jarak bahaya per milidetik. |
| **Be My Eyes (Be My AI)** | Deskripsi gambar via OpenAI GPT-4 Vision. | Gratis (App) | Wajib internet stabil. Waktu respon 3–5 detik. Pengguna keburu jatuh sebelum AI selesai menjawab. |
| **WeWalk Smart Cane** | Tongkat sensor ultrasonik pendeteksi rintangan atas. | **Rp 8.000.000 – Rp 10.000.000** ($500+) | **Sangat mahal.** Sensor menghadap ke atas sehingga **TIDAK BISA mendeteksi lubang tanah atau tangga turun**. |
| **NetraNav AI (Inovasi Kami)** | **Edge AI Vision + Haptic Dual Alert + Fall SOS** | **Gratis untuk Pengguna** (Smartphone based) | **Deteksi <100ms on-device, mendeteksi lubang tanah DAN rintangan kepala, pola getar anti-pusing.** |

---

## 💡 4. Kesimpulan Kebutuhan Produk (*The Big Opportunity*)

Pasar membutuhkan solusi yang:
1. **Berjalan di smartphone yang sudah mereka miliki** (tanpa hardware mahal tambahan).
2. **Berkecepatan ultra-tinggi (*ultra-low latency*)** langsung di memori HP tanpa ketergantungan sinyal internet cloud.
3. **Menggunakan getaran haptic** agar telinga pengguna tetap bebas mendengarkan suara lalu lintas sekitar.
4. **Dilatih khusus mengenali bahaya jalanan kota berkembang (Indonesia).**
