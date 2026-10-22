#!/usr/bin/env python3
"""
LOGICODIX 2026 — Real-Time Timeline & Interactive Task Tracker Auto-Updater
Generates a minimalist real-time SVG progress card and synchronizes the
interactive markdown checklist in README.md based on the official Guidebook.
"""

import os
import re
from datetime import datetime, timezone, timedelta

WIB = timezone(timedelta(hours=7))

# Competition Critical Dates
START_DATE = datetime(2026, 9, 15, 0, 0, 0, tzinfo=WIB)
SUBMISSION_DEADLINE = datetime(2026, 11, 14, 23, 59, 59, tzinfo=WIB)
GRAND_FINAL = datetime(2026, 11, 29, 8, 30, 0, tzinfo=WIB)

MILESTONES = [
    {"name": "Batch 1 Registration", "date": datetime(2026, 10, 6, 23, 59, 59, tzinfo=WIB), "type": "registration"},
    {"name": "Batch 2 Registration Deadline", "date": datetime(2026, 11, 6, 23, 59, 59, tzinfo=WIB), "type": "registration"},
    {"name": "Mentoring with Navasena", "date": datetime(2026, 11, 7, 9, 30, 0, tzinfo=WIB), "type": "mentoring"},
    {"name": "Hacking Week Kick-Off", "date": datetime(2026, 11, 7, 10, 0, 0, tzinfo=WIB), "type": "hacking"},
    {"name": "Last Submission (Freeze Repo)", "date": datetime(2026, 11, 14, 23, 59, 59, tzinfo=WIB), "type": "submission"},
    {"name": "Top 8 Finalists Announcement", "date": datetime(2026, 11, 21, 12, 0, 0, tzinfo=WIB), "type": "announcement"},
    {"name": "Technical Meeting Finalis", "date": datetime(2026, 11, 22, 10, 0, 0, tzinfo=WIB), "type": "tm"},
    {"name": "Grand Final Pitching & Awarding", "date": datetime(2026, 11, 29, 8, 30, 0, tzinfo=WIB), "type": "final"},
]

def get_current_wib():
    return datetime.now(WIB)

