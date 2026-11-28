# -*- coding: utf-8 -*-
# Generator konten Pendidikan Pancasila XI -> src/content.ts (format Course shell).
# Materi dasar dari sumber (tools/pkn-chapters.json), diperkaya: chip istilah,
# kotak definisi, tabel rangkuman, catatan, jebakan soal, dan uji pemahaman.
import re, json, html as h

SRC_CH = json.load(open('tools/pkn-chapters.json', encoding='utf-8'))
SRC_Q  = json.load(open('tools/pkn-questions.json', encoding='utf-8'))

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', h.unescape(s)).strip().lower()

def section(sid, number, title, chips, lead, details):
    chips_text = ' '.join(chips)
    search = number + ' ' + title + ' ' + chips_text + ' ' + strip_tags(lead) + ' ' + ' '.join(strip_tags(d['title'] + ' ' + d['html']) for d in details)
    search = re.sub(r'\s+', ' ', search).strip()
    chips_html = '<div class="term-chips">' + ''.join('<span>' + x + '</span>' for x in chips) + '</div>'
    return {"id": sid, "number": number, "title": title, "lead": chips_html + lead.strip(), "details": details, "search": search}

def d(title, html):
    return {"title": title, "html": html.strip()}

CHIPS = lambda *t: tuple(t)
DEF  = lambda isi: '<div class="def-box"><b>PENGERTIAN</b>' + isi + '</div>'
TIP  = lambda isi: '<div class="tip-box"><b>CATATAN</b>' + isi + '</div>'
WARN = lambda isi: '<div class="warn-box"><b>JEBAKAN SOAL</b>' + isi + '</div>'
QUIZ = lambda isi, key: '<div class="mini-quiz"><b>UJI PEMAHAMAN</b>' + isi + '<p class="mq-key">' + key + '</p></div>'
TBL  = lambda head, rows: ('<div class="table-scroll"><table><thead><tr>' + ''.join('<th>' + x + '</th>' for x in head) +
        '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>')

def pg(qid, chapter, prompt, items, correct_idx, explanation):
    opts = []
    for i, txt in enumerate(items):
        letter = 'ABCD'[i]
        opts.append({"id": qid + '-' + letter, "html": "<p>" + txt + "</p>", "text": txt})
    return {"id": qid, "chapter": chapter, "prompt": "<p>" + prompt + "</p>", "options": opts,
            "correct": opts[correct_idx]["id"], "explanation": "<p>" + explanation + "</p>", "group": chapter}

# ============ Pengayaan per topik: blok ekstra yang dikurasi ============
E = {}
E['s1-1'] = [
 d("Makna dan kedudukan sila pertama", DEF("""
<p>Sila pertama menegaskan bahwa negara Indonesia <strong>berlandaskan kepercayaan terhadap Tuhan Yang Maha Esa</strong>. Kedudukannya sebagai <em>dasar</em> negara ditegaskan dalam <strong>Pembukaan UUD 1945 alinea pertama</strong>.</p>""") + """
<p>Wujud sila ini dalam kehidupan:</p>
<ul><li><strong>Kebebasan beribadah</strong> — setiap warga menjalankan ibadah menurut agamanya.</li><li><strong>Tidak memaksakan agama</strong> — keyakinan setiap orang dihormati.</li><li><strong>Kebebasan berkeyakinan</strong> — termasuk menjaga toleransi antarpemeluk agama.</li></ul>"""),
 d("Batas sila pertama", WARN("""
<p>Perhatikan dua penjebakan umum: <strong>(1)</strong> sila pertama <em>bukan</em> berarti negara berdasarkan agama tertentu — Indonesia bukan negara agama satu agama; <strong>(2)</strong> sila pertama <em>bukan</em> berarti negara mengabaikan agama (sekuler). Keduanya salah: negara <strong>berketuhanan</strong>, menjamin semua agama.</p>""")),
 d("Uji cepat", QUIZ("<p>Warga sekolah merayakan hari besar agamanya masing-masing tanpa saling mengganggu. Nilai sila berapa yang tampil?</p>", "Sila pertama — ketuhanan dan kebebasan berkeyakinan yang dihormati bersama."))]
