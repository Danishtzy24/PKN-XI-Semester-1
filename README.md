# Pendidikan Pancasila — Kelas XI · Semester 1

Website materi & latihan Pendidikan Pancasila (Pancasila & UUD 1945) kelas XI, dibangun dengan Vite + TypeScript murni (tanpa framework), tema **merah bata**.

## Isi
- **6 bab · 34 topik**: Lima Sila · Penerapan & Konflik Nilai · Ideologi Negara · Proses Perubahan UUD 1945 · Periodisasi Konstitusi · TAP MPR & Tata Cara UUD
- Materi bab 4–6 disinkronkan dengan folder Drive sumber (2 PPT: *Bahan Tayangan (UUD45 & TAP)* + *Periodisasi Konstitusi di Indonesia*) — angka & tanggal mengikuti slide: tuntutan Reformasi, sidang MPR 1999—2002, struktur 16/37/49 → 21/73/170, lima periode konstitusi, TAP MPR No. I/MPR/2003 (139 TAP → 6 pasal), tata cara Pasal 91—94 & 7B.
- ⚠️ **Jangan regenerasi penuh** `src/content.ts` lewat `python3 tools/gen_content.py` — blok `E`/`META`/`summary`/`BD6` di generator masih memakai id bab lama (`s4-*`…`s6-*`). Konten bab 4–6 (id `k4-*`…`k6-*`) sudah tertulis langsung di `src/content.ts`; generator hanya jalan saat struktur JSON dan blok pengayaan generator diselaraskan ulang.
- Materi lengkap dengan chip istilah, kotak definisi, tabel rangkuman, catatan, jebakan soal, dan uji pemahaman
- **Latihan interaktif per bab** (soal pilihan ganda berpembahasan, diacak tiap sesi)
- **Uji Kemampuan**: 40 soal kisi-kisi (2,5 poin/soal, maks 100), diacak setiap mulai/ulang
- Lab visual interaktif di setiap topik

## Menjalankan
```bash
npm ci
npm run dev     # pengembangan
npm run build   # output ke dist/
```

Folder `siap-upload/` berisi hasil build siap hosting statis (Vercel/Netlify/GitHub Pages).
