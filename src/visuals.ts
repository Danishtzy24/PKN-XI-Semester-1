import { esc } from './dom';
import { icon, CHAPTER_ICONS } from './art';
import type { VisualModel, VisualItem, LessonSection } from './types';
/* Ringkasan visual interaktif pendamping materi Pendidikan Pancasila. */
const token=(text: string,role: string='verb')=>({text,role});
const sample=(label: string,sentence: string,formula: string,meaning='',cue=''): VisualItem=>({label,parts:sentence.split('|').map((s,i)=>token(s,['subject','verb','object','extra'][i]||'extra')),formula,meaning,cue});
const lab=(note: string,kind: string,items: VisualItem[]): VisualModel=>({note,kind,items});
const flat=(s: string)=>esc(s.replace(/\|/g,' · '));
export const VISUALS: Record<string, VisualModel> = {
/* ---------- Bab 1 · Lima Sila Pancasila ---------- */
's1-1':lab('Sila pertama: landasan ketuhanan negara.','steps',[
 sample('Makna','Negara|berlandaskan|kepercayaan kepada Tuhan','Pembukaan UUD 1945 alinea pertama','Landasan seluruh nilai Pancasila.'),
 sample('Wujud','Setiap warga|beribadah|menurut agamanya','Kebebasan beribadah dan berkeyakinan','Tidak ada pemaksaan agama kepada siapa pun.'),
 sample('Toleransi','Merayakan hari besar|agama lain|dengan hormat','Saling menghormati keyakinan','Contoh: tidak mengganggu ibadah tetangga.')]),
's1-2':lab('Sila kedua: harkat dan martabat manusia.','steps',[
 sample('Adil','Tidak|diskriminatif|kepada siapa pun','Perlakuan setara','Tidak membedakan suku, agama, atau status.'),
 sample('Beradab','Bertindak|sesuai|budi pekerti','Nilai kesopanan','Contoh: sopan kepada guru dan orang tua.'),
 sample('Contoh','Membantu|korban bencana|tanpa memandang latar','Kemanusiaan nyata','Pertolongan tanpa memilih-milih latar belakang.')]),
's1-3':lab('Sila ketiga: persatuan di atas perbedaan.','steps',[
 sample('Semboyan','Bhinneka|Tunggal|Ika','Berbeda-beda tetapi satu','Dari Kitab Sutasoma karya Mpu Tantular.'),
 sample('Makna','Mengutamakan|persatuan|bangsa','Di atas perbedaan','Keberagaman tetap dipelihara.'),
 sample('Wujud','Menjaga|nama baik|daerah kelahiran','Toleransi antarsuku','Juga memilih produk dalam negeri.')]),
's1-4':lab('Sila keempat: musyawarah mufakat.','flow',[
 sample('01 · Usul','Mengajukan|masalah|untuk didiskusikan','Tahap pembuka','Masalah jelas dan disepakati dibahas.'),
 sample('02 · Pendapat','Setiap pihak|menyampaikan|pendapatnya','Secara teratur','Dilakukan dengan sopan tanpa memotong.'),
 sample('03 · Titik temu','Menimbang|semua pendapat|untuk mencari jalan','Pencarian kesepakatan','Memilih jalan yang dapat diterima semua.'),
 sample('04 · Keputusan','Menetapkan|keputusan|bersama','Diliputi kekeluargaan','Tidak ada pihak yang dipaksa kalah.')]),
's1-5':lab('Sila kelima: keadilan sosial sebagai tujuan.','steps',[
 sample('Makna','Mewujudkan|kesejahteraan|yang merata','Bagi seluruh rakyat','Bukan hanya milik kelompok tertentu.'),
 sample('Contoh','Bantuan sosial|bagi warga|kurang mampu','Program keadilan','Juga beasiswa dan lapangan kerja adil.'),
 sample('Posisi','Tujuan|dari seluruh|pengamalan sila','Puncak piramida','Sila 1—4 bermuara ke sila 5.')]),
's1-6':lab('Piramida nilai: posisi kelima sila.','steps',[
 sample('Sila 1 · Dasar','Ketuhanan|menjadi|landasan seluruh nilai','Puncak piramida di sila 5','Urutan piramida: 1 di dasar, 5 di puncak.'),
 sample('Sila 2 · Inti','Kemanusiaan|menyumbang|semangat','Saling menjiwai','Satu sila menguatkan sila lain.'),
 sample('Sila 3 · Prasyarat','Persatuan|syarat|keutuhan bangsa','Prasyarat kehidupan','Tanpa persatuan, negara terpecah.'),
 sample('Sila 4 · Sarana','Musyawarah|cara mencapai|keputusan','Sarana perjalanan','Musyawarah membawa menuju keadilan.'),
 sample('Sila 5 · Tujuan','Keadilan sosial|hasil akhir|semua nilai','Tujuan negara','Seluruh sila bermuara ke sini.')]),
/* ---------- Bab 2 · Penerapan & Konflik Nilai ---------- */
's2-1':lab('Penerapan dimulai dari lingkaran terdekat.','steps',[
 sample('Keluarga','Beribadah bersama|dan|saling menghargai','Sila 1 dan 2','Musyawarah keputusan rumah tangga (sila 4).'),
 sample('Masyarakat','Gotong royong|dan|kerja bakti','Sila 3','Toleransi antarwarga juga termasuk.'),
 sample('Prinsip','Dimulai|dari tindakan|kecil sehari-hari','Tidak menunggu besar','Konsistensi kecil jadi kebiasaan baik.')]),
's2-2':lab('Menyelesaikan konflik nilai tanpa pemaksaan.','flow',[
 sample('01 · Identifikasi','Menentukan|masalah|dan pihak terlibat','Langkah pertama','Semua pihak sepakat masalah dibahas.'),
 sample('02 · Menyuarakan','Setiap pihak|menyampaikan|pendapat dengan sopan','Semua terwakili','Tidak ada pihak yang didiamkan.'),
 sample('03 · Titik temu','Mencari|persamaan|yang diterima semua','Jalan kompromi','Contoh: jadwal kegiatan yang disepakati.'),
 sample('04 · Keputusan','Menetapkan|keputusan|bersama','Selesai tanpa pemaksaan','Semangat kekeluargaan tetap terjaga.')]),
's2-3':lab('Pancasila hidup di sekolah.','steps',[
 sample('Upacara','Bendera|dinaikkan|setiap hari Senin','Sila 3 — persatuan','Kedisiplinan dan kebersamaan.'),
 sample('Pelajaran','Pendidikan Pancasila|diajarkan|di kelas','Semua sila','Pemahaman nilai sejak sekolah.'),
 sample('Budaya','Menghargai|guru|dan teman','Sila 2','Tidak menang sendiri saat bertanding.'),
 sample('Teladan','Kepala sekolah|menjadi|contoh nilai','Panutan penerapan','Guru dan siswa meniru keteladanan.')]),
's2-4':lab('Memetakan tindakan ke sila yang menjiwai.','steps',[
 sample('Membantu sakit','Membantu|tetangga|yang sakit','Sila 2 dan sila 5','Kemanusiaan dan keadilan sekaligus.'),
 sample('Patuh aturan','Wajib patuh|pada peraturan|sekolah','Sila 4','Aturan bersama disepakati bersama.'),
 sample('Kebersihan','Menjaga|kebersihan|lingkungan','Sila 3','Kepentingan bersama di atas pribadi.'),
 sample('Mengingat','Satu tindakan|dapat menjiwai|lebih dari satu sila','Kunci soal','Pilih jawaban yang menyebut semua sila.')]),
's2-5':lab('Keadilan sosial punya tiga wajah.','paper',[
 sample('01 · Ekonomi','Pemerataan|kesejahteraan|untuk semua','Bantuan sosial · beasiswa','Kesenjangan ditekan.'),
 sample('02 · Politik','Hak suara|yang sama|bagi semua warga','Pemilu dan pilkada','Setiap suara bernilai sama.'),
 sample('03 · Sosial-budaya','Penghargaan|terhadap|semua kelompok','Termasuk minoritas','Tidak ada kelompok direndahkan.')]),
's2-6':lab('Kriteria kebijakan yang sesuai Pancasila.','steps',[
 sample('Menguntungkan','Manfaat|bagi seluruh|rakyat','Bukan satu kelompok','Contoh: bantuan bagi prasejahtera.'),
 sample('Adil','Tidak|diskriminatif|antarwarga','Semua terlayani','Wilayah pun tidak diabaikan.'),
 sample('Persatuan','Mendukung|keutuhan|bangsa','Sila 3','Tidak memecah belah masyarakat.'),
 sample('Jebakan','Kebijakan|satu kelompok|saja = belum sesuai','Sila 5 belum terwujud','Soal sering uji contoh seperti ini.')]),
/* ---------- Bab 3 · Ideologi Negara ---------- */
's3-1':lab('Tiga sebutan, satu kedudukan Pancasila.','steps',[
 sample('Ideologi','Sistem nilai|dan pandangan|hidup bangsa','Pedoman berbangsa','Menjadi acuan perilaku warga.'),
 sample('Falsafah','Pikiran dasar|mengatur|kehidupan berbangsa','Landasan berpikir','Sumber aturan dan keputusan.'),
 sample('Dasar negara','Fondasi|penyelenggaraan|negara','Pembukaan alinea 4','Sumber segala sumber hukum.')]),
's3-2':lab('Ideologi terbuka: tetap dan berkembang.','paper',[
 sample('01 · Nilai dasar','Lima sila|tetap|tidak berubah','Substansi terkunci','Tidak boleh direvisi.'),
 sample('02 · Penjabaran','Pelaksanaan|menyesuaikan|zaman','Cara mewujud berkembang','Contoh: etika digital baru.'),
 sample('03 · Relevansi','Tetap pedoman|dari masa|ke masa','Ideologi terbuka','Relevan sejak 1945 sampai kini.')]),
's3-3':lab('Tiga dimensi Pancasila.','paper',[
 sample('01 · Filosofis','Nilai moral|dan kearifan|landasan berpikir','Dimensi pikiran','Menjadi dasar menilai benar-salah.'),
 sample('02 · Politis','Dasar negara|dan pedoman|kebijakan','Dimensi negara','Kebijakan diukur dengan Pancasila.'),
 sample('03 · Sosiologis','Budaya hidup|yang dipraktikkan|masyarakat','Dimensi masyarakat','Nilai hidup dalam kebiasaan.')]),
's3-4':lab('Tantangan dari dalam dan luar.','steps',[
 sample('Internal','Paham hanya|hafalan|tanpa praktik','Tindak tanduk kurang','Nilai belum hidup sehari-hari.'),
 sample('Eksternal','Globalisasi|dan nilai asing|yang bentrok','Juga gerakan penggugat','Masuk lewat budaya dan media.'),
 sample('Jawaban','Perdalam paham|lalu wujudkan|dalam tindak tanduk','Bukan hafalan saja','Praktik nyata di rumah dan sekolah.')]),
's3-5':lab('Pancasila di era digital dan dunia kerja.','steps',[
 sample('Informasi','Menyebarkan|informasi|yang benar','Lawan hoaks','Cek kebenaran sebelum bagikan.'),
 sample('Media sosial','Menghormati|hak orang lain|di dunia maya','Termasuk karya','Jangan salin tanpa izin.'),
 sample('Teknologi','Untuk|kepentingan|bersama','Bukan perusak','Konten menjaga nama baik bangsa.'),
 sample('Kerja','Bekerja|jujur|dan disiplin','Etika profesi','Pancasila di tempat kerja.')]),
/* ---------- Bab 4 · Proses Perubahan UUD 1945 ---------- */
'k4-1':lab('Enam tuntutan Reformasi 1998.','steps',[
 sample('01 · Amandemen','Amandemen|UUD|1945','Tuntutan pertama','Jalan utama perubahan aturan dasar.'),
 sample('02 · Dwi Fungsi','Penghapusan|Dwi Fungsi|ABRI','Peran ganda dihapus','Militer lepas dari peran sosial-politik.'),
 sample('03 · Hukum','Penegakan|hukum, HAM, KKN','Tuntutan ketiga','Hukum dan HAM berdiri sejajar.'),
 sample('04 · Daerah','Otonomi|Daerah','Devolusi wewenang','Daerah mengatur urusannya sendiri.'),
 sample('05 · Pers','Kebebasan|Pers','Informasi terbuka','Wartawan bebas meliput.'),
 sample('06 · Demokrasi','Mewujudkan|kehidupan|demokrasi','Tuntutan keenam','Rakyat ikut menentukan kebijakan.')]),
'k4-2':lab('Menyempurnakan aturan dasar negara.','paper',[
 sample('01 · Tatanan','Tatanan|negara|disempurnakan','Ruang lingkup 1','Struktur negara ditata ulang.'),
 sample('02 · Kedaulatan','Kedaulatan|rakyat|ditegakkan','Ruang lingkup 2','Kekuasaan kembali ke rakyat.'),
 sample('03 · HAM & Kekuasaan','HAM|dan pembagian|kekuasaan','Ruang lingkup 3—4','Hak dijamin, kekuasaan terbagi.'),
 sample('04 · Kesejahteraan','Kesejahteraan|sosial|dan negara hukum','Ruang lingkup 5—6','Adil dan berkeadilan.'),
 sample('05 · Aspirasi','Hal lain|sesuai|aspirasi bangsa','Ruang lingkup 7','Mengikuti kebutuhan rakyat.')]),
'k4-3':lab('Empat sidang MPR 1999—2002.','line',[
 sample('1999','Sidang Umum MPR|14—21|Oktober 1999','Amandemen I','Kesepakatan dasar pertama.'),
 sample('2000','Sidang Tahunan MPR|7—18|Agustus 2000','Amandemen II','Otonomi daerah menguat.'),
 sample('2001','Sidang Tahunan MPR|1—9|November 2001','Amandemen III','Lembaga negara ditata.'),
 sample('2002','Sidang Tahunan MPR|1—11|Agustus 2002','Amandemen IV','Struktur 21/73/170.')]),
'k4-4':lab('Struktur sebelum dan sesudah perubahan.','paper',[
 sample('01 · Sebelum','16 bab|37 pasal|49 ayat','Aturan Peralihan 4','Aturan Tambahan 2 ayat.'),
 sample('02 · Sesudah','21 bab|73 pasal|170 ayat','Aturan Peralihan 3','Aturan Tambahan 2 pasal.'),
 sample('03 · Tanpa Pembukaan','Pembukaan|tidak|diubah','Adendum','Perubahan menyambung naskah lama.'),
 sample('04 · Presidensial','Sistem|presidensiil|diperkuat','Penjelasan → pasal','Norma masuk ke batang tubuh.')]),
'k4-5':lab('Naskah resmi UUD 1945 dan amandemen.','line',[
 sample('1945','Ditetapkan|18 Agustus|1945','Naskah asli','Proklamasi menegaskan berlakunya.'),
 sample('1959','Dekrit Presiden|5 Juli|1959','Berlaku kembali','Dikukuhkan aklamasi 22 Juli 1959.'),
 sample('1999—2002','Empat|naskah|perubahan','Amandemen I—IV','Satu naskah kompilasi 2002.')]),
'k4-6':lab('Lembaga ketatanegaraan UUD 1945.','w6',[
 sample('MPR','Mengubah & menetapkan UUD','Pasal 3 & 37'),
 sample('DPR','Membentuk undang-undang','Pasal 20 (1)'),
 sample('DPD','Dipilih melalui pemilu','Pasal 22C'),
 sample('Presiden','Kekuasaan pemerintahan','Pasal 4 (1)'),
 sample('MA & KY','Kekuasaan kehakiman merdeka','Pasal 24'),
 sample('MK','Memutus sengketa kewenangan','Pasal 24C'),
 sample('BPK','Memeriksa pengelolaan keuangan','Pasal 23E'),
 sample('Bank Sentral','Menjaga stabilitas rupiah','Pasal 23D')]),
'k4-7':lab('MPR: lembaga tertinggi vs lembaga negara.','paper',[
 sample('01 · Sebelum','Lembaga|Tertinggi|Negara','Penjelmaan rakyat','Pemegang kedaulatan sepenuhnya.'),
 sample('02 · Sesudah','Lembaga|permusyawaratan|rakyat','Berstatus lembaga negara','Anggota: DPR + DPD hasil pemilu.'),
 sample('03 · GBHN','Menetapkan|GBHN|hanya sebelum perubahan','Hilang sesudahnya','Fokus ke UUD & UU.'),
 sample('04 · Pemberhentian','Memberhentikan|Presiden|lewat sidang','Wewenang tetap','Dengan putusan pengadilan.')]),
/* ---------- Bab 5 · Periodisasi Konstitusi ---------- */
'k5-1':lab('Tiga konstitusi periode pertama.','line',[
 sample('1945','UUD 1945|18 Agu 1945—27 Des|1949','Periode 1','Berlaku sejak proklamasi.'),
 sample('1949','Konstitusi RIS|27 Des 1949—17 Agu|1950','Periode 2','Republik Indonesia Serikat.'),
 sample('1950','UUDS 1950|17 Agu 1950—5 Jul|1959','Periode 3','Sistem parlementer.')]),
'k5-2':lab('Kembali ke UUD 1945 (1959—1999).','steps',[
 sample('Dekrit','UUD 1945|berlaku|kembali','5 Juli 1959','Dekrit Presiden mengakhiri UUDS.'),
 sample('Masa','Berlaku|sampai|19 Oktober 1999','40 tahun','Masuk amandemen pertama.'),
 sample('Amandemen','Dimulai|amandemen|pertama','19 Oktober 1999','Awal periode kelima.')]),
'k5-3':lab('Rentang waktu amandemen I—IV.','line',[
 sample('I','19 Okt 1999|— 18 Agu|2000','Amandemen I','MPR 1999 menyetujui.'),
 sample('II','18 Agu 2000|— 9 Nov|2001','Amandemen II','Otonomi & pemilihan.'),
 sample('III','9 Nov 2001|— 10 Agu|2002','Amandemen III','Lembaga negara.'),
 sample('IV','10 Agu 2002|— sekarang','Amandemen IV','Berlaku hingga kini.')]),
'k5-4':lab('Tugas: telusuri pasal yang diamandemen.','flow',[
 sample('01 · Kumpulkan','Siapkan|naskah|perubahan I—IV','Bahan rujukan','Naskah resmi MPR.'),
 sample('02 · Bandingkan','Bandingkan|pasal lama|dan baru','Sebelum—sesudah','Perhatikan bunyi tiap ayat.'),
 sample('03 · Catat','Catat|nomor pasal|dan amandemen','Format rapi','Nomor pasal + amandemen ke-berapa.'),
 sample('04 · Rangkum','Rangkum|perubahan|bersama teman','Diskusi kelas','Kunci pemahaman periodisasi.')]),
/* ---------- Bab 6 · TAP MPR & Tata Cara UUD ---------- */
'k6-1':lab('TAP MPR No. I/MPR/2003: enam kelompok status.','paper',[
 sample('01 · Pasal 1','8 TAP|dicabut|& tidak berlaku','Berakhir masa berlaku','Sebagian sudah diatur UUD.'),
 sample('02 · Pasal 2','3 TAP|tetap|berlaku + ketentuan','Syarat khusus','Contoh: XXV/MPRS/1966.'),
 sample('03 · Pasal 3','8 TAP|sampai|Pemilu 2004','Batas waktu','GBHN 1999—2004 dsb.'),
 sample('04 · Pasal 4','11 TAP|sampai|terbentuk UU','Menunggu UU','XI/MPR/1998 dsb.'),
 sample('05 · Pasal 5','5 TAP|sampai|tatib baru','Tata tertib MPR','II/MPR/1999 dsb.'),
 sample('06 · Pasal 6','104 TAP|final|/ einmalig','Tidak perlu tindakan','Kelompok terbesar.')]),
'k6-2':lab('Delapan TAP dicabut, tiga dengan ketentuan.','steps',[
 sample('Dicabut','8 TAP|X/MPRS/1966|dst.','Pasal 1','Berakhir atau tergantikan UUD.'),
 sample('PKI','XXV/MPRS/1966|berlaku|berkeadilan','Pasal 2','Hormati HAM & demokrasi.'),
 sample('Ekonomi','XVI/MPR/1998|pilar|ekonomi kecil','Pasal 2','Koperasi & UMKM.'),
 sample('Timor Timur','V/MPR/1999|sampai|tuntas','Pasal 2','Kewarganegaraan & aset.')]),
'k6-3':lab('Sembilan belas TAP berlaku sementara.','paper',[
 sample('01 · Pasal 3','8 TAP|menunggu|Pemilu 2004','GBHN 1999—2004','Laporan tahunan MPR.'),
 sample('02 · Pasal 4a','XXIX/MPRS/1966|XI & XV|MPR/1998','Pahlawan · KKN · Otonomi','Sampai UU lahir.'),
 sample('03 · Pasal 4b','III/MPR/2000|sumber|hukum','Tata urutan peraturan','UU pembungkus peraturan.'),
 sample('04 · Pasal 4c','VI & VII|MPR/2000|TNI—POLRI','Pemisahan & peran','Etika & visi bangsa 2001.')]),
'k6-4':lab('Tatib MPR dan 104 TAP final.','steps',[
 sample('Tatib','5 TAP|tatib|MPR','Pasal 2 dan 5','II/MPR/1999 dst.'),
 sample('Batash','Tatib baru|hasil|Pemilu 2004','Menggantikan tatib lama','Tatib lama berakhir.'),
 sample('Final','104 TAP|final|/ einmalig','Pasal 6','Sudah dicabut atau selesai.'),
 sample('Arti','Tidak perlu|tindakan|hukum lanjut','Tuntas','Status hukumnya jelas.')]),
'k6-5':lab('Tata cara perubahan UUD 1945.','flow',[
 sample('01 · Usul','Usul|1/3|anggota MPR','Pasal 91','Tertulis dan beralasan.'),
 sample('02 · Pimpinan','Diajukan|ke|Pimpinan + berita acara','3×24 jam tidak boleh ditarik','Pemeriksaan ≤30 hari.'),
 sample('03 · Salinan','Salinan|≤14 hari|sebelum paripurna','Pasal 94','Usul tidak lengkap ditolak.'),
 sample('04 · Sidang','Hadir 2/3|setuju|50%+1','Pasal 37','NKRI tidak dapat diubah.')]),
'k6-6':lab('Pemberhentian Presiden & Wakil Presiden.','flow',[
 sample('01 · DPR','Usul|≥2/3|anggota hadir','Pasal 7B (2)—(3)','DPR meneruskan ke MK.'),
 sample('02 · MK','Putus|≤90|hari','Pasal 7B (4)','Mahkamah memeriksa fakta.'),
 sample('03 · MPR','Sidang|≤30|hari setelah putusan MK','Pasal 7B (5)—(6)','Tatib 102—103.'),
 sample('04 · Putusan','Hadir 3/4|setuju|2/3 hadir','Pasal 7B (7)','Presiden diberi kesempatan jelaskan.')]),
};
function labDiagram(v: VisualModel,index: number): string{const i=v.items[index];

 if(v.kind==='paper')return `<div class="paper-diagram">${v.items.map((it,j)=>`<span class="pd-row ${j===index?'current':j<index?'passed':''}"><i>${esc(it.label.replace(/^\d+ · /,''))}</i><b>${flat(it.formula)}</b></span>`).join('')}</div>`;
 if(v.kind==='w6')return `<div class="w6-diagram">${v.items.map((it,j)=>`<span class="wh-cell ${j===index?'current':''}"><b>${esc(it.label.replace(/^\d+ · /,''))}</b><i>${flat(it.formula)}</i></span>`).join('')}</div>`;
 if(v.kind==='line')return `<div class="line-diagram">${v.items.map((it,j)=>`<span class="ln-item ${j===index?'current':j<index?'passed':''}"><i>${j===index?'':'\u25cf'}</i><div><b>${esc(it.label)}</b><em>${flat(it.formula)}</em></div></span>`).join('')}</div>`;
 if(v.kind==='flow')return `<div class="flow-diagram">${v.items.map((it,j)=>`<span class="fd-card ${j===index?'current':j<index?'passed':''}"><i>${String(j+1).padStart(2,'0')}</i><div><b>${esc(it.label.replace(/^\d+ · /,''))}</b><em>${flat(it.formula)}</em></div></span>${j<v.items.length-1?'<em class="fd-arrow">↓</em>':''}`).join('')}</div>`;
 if(v.kind==='compare')return `<div class="compare-diagram"><span class="cd-col ${index===0||index===2?'current':''}"><i>FAKTA</i><small>berbukti · dapat dibuktikan</small></span><span class="cd-vs">≠</span><span class="cd-col other ${index===1||index===2?'current':''}"><i>INTERPRETASI</i><small>penafsiran · pandangan</small></span></div>`;
 if(v.kind==='chat')return `<div class="chat-diagram"><span class="chat-avatar">A</span><div class="chat-bubble">${icon('chat')}<i>${i.formula}</i><span></span><span></span><span></span></div><span class="chat-avatar other">B</span></div>`;
 if(v.kind==='steps')return `<div class="step-diagram">${v.items.map((it,j)=>`<span class="${j===index?'current':j<index?'passed':''}"><b>${j<index?'\u2713':String(j+1).padStart(2,'0')}</b><i>${it.label.replace(/^\d+ · /,'')}</i></span>`).join('')}</div>`;
 return `<div class="syntax-diagram"><span>A<small>AWAL</small></span><i>→</i><span>I<small>INTI</small></span><i>→</i><span>P<small>PELENGKAP / KETERANGAN</small></span></div>`;
}
export function labStageHTML(v: VisualModel,index: number){const i=v.items[index];
 return `${labDiagram(v,index)}<div class="sentence-pieces" lang="id">${i.parts.map((p,j)=>`<div class="sentence-piece piece-${p.role}"><b>${esc(p.text)}</b><small>${['AWAL','INTI','PELENGKAP','KETERANGAN'][j]||'KETERANGAN'}</small></div>`).join('')}</div><div class="lab-bottom"><div class="lab-formula">${icon('layers')}<span>${esc(i.formula)}</span></div>${i.meaning?`<p>${esc(i.meaning)}</p>`:''}</div>`}
export function visualHTML(s: LessonSection,chapterId: number){const v=VISUALS[s.id];return `<div class="visual-lab" data-lab="${s.id}" data-index="0"><div class="lab-caption"><span>${icon(CHAPTER_ICONS[chapterId-1])} ${esc(v.note)}</span><b>INTERAKTIF</b></div><div class="lab-controls" role="group" aria-label="Contoh ${esc(s.title)}">${v.items.map((it,i)=>`<button class="${i===0?'selected':''}" data-lab-choice="${i}" aria-pressed="${i===0}"><i class="lab-num" aria-hidden="true">${String(i+1).padStart(2,'0')}</i><span>${esc(it.label.replace(/^\d+ · /,''))}</span></button>`).join('')}</div><div class="lab-stage" aria-live="polite">${labStageHTML(v,0)}</div><div class="lab-pagination"><span>01 <i>/ ${String(v.items.length).padStart(2,'0')}</i></span><button data-lab-next>Contoh berikutnya ${icon('arrow')}</button></div></div>`}