E['s1-2'] = [
 d("Makna adil dan beradab", DEF("""
<p><strong>Adil</strong> berarti tidak diskriminatif — setiap manusia diperlakukan sesuai harkat dan martabatnya tanpa memandang latar belakang. <strong>Beradab</strong> berarti bertindak sesuai <strong>nilai budi pekerti</strong> atau kesopanan.</p>""") + """
<p>Contoh sikap sesuai sila kedua: perlakuan adil kepada teman baru, tidak membeda-bedakan pembagian tugas kelompok, dan membantu korban bencana tanpa memandang suku maupun agamanya.</p>"""),
 d("Jebakan makna adil", WARN("""
<p><strong>Adil bukan berarti semua orang diperlakukan persis sama.</strong> Keadilan memperhatikan kebutuhan — siswa yang kesulitan belajar justru memerlukan bimbingan lebih banyak. Pernyataan yang menyamakan adil dengan "diberi semuanya sama rata" adalah penjebakan.</p>"""))]
E['s1-3'] = [
 d("Semboyan Bhinneka Tunggal Ika", DEF("""
<p><strong>Bhinneka Tunggal Ika</strong> berasal dari Kitab Sutasoma karya <strong>Mpu Tantular</strong> dan berarti <em>berbeda-beda tetapi tetap satu</em>. Semboyan ini menjadi jangkar sila ketiga: persatuan di atas segala perbedaan.</p>""") + """
<p>Wujud sila ketiga: toleransi antarsuku dan bahasa, menjaga nama baik daerah kelahiran, serta memilih produk dalam negeri untuk memajukan ekonomi bersama.</p>"""),
 d("Persatuan bukan keseragaman", WARN("""
<p>Sila ketiga <strong>tidak menyuruh semua orang menjadi sama</strong>. Keberagaman suku, budaya, dan bahasa justru <em>dipelihara</em> di dalam kebersatuan. Pernyataan seperti "persatuan berarti menghapus perbedaan budaya" pasti salah.</p>"""))]
E['s1-4'] = [
 d("Langkah musyawarah mufakat", TBL(["Tahap", "Kegiatan"], [
  ["1", "Mengusulkan dan mengajukan masalah untuk didiskusikan"],
  ["2", "Setiap pihak menyampaikan pendapat secara teratur"],
  ["3", "Menimbang berbagai pendapat untuk mencari titik temu"],
  ["4", "Menetapkan keputusan bersama yang diterima semua pihak"]]) + """
<p>Keputusan musyawarah <strong>diliputi semangat kekeluargaan</strong> — tidak ada pihak yang dipaksa kalah. Contoh: musyawarah kelas memilih kegiatan, musyawarah RT mengatur kerja bakti, musyawarah organisasi menetapkan program.</p>"""),
 d("Musyawarah vs pemungutan suara", WARN("""
<p>Sila keempat mengutamakan <strong>mufakat</strong>. Pemungutan suara (voting) boleh menjadi jalan keluar bila mufakat sulit dicapai, tetapi pernyataan yang menganggap <em>musyawarah sama dengan voting</em> atau "keputusan mayoritas selalu menggantikan musyawarah" adalah jebakan — tujuannya tetap kesepakatan yang kekeluargaan.</p>"""))]
E['s1-5'] = [
 d("Sila kelima sebagai tujuan negara", TIP("""
<p>Dalam piramida Pancasila, sila kelima berkedudukan sebagai <strong>tujuan</strong>: seluruh pengamalan sila di bawahnya bermuara pada <strong>keadilan sosial bagi seluruh rakyat</strong> — kesejahteraan yang merata, bukan hanya milik kelompok tertentu.</p>""") + """
<p>Contoh perwujudannya: bantuan sosial bagi warga kurang mampu, kesempatan pendidikan yang sama untuk semua anak, dan lapangan kerja yang terbuka secara adil.</p>"""),
 d("Uji cepat", QUIZ("<p>Sekolah menyediakan beasiswa khusus bagi siswa berprestasi dari keluarga prasejahtera. Nilai sila mana yang ditunjukkan?</p>", "Sila kelima — keadilan sosial melalui perataan kesempatan pendidikan."))]
E['s1-6'] = [
 d("Posisi setiap sila di piramida", TBL(["Sila", "Posisi", "Perannya"], [
  ["Sila 1", "Dasar", "Landasan seluruh nilai — ketuhanan"],
  ["Sila 2", "Inti", "Penyumbang semangat — kemanusiaan"],
  ["Sila 3", "Prasyarat", "Syarat keutuhan — persatuan"],
  ["Sila 4", "Sarana", "Cara mencapai — musyawarah"],
  ["Sila 5", "Tujuan", "Hasil akhir — keadilan sosial"]]) + """
<p>Lima sila adalah <strong>satu kesatuan utuh</strong> yang saling menjiwai: mengamalkan satu sila berarti turut menjunjung sila lainnya. Piramida digambar dengan sila 1 di dasar dan sila 5 di puncak.</p>"""),
 d("Urutan piramida", WARN("""
<p>Ingat <strong>urutan</strong>: dasar piramida adalah <strong>sila pertama</strong>, puncaknya <strong>sila kelima</strong>. Pernyataan yang membalik urutan (misalnya "sila kelima sebagai dasar") atau menyebut piramida hanya terdiri atas tiga sila adalah jebakan soal klasik.</p>"""))]
E['s2-1'] = [
 d("Contoh penerapan di lingkaran terdekat", TBL(["Lingkungan", "Contoh tindakan", "Sila"], [
  ["Keluarga", "Beribadah bersama, musyawarah keputusan rumah tangga", "Sila 1 dan 4"],
  ["Masyarakat", "Gotong royong dan kerja bakti", "Sila 3"],
  ["Bertetangga", "Saling mengunjungi dan membantu tetangga sakit", "Sila 2"],
  ["Keprihatinan", "Membantu warga kurang mampu", "Sila 5"]]) + """
<p>Penerapan Pancasila <strong>tidak menunggu momen besar</strong> — dimulai dari tindakan kecil yang konsisten setiap hari, kemudian tumbuh ke lingkup sekolah dan masyarakat.</p>""")]
E['s2-2'] = [
 d("Menyelesaikan konflik nilai", TBL(["Langkah", "Penjelasan"], [
  ["1 · Identifikasi", "Tentukan masalah dan pihak yang terlibat"],
  ["2 · Menyampaikan", "Setiap pihak menyuarakan pendapat dengan sopan"],
  ["3 · Titik temu", "Cari persamaan yang dapat diterima semua pihak"],
  ["4 · Keputusan", "Tetapkan keputusan bersama yang diliputi kekeluargaan"]]) + """
<p>Contoh: dua kelompok tidak sepakat soal jadwal kegiatan — keduanya duduk bersama, menyampaikan alasan masing-masing, lalu menyepakati jadwal kompromi. Konflik selesai <strong>tanpa pemaksaan</strong>.</p>""")]
E['s2-3'] = [
 d("Wujud Pancasila di sekolah", TBL(["Kegiatan sekolah", "Sila yang ditunjukkan"], [
  ["Upacara bendera hari Senin", "Sila 3 — persatuan"],
  ["Belajar Pendidikan Pancasila", "Semua sila"],
  ["Menghargai guru dan teman", "Sila 2 — kemanusiaan"],
  ["Musyawarah kelas menentukan kegiatan", "Sila 4 — kerakyatan"],
  ["Tidak menang sendiri saat bertanding", "Sila 2 dan 4"],
  ["Kepala sekolah meneladan nilai", "Teladan penerapan Pancasila"]]))]