def generate_minimalist_svg(now, hacking_pct, overall_pct, next_m, days_to_deadline):
    bar_w = int(760 * (hacking_pct / 100))
    overall_bar_w = int(760 * (overall_pct / 100))

    if next_m:
        next_name = next_m["name"]
        diff_days = (next_m["date"].date() - now.date()).days
        if diff_days == 0:
            schedule_status = "Today"
        elif diff_days == 1:
            schedule_status = "Tomorrow"
        else:
            schedule_status = f"In {diff_days} days ({next_m['date'].strftime('%d %b')})"
    else:
        next_name = "Competition Concluded"
        schedule_status = "Finished"

    date_str = now.strftime("%A, %d %B %Y")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 230" width="100%" height="230">
  <defs>
    <style>
      @keyframes fillBar {{
        from {{ width: 0px; }}
        to {{ width: {bar_w}px; }}
      }}
      @keyframes fillOverall {{
        from {{ width: 0px; }}
        to {{ width: {overall_bar_w}px; }}
      }}
      .bar-fill {{
        animation: fillBar 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
    </style>
  </defs>

  <!-- Clean Minimalist Dark Background -->
  <rect x="0" y="0" width="840" height="230" rx="12" fill="#09090B" stroke="#27272A" stroke-width="1" />

  <!-- Header Section -->
  <g transform="translate(40, 34)">
    <text x="0" y="0" fill="#FAFAFA" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="600" letter-spacing="-0.3">LOGICODIX 2026</text>
    <text x="135" y="0" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="400">/ Hackathon (InklusiCare Team)</text>
    <text x="760" y="0" text-anchor="end" fill="#A1A1AA" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="400">{date_str}</text>
  </g>

  <!-- Divider Line -->
  <line x1="40" y1="52" x2="800" y2="52" stroke="#18181B" stroke-width="1" />

  <!-- Metrics Grid (3 Minimalist Columns) -->
  <g transform="translate(40, 84)">
    <!-- Col 1: Submission Deadline -->
    <text x="0" y="0" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" letter-spacing="0.5">SUBMISSION DEADLINE</text>
    <text x="0" y="24" fill="#FAFAFA" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="600">{days_to_deadline} Days Left</text>
    <text x="0" y="42" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Target: 14 Nov 2026 (23:59 WIB)</text>

    <!-- Col 2: Next Milestone -->
    <text x="270" y="0" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" letter-spacing="0.5">NEXT MILESTONE</text>
    <text x="270" y="24" fill="#FAFAFA" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="600">{next_name}</text>
    <text x="270" y="42" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Schedule: {schedule_status}</text>

    <!-- Col 3: Progress State -->
    <text x="560" y="0" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" letter-spacing="0.5">HACKATHON TIMELINE</text>
    <text x="560" y="24" fill="#FAFAFA" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="600">{hacking_pct:.1f}%</text>
    <text x="560" y="42" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12">Total Competition: {overall_pct:.1f}%</text>
  </g>

  <!-- Minimalist Progress Bar Track -->
  <g transform="translate(40, 166)">
    <rect x="0" y="0" width="760" height="4" rx="2" fill="#27272A" />
    <rect x="0" y="0" width="{bar_w}" height="4" rx="2" fill="#00CEC9" class="bar-fill" />
  </g>

  <g transform="translate(40, 192)">
    <text x="0" y="0" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">Kick Off (15 Sep)</text>
    <text x="760" y="0" text-anchor="end" fill="#71717A" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">Last Submission (14 Nov)</text>
  </g>
</svg>
"""
    return svg

def generate_interactive_checklist(now):
    """
    Native GitHub Task List format (- [ ] / - [x]).
    Users can interactively click and toggle these checkboxes directly on GitHub!
    """
    checklist = """### Interactive Task List (Click checkboxes directly on GitHub)

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
"""
    return checklist

def update_readme(now, hacking_pct, overall_pct, next_m, days_to_deadline):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    timestamp_v = int(now.timestamp())
    checklist_md = generate_interactive_checklist(now)

    tracker_section = f"""<!-- TIMELINE_TRACKER:START -->
## ⏱️ Real-Time Timeline & Interactive Task Tracker

![Competition Progress](assets/timeline_progress.svg?v={timestamp_v})

*Buka Dashboard Web Interaktif di [`tracker/index.html`](tracker/index.html) untuk melihat hitung mundur live detik-demi-detik dan simulator timer pitching.*

{checklist_md}
<!-- TIMELINE_TRACKER:END -->"""

    pattern = r"<!-- TIMELINE_TRACKER:START -->.*?<!-- TIMELINE_TRACKER:END -->"
    if re.search(pattern, content, flags=re.DOTALL):
        new_content = re.sub(pattern, tracker_section, content, flags=re.DOTALL)
    else:
        # Insert after "## 📌 Ringkasan Proyek" or before "## 📂 Peta & Struktur Repositori"
        if "## 📂 Peta & Struktur Repositori" in content:
            new_content = content.replace("## 📂 Peta & Struktur Repositori", tracker_section + "\n\n---\n\n## 📂 Peta & Struktur Repositori")
        else:
            new_content = content + "\n\n" + tracker_section

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README.md updated with minimalist SVG card & interactive checklist.")

def main():
    now = get_current_wib()

    hacking_total_sec = (SUBMISSION_DEADLINE - START_DATE).total_seconds()
    hacking_elapsed_sec = (now - START_DATE).total_seconds()
    hacking_pct = max(0.0, min(100.0, (hacking_elapsed_sec / hacking_total_sec) * 100))

    overall_total_sec = (GRAND_FINAL - START_DATE).total_seconds()
    overall_elapsed_sec = (now - START_DATE).total_seconds()
    overall_pct = max(0.0, min(100.0, (overall_elapsed_sec / overall_total_sec) * 100))

    days_to_deadline = max(0, (SUBMISSION_DEADLINE.date() - now.date()).days)
    upcoming = [m for m in MILESTONES if m["date"] >= now]
    next_m = upcoming[0] if upcoming else None

    os.makedirs("assets", exist_ok=True)

    svg_content = generate_minimalist_svg(now, hacking_pct, overall_pct, next_m, days_to_deadline)
    svg_path = os.path.join("assets", "timeline_progress.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Minimalist SVG card generated at {svg_path}")

    update_readme(now, hacking_pct, overall_pct, next_m, days_to_deadline)

if __name__ == "__main__":
    main()