E['s2-4'] = [
 d("Memetakan tindakan ke sila", TBL(["Tindakan nyata", "Sila yang menjiwai"], [
  ["Membantu tetangga yang sakit", "Sila 2 (kemanusiaan) dan sila 5 (keadilan)"],
  ["Patuh pada peraturan sekolah", "Sila 4 (kerakyatan dan aturan bersama)"],
  ["Menjaga kebersihan lingkungan", "Sila 3 (persatuan — kepentingan bersama)"],
  ["Merayakan hari besar agama dengan hormat", "Sila 1 (ketuhanan)"]]) + """
<p>Perhatikan: satu tindakan dapat <strong>menjiwai lebih dari satu sila</strong>. Dalam soal, pilihlah jawaban yang menyebut <em>semua</em> sila yang relevan, bukan hanya salah satunya.</p>""")]
E['s2-5'] = [
 d("Tiga wajah keadilan sosial", TBL(["Jenis", "Wujudnya", "Contoh program"], [
  ["Ekonomi", "Pemerataan kesejahteraan", "Bantuan sosial dan beasiswa"],
  ["Politik", "Hak suara yang sama", "Pemilihan umum dan pemilihan kepala daerah"],
  ["Sosial-budaya", "Penghargaan terhadap semua kelompok", "Perlindungan hak kelompok minoritas"]]))]
E['s2-6'] = [
 d("Kriteria kebijakan berlandaskan Pancasila", TIP("""
<p>Sebuah kebijakan publik dinilai <strong>sesuai Pancasila</strong> apabila: menguntungkan <strong>seluruh rakyat</strong>, adil dan tidak diskriminatif, serta mendukung <strong>persatuan</strong>. Contoh: program bantuan yang menyasar keluarga prasejahtera, tata kota yang memperhatikan semua warga, dan kurikulum yang merata kualitasnya.</p>""")),
 d("Kebijakan yang belum sesuai", WARN("""
<p>Kebijakan yang <strong>hanya menguntungkan satu kelompok</strong> atau mengabaikan wilayah tertentu belum mencerminkan sila kelima. Soal sering menyodorkan contoh kebijakan semacam ini dan menanyakan sila mana yang <em>belum</em> terwujud — jawabannya keadilan sosial.</p>"""))]
E['s3-1'] = [
 d("Tiga sebutan, satu kedudukan", DEF("""
<p>Pancasila berkedudukan sebagai <strong>ideologi negara</strong> (sistem nilai dan pandangan hidup bangsa), <strong>falsafah negara</strong> (pikiran dasar mengatur kehidupan), dan <strong>dasar negara</strong> (fondasi penyelenggaraan negara). Kedudukan ini tertuang dalam <strong>Pembukaan UUD 1945 alinea keempat</strong>.</p>""") + """
<p>Karena itu Pancasila disebut <strong>dasar segala dasar negara</strong> dan menjadi <strong>sumber segala sumber hukum</strong> — seluruh peraturan di Indonesia tidak boleh bertentangan dengannya.</p>""")]
E['s3-2'] = [
 d("Yang tetap dan yang berkembang", TBL(["Aspek", "Keterangan"], [
  ["Nilai dasar (lima sila)", "Tetap — tidak dapat diubah"],
  ["Penjabaran dan pelaksanaan", "Berkembang mengikuti perkembangan zaman"],
  ["Relevansi", "Tetap menjadi pedoman dari masa ke masa"]]) + """
<p>Kemampuan menyesuaikan <em>penjabaran</em> tanpa mengubah <em>substansi</em> inilah yang membuat Pancasila disebut <strong>ideologi terbuka</strong>.</p>"""),
 d("Batas ideologi terbuka", WARN("""
<p><strong>Ideologi terbuka bukan berarti nilai dasarnya boleh diganti.</strong> Yang terbuka hanyalah cara mewujudkannya. Pernyataan seperti "karena terbuka, sila boleh direvisi sesuai zaman" adalah jebakan — lima sila tetap.</p>"""))]
E['s3-3'] = [
 d("Tiga dimensi Pancasila", TBL(["Dimensi", "Maknanya"], [
  ["Filosofis", "Nilai moral dan kearifan yang menjadi landasan berpikir"],
  ["Politis", "Dasar negara dan pedoman penyelenggaraan kebijakan"],
  ["Sosiologis", "Budaya hidup masyarakat — nilai yang dipraktikkan sehari-hari"]]))]
E['s3-4'] = [
 d("Tantangan dari dalam dan luar", TBL(["Jenis", "Contohnya"], [
  ["Internal", "Pemahaman hanya sebatas hafalan; tindak tanduk tidak sesuai nilai"],
  ["Eksternal", "Arus globalisasi; nilai asing yang bertentangan; gerakan yang menggugat Pancasila"]]) + """
<p>Cara menghadapinya: memperdalam <strong>pemahaman</strong>, lalu mewujudkannya dalam <strong>tindak tanduk nyata</strong> — bukan sekadar menghafal bunyi sila.</p>""")]
E['s3-5'] = [
 d("Pancasila di dunia digital dan kerja", TBL(["Lakukan", "Hindari"], [
  ["Menyebarkan informasi yang benar", "Menyebarkan hoaks dan ujaran kebencian"],
  ["Menghormati hak orang lain di media sosial", "Menyalin karya tanpa izin"],
  ["Menggunakan teknologi untuk kepentingan bersama", "Menyebar konten perusak nama baik bangsa"],
  ["Bekerja jujur dan disiplin", "Melanggar etika profesi"]]))]
E['s4-1'] = [
 d("Struktur UUD 1945", TBL(["Bagian", "Isi utamanya"], [
  ["Pembukaan", "Empat alinea; alinea keempat memuat Pancasila sebagai dasar negara"],
  ["Batang Tubuh", "Pasal-pasil: aturan kedudukan dan kekuasaan, hak dan kewajiban warga"],
  ["Penutup", "Ketentuan peralihan dan ketentuan tambahan"]]) + """
<p>Sebagai <strong>konstitusi tertinggi</strong>, UUD 1945 menjadi <strong>sumber hukum tertinggi</strong> — semua peraturan di bawahnya harus sesuai dengan UUD 1945 dan Pancasila.</p>"""),
 d("Alinea yang memuat Pancasila", WARN("""
<p>Pancasila tertuang dalam <strong>Pembukaan alinea keempat</strong>, bukan alinea pertama. Alinea <strong>pertama</strong> berisi pernyataan kemerdekaan dan landasan ketuhanan. Soal sering menukar nomor alinea — hafalkan: alinea 1 pernyataan kemerdekaan, alinea 4 Pancasila.</p>"""))]
E['s4-2'] = [
 d("UUDS 1950 dan sistem parlementer", TIP("""
<p>UUDS 1950 mengubah sistem pemerintahan dari <strong>presidensial</strong> menjadi <strong>parlementer</strong>: kekuasaan pemerintahan berada di tangan <strong>kabinet (perdana menteri)</strong>, sedangkan presiden lebih berperan sebagai kepala negara. Masa ini diwarnai banyak pergantian kabinet.</p>""")),
 d("Kedudukan presiden pada UUDS 1950", WARN("""
<p>Jangan terkecoh: pada masa UUDS 1950 <strong>presiden tetap ada</strong> sebagai kepala negara — hanya perannya yang tidak memegang pemerintahan sehari-hari. Pernyataan "presiden dibubarkan pada masa UUDS 1950" salah.</p>"""))]
E['s4-3'] = [
 d("Tiga poin Dekrit 5 Juli 1959", TBL(["Poin", "Isinya"], [
  ["1", "Mengukuhkan kembali UUD 1945"],
  ["2", "Menyambung (membubarkan) sidang Konstituante"],
  ["3", "Membentuk MPRS dan DPRGR"]]) + """
<p>Latar belakangnya: <strong>Konstituante gagal</strong> menyusun UUD baru, sehingga dekrit dilandasi keyakinan bahwa UUD 1945 dan Pancasila adalah sumber tertib hukum tertinggi yang tidak dapat ditawar.</p>""")]
E['s4-4'] = [
 d("Mekanisme amandemen", TBL(["Tahap", "Ketentuan"], [
  ["Usulan", "Dapat diajukan DPR, Presiden, atau MPRS"],
  ["Persetujuan", "Sidang DPR dengan hadir minimal dua per tiga anggota"],
  ["Pengesahan", "Setuju minimal dua per tiga dari anggota hadir"]]) + """
<p><strong>Amandemen</strong> berarti perubahan — UUD 1945 telah diamandemen <strong>empat kali (1999—2002)</strong> dengan mekanisme yang ketat.</p>"""),
 d("Yang tidak dapat diubah", WARN("""
<p>Beberapa hal <strong>tidak dapat diamandemen</strong>: sifat <strong>NKRI</strong>, sistem <strong>presidensial</strong>, serta <strong>Pembukaan UUD 1945</strong>. Soal sering menguji batas ini — pernyataan "Pembukaan UUD 1945 dapat diubah lewat amandemen" pasti salah.</p>"""))]
E['s4-5'] = [
 d("Bertindak sesuai konstitusi", TBL(["Tindakan warga", "Wujud konstitusi"], [
  ["Menggunakan hak pilih", "Berpartisipasi dalam pemilihan"],
  ["Menjaga persatuan", "Mengutamakan kepentingan bangsa"],
  ["Taat pada peraturan", "Menundukkan diri pada hukum"],
  ["Menyampaikan aspirasi", "Secara wajar dan sesuai prosedur"]]))]
E['s4-6'] = [
 d("Negara hukum", DEF("""
<p>Indonesia adalah <strong>negara hukum</strong>: hukum berlaku bagi <strong>semua orang</strong> — warga negara maupun pemerintah. Prinsip <em>supremasi hukum</em> berarti tidak ada pihak yang berada di atas hukum.</p>""") + """
<p>Prinsip ini <strong>melindungi hak warga</strong> sekaligus <strong>membatasi kesewenangan</strong> penguasa — keputusan pejabat pun harus berlandaskan aturan.</p>""")]
E['s5-1'] = [
 d("Perjalanan konstitusi 1945—1950", TBL(["Tahun", "Konstitusi", "Sistem"], [
  ["1945", "UUD 1945", "Presidensial"],
  ["1949—1950", "Konstitusi RIS", "Parlementer (negara serikat)"],
  ["1950", "UUDS 1950", "Parlementer (negara kesatuan)"]]))]
E['s5-2'] = [
 d("Masa Demokrasi Terpimpin", TIP("""
<p>Dekrit 5 Juli 1959 mengakhiri masa parlementer dan mengembalikan UUD 1945. Periode berikutnya (1959—1965) dikenal sebagai <strong>Demokrasi Terpimpin</strong>, lalu diakhiri periode transisi menuju Orde Baru.</p>"""))]
E['s5-3'] = [
 d("Isi empat amandemen", TBL(["Amandemen", "Tahun", "Inti perubahan"], [
  ["I", "1999", "Kewenangan MPR, hak asasi manusia, hak daerah, DPD"],
  ["II", "2000", "Hubungan pusat dan daerah, pemilihan gubernur"],
  ["III", "2001", "Tata kekuasaan dan lembaga negara"],
  ["IV", "2002", "Penataan ketentuan penyelenggaraan negara"]]) + """
<p>Keempat amandemen dilakukan <strong>secara bertahap dan damai</strong> — bukti bahwa UUD 1945 sebagai konstitusi dapat disesuaikan tanpa mengubah dasar negara.</p>""")]
E['s5-4'] = [
 d("Konstitusi di era digital", TIP("""
<p>Era digital membawa <strong>arus informasi lintas batas</strong>, <strong>kejahatan siber</strong>, dan tuntutan kebijakan yang berpihak pada rakyat. Konstitusi tetap menjadi <strong>tolok ukur</strong>: kebijakan dan perilaku digital warga dinilai benar apabila sesuai UUD 1945 dan Pancasila.</p>"""))]
E['s5-5'] = [
 d("Pelanggaran dan sanksi", TBL(["Contoh pelanggaran", "Akibatnya"], [
  ["Melecehkan simbol negara", "Diproses sesuai peraturan hukum"],
  ["Menyebarkan hasutan", "Diproses sesuai peraturan hukum"],
  ["Tindakan yang melecehkan SARA", "Diproses sesuai peraturan hukum"]]) + """
<p>Hukum bekerja <strong>membela nilai Pancasila</strong>: pelanggaran terhadap nilai dikenai sanksi sesuai aturan — bukan diselesaikan dengan balas dendam.</p>""")]
E['s5-6'] = [
 d("Menyikapi persoalan sosial", TBL(["Persoalan", "Pendekatan berlandaskan Pancasila"], [
  ["Kemiskinan dan kesenjangan", "Kebijakan yang berpihak pada keadilan sosial (sila 5)"],
  ["Perbedaan pendapat", "Musyawarah untuk mencapai mufakat (sila 4)"],
  ["Konflik antarkelompok", "Dialog dan penegakan hukum yang adil"]]))]
E['s6-1'] = [
 d("Sumber segala sumber hukum", DEF("""
<p><strong>Pancasila adalah sumber segala sumber hukum negara</strong>. Kedudukan ini tertuang dalam Pembukaan UUD 1945 alinea keempat. Karena <strong>Pembukaan tidak dapat diubah</strong>, kedudukan Pancasila sebagai dasar negara juga <strong>tidak tergantikan</strong>.</p>""") + """
<p>Akibatnya: seluruh peraturan perundang-undangan — dari UU sampai peraturan daerah — <strong>wajib tidak bertentangan</strong> dengan Pancasila.</p>"""),
 d("Uji cepat", QUIZ("<p>Mengapa kedudukan Pancasila tidak dapat digantikan oleh peraturan baru?</p>", "Karena Pancasila tertuang dalam Pembukaan UUD 1945 yang tidak dapat diubah."))]
E['s6-2'] = [
 d("Hubungan yang saling menunjang", TBL(["Aspek", "Pancasila", "UUD 1945"], [
  ["Kedudukan", "Jiwa dan dasar konstitusi", "Penjabaran Pancasila dalam aturan hukum tertinggi"],
  ["Fungsi", "Sumber nilai dan sumber hukum", "Pedoman penyelenggaraan negara"],
  ["Sifat", "Tidak tergantikan", "Dapat diamandemen (kecuali Pembukaan)"]]) + """
<p>Apapun peraturan yang <strong>bertentangan dengan Pancasila dan UUD 1945</strong> dinyatakan tidak berlaku — inilah bentuk keterikatan seluruh hukum pada dasar negara.</p>"""),
 d("Arah hubungan", WARN("""
<p>Jangan membalik arah hubungan: <strong>UUD menjabarkan Pancasila</strong>, bukan sebaliknya. Pernyataan seperti "Pancasila diturunkan dari UUD 1945" adalah jebakan — Pancasila justru menjadi dasarnya.</p>"""))]
E['s6-3'] = [
 d("Lima langkah mengerjakan soal kompleks", TBL(["Langkah", "Yang dilakukan"], [
  ["1", "Baca soal, identifikasi konteks permasalahan"],
  ["2", "Tentukan sila atau aspek yang diujikan"],
  ["3", "Kaji hubungan sebab-akibat"],
  ["4", "Jawab dengan merujuk pada nilai Pancasila dan konstitusi"],
  ["5", "Periksa konsistensi jawaban dengan bunyi sila"]]) + """
<p>Soal nomor 31—40 berupa <strong>kasus kontekstual</strong>: sebuah peristiwa dipetakan ke sila, aspek keadilan, atau hubungan Pancasila—konstitusi. Kuncinya <em>pahami nilainya, bukan hafal nomornya</em>.</p>""")]

# ============ Membangun sections terenrichment ============
CHIPS_MAP = {
 's1-1': CHIPS("Ketuhanan", "Kebebasan beribadah", "Toleransi"),
 's1-2': CHIPS("Harkat martabat", "Adil", "Beradab"),
 's1-3': CHIPS("Persatuan", "Bhinneka Tunggal Ika", "Keberagaman"),
 's1-4': CHIPS("Musyawarah", "Mufakat", "Kekeluargaan"),
 's1-5': CHIPS("Keadilan sosial", "Kesejahteraan", "Pemerataan"),
 's1-6': CHIPS("Piramida", "Kesatuan sila", "Saling menjiwai"),
 's2-1': CHIPS("Keluarga", "Gotong royong", "Tindakan kecil"),
 's2-2': CHIPS("Konflik nilai", "Titik temu", "Keputusan bersama"),
 's2-3': CHIPS("Upacara", "Budaya sekolah", "Teladan"),
 's2-4': CHIPS("Pemetaan sila", "Tindakan nyata", "Konteks"),
 's2-5': CHIPS("Ekonomi", "Politik", "Sosial-budaya"),
 's2-6': CHIPS("Kebijakan publik", "Kriteria", "Kepentingan bersama"),
 's3-1': CHIPS("Ideologi", "Falsafah", "Dasar negara"),
 's3-2': CHIPS("Ideologi terbuka", "Nilai dasar", "Penjabaran"),
 's3-3': CHIPS("Filosofis", "Politis", "Sosiologis"),
 's3-4': CHIPS("Tantangan", "Globalisasi", "Tindak tanduk"),
 's3-5': CHIPS("Hoaks", "Media sosial", "Tanggung jawab"),
 's4-1': CHIPS("Pembukaan", "Batang Tubuh", "Hukum tertinggi"),
 's4-2': CHIPS("UUDS 1950", "Parlementer", "Kabinet"),
 's4-3': CHIPS("Dekrit", "5 Juli 1959", "MPRS"),
 's4-4': CHIPS("Amandemen", "Dua per tiga", "Batas perubahan"),
 's4-5': CHIPS("Hak pilih", "Kewajiban", "Aspirasi"),
 's4-6': CHIPS("Negara hukum", "Supremasi", "Kesewenangan"),
 's5-1': CHIPS("1945", "RIS", "UUDS 1950"),
 's5-2': CHIPS("1959—1966", "Demokrasi Terpimpin", "Transisi"),
 's5-3': CHIPS("Empat amandemen", "1999—2002", "Tata kekuasaan"),
 's5-4': CHIPS("Era digital", "Kejahatan siber", "Tolok ukur"),
 's5-5': CHIPS("Pelanggaran", "Sanksi", "Simbol negara"),
 's5-6': CHIPS("Persoalan sosial", "Kebijakan", "Keadilan"),
 's6-1': CHIPS("Sumber hukum", "Pembukaan", "Hierarki"),
 's6-2': CHIPS("Jiwa konstitusi", "Penjabaran", "Tidak berlaku"),
 's6-3': CHIPS("Strategi", "Kontekstual", "Sebab-akibat"),
}
FIX_LEAD = [
 ('berkekeyakinan', 'berkeyakinan'),
 ('musyawarah mufakat , bukan', 'musyawarah mufakat, bukan'),
 ('konstitusi onal', 'konstitusional'),
 ('presidensial dan peran konstituante', 'presidensial dan peran Konstituante'),
]
def clean_lead(x):
    for a, b in FIX_LEAD: x = x.replace(a, b)
    return x

all_sections = {}
new_chapters = []
for c in SRC_CH:
    secs = []
    for s in c['sections']:
        base_detail = s['details'][0] if s['details'] else {"title": "Poin utama", "html": "<p>" + strip_tags(s['lead']) + "</p>"}
        title1 = base_detail['title'] if base_detail['title'] else "Poin utama"
        details = [d(title1, base_detail['html'])] + E.get(s['id'], [])
        lead = clean_lead(s['lead'])
        secs.append(section(s['id'], s['number'], s['title'], CHIPS_MAP.get(s['id'], ()), lead, details))
        all_sections[s['id']] = secs[-1]
    new_chapters.append({"src": c, "sections": secs})

# ============ Soal ============
FIX_EXPL = [('konstitusi onal', 'konstitusional')]
questions = []
for q0 in SRC_Q:
    opts = []
    for o in q0['options']:
        t = o['text'].strip()
        opts.append({"id": o['id'], "html": "<p>" + t + "</p>", "text": t})
    expl = q0['explanation'].strip()
    for a, b in FIX_EXPL: expl = expl.replace(a, b)
    prompt = q0['prompt'].strip()
    if not prompt.startswith('<'): prompt = '<p>' + prompt + '</p>'
    questions.append({"id": q0['id'], "chapter": q0['chapter'], "prompt": prompt, "options": opts,
                      "correct": q0['correct'], "explanation": "<p>" + expl + "</p>", "group": q0['chapter']})
# Tambahan soal latihan bab 6 (tidak masuk bank Uji Kemampuan)
questions += [
 pg("BD6-01", 6, "Peraturan perundang-undangan yang bertentangan dengan Pancasila dan UUD 1945 akan…",
    ["Dibatalkan dan tidak berlaku", "Diberlakukan sampai ada penggantinya", "Diubah menjadi peraturan daerah", "Ditunda pelaksanaannya tanpa batas waktu"], 0,
    "Karena Pancasila sumber segala sumber hukum, setiap peraturan yang bertentangan dengan Pancasila dan UUD 1945 dinyatakan tidak berlaku."),
 pg("BD6-02", 6, "Kedudukan Pancasila terhadap seluruh peraturan perundang-undangan di Indonesia adalah sebagai…",
    ["Pelengkap peraturan", "Sumber segala sumber hukum", "Sumber hukum sekunder", "Pengganti peraturan tertulis"], 1,
    "Pancasila tertuang dalam Pembukaan UUD 1945 alinea keempat dan menjadi sumber segala sumber hukum negara."),
 pg("BD6-03", 6, "Karena Pembukaan UUD 1945 tidak dapat diubah, maka…",
    ["Seluruh UUD tidak dapat diubah sama sekali", "Kedudukan Pancasila sebagai dasar negara tidak tergantikan", "Musyawarah tidak diperlukan lagi", "Amandemen tidak pernah dilakukan"], 1,
    "Pancasila tertuang dalam Pembukaan yang tidak dapat diubah, sehingga kedudukannya sebagai dasar negara tidak tergantikan — walaupun batang tubuh UUD tetap dapat diamandemen."),
]

# ============ Metadata bab ============
META = {
 1: {"fullTitle": "Lima Sila Pancasila", "subtitle": "Makna sila · piramida nilai · hubungan antarsila",
     "example": "Ketuhanan · Kemanusiaan · Persatuan · Kerakyatan · Keadilan",
     "translation": "Lima sila sebagai satu kesatuan nilai — dasar (sila 1) hingga tujuan (sila 5)."},
 2: {"fullTitle": "Penerapan & Konflik Nilai", "subtitle": "Keluarga · masyarakat · sekolah · kebijakan publik",
     "example": "Membantu tetangga yang sakit menjiwai sila 2 dan sila 5.",
     "translation": "Satu tindakan nyata dapat mencerminkan lebih dari satu sila sekaligus."},
 3: {"fullTitle": "Pancasila sebagai Ideologi Negara", "subtitle": "Ideologi terbuka · dimensi · tantangan · era digital",
     "example": "Nilai dasar lima sila tetap; penjabarannya berkembang mengikuti zaman.",
     "translation": "Inti ideologi terbuka: substansi terkunci, pelaksanaan menyesuaikan zaman."},
 4: {"fullTitle": "UUD 1945 & Konstitusi", "subtitle": "Kedudukan · UUDS 1950 · Dekrit 1959 · amandemen",
     "example": "Pembukaan — Batang Tubuh — Penutup: struktur UUD 1945.",
     "translation": "UUD 1945 konstitusi tertinggi; semua peraturan harus sesuai dengannya."},
 5: {"fullTitle": "Periodisasi & Amandemen", "subtitle": "1945—kini · Demokrasi Terpimpin · empat amandemen",
     "example": "Amandemen I—IV terjadi 1999—2002 secara bertahap.",
     "translation": "Perjalanan konstitusi: berubah-ubah pada awalnya, stabil setelah amandemen."},
 6: {"fullTitle": "Hubungan Pancasila & Konstitusi", "subtitle": "Sumber hukum · penjabaran · strategi soal",
     "example": "UUD 1945 menjabarkan Pancasila dalam bentuk aturan hukum tertinggi.",
     "translation": "Pancasila jiwa konstitusi; UUD 1945 wujud hukumnya."},
}
chapters = []
q_by_ch = {}
for qq in questions: q_by_ch.setdefault(qq["chapter"], []).append(qq["id"])
for c in new_chapters:
    src = c["src"]; m = META[src["id"]]
    chapters.append({"id": src["id"], "title": src["title"], "fullTitle": m["fullTitle"], "subtitle": m["subtitle"],
                     "intro": src.get("intro", ""), "example": m["example"], "translation": m["translation"],
                     "sections": c["sections"], "questions": q_by_ch[src["id"]]})

summary = """
<h3>Lima Sila Pancasila</h3>
<ul><li><strong>Sila 1:</strong> ketuhanan — kebebasan beribadah dan berkeyakinan.</li><li><strong>Sila 2:</strong> kemanusiaan yang adil dan beradab.</li><li><strong>Sila 3:</strong> persatuan — Bhinneka Tunggal Ika.</li><li><strong>Sila 4:</strong> musyawarah mufakat yang kekeluargaan.</li><li><strong>Sila 5:</strong> keadilan sosial — tujuan negara.</li><li><strong>Piramida:</strong> sila 1 dasar, sila 5 tujuan; kelima sila saling menjiwai.</li></ul>
<h3>Penerapan & Konflik Nilai</h3>
<ul><li>Penerapan dimulai dari tindakan kecil di keluarga, masyarakat, dan sekolah.</li><li>Konflik nilai diselesaikan lewat <strong>musyawarah</strong>: identifikasi — pendapat — titik temu — keputusan.</li><li>Keadilan sosial mencakup ekonomi, politik, dan sosial-budaya.</li><li>Kebijakan publik sesuai Pancasila bila adil, tidak diskriminatif, dan menguntungkan seluruh rakyat.</li></ul>
<h3>Pancasila sebagai Ideologi Negara</h3>
<ul><li>Kedudukan: ideologi, falsafah, dan dasar negara (Pembukaan UUD 1945 alinea 4).</li><li><strong>Ideologi terbuka:</strong> nilai dasar tetap, penjabaran berkembang.</li><li>Dimensi: filosofis, politis, sosiologis.</li><li>Tantangan: internal (hafalan tanpa praktik) dan eksternal (globalisasi).</li></ul>
<h3>UUD 1945 & Konstitusi</h3>
<ul><li>Struktur: Pembukaan (alinea 4 memuat Pancasila), Batang Tubuh, Penutup.</li><li>UUDS 1950: sistem parlementer; Dekrit 5 Juli 1959 mengembalikan UUD 1945.</li><li>Amandemen: usul DPR/Presiden/MPRS, setuju dua per tiga; Pembukaan, NKRI, dan presidensial tidak dapat diubah.</li><li>Indonesia negara hukum — tidak ada pihak di atas hukum.</li></ul>
<h3>Periodisasi & Amandemen</h3>
<ul><li>1945 UUD 1945 (presidensial) → 1949 RIS → 1950 UUDS 1950 (parlementer) → 1959 Dekrit → UUD 1945 kembali.</li><li>Empat amandemen 1999—2002: MPR-HAM, pusat-daerah, tata kekuasaan, ketentuan penyelenggaraan.</li><li>Pelanggaran nilai Pancasila dikenai sanksi sesuai hukum.</li></ul>
<h3>Hubungan Pancasila & Konstitusi</h3>
<ul><li>Pancasila = <strong>sumber segala sumber hukum</strong>; UUD 1945 = penjabarannya.</li><li>Peraturan yang bertentangan dengan keduanya tidak berlaku.</li><li>Soal kompleks: pahami konteks → tentukan sila → kaji sebab-akibat → periksa konsistensi.</li></ul>
<div class="warn-box"><b>STRATEGI SOAL PILIHAN GANDA</b><p>Waspadai kata <strong>absolut</strong> (<em>semua, hanya, selalu, wajib, tidak pernah</em>) — biasanya penanda jawaban salah. Hafalkan pasangan yang sering ditukar: <strong>alinea 1 vs alinea 4</strong>, <strong>presidensial vs parlementer</strong>, <strong>yang tetap vs yang berkembang</strong>, serta arah hubungan <strong>Pancasila → UUD 1945</strong> (UUD menjabarkan Pancasila, bukan sebaliknya).</p></div>
"""

course = {
 "chapters": chapters,
 "questions": questions,
 "summary": summary.strip(),
 "counts": {"chapters": len(chapters), "sections": sum(len(c["sections"]) for c in chapters), "questions": len(questions)},
}
json_str = json.dumps(course, ensure_ascii=False, indent=1)
out = "import type { Course } from './types';\nexport const COURSE: Course = " + json_str + ";\n"
open("src/content.ts", "w", encoding="utf-8").write(out)
print("chapters:", len(chapters), "| sections:", course["counts"]["sections"], "| questions:", len(questions))
print("soal per bab:", [len(c["questions"]) for c in chapters])
print("bank uji kemampuan (P-):", len([x for x in questions if x['id'].startswith('P-')]))
