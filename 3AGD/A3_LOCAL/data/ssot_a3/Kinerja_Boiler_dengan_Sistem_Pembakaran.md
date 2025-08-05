# Kinerja_Boiler_dengan_Sistem_Pembakaran

**Fonte**: Kinerja_Boiler_dengan_Sistem_Pembakaran.pdf  
**Data de conversão**: 2025-07-30 15:08:36  
**Origem**: base_relevantes

---

102 SEMESTA TEKNIKA
Vol.24, No.2, 102-110, November 2021
DOI : https://doi.org/10.18196/st.v24i2.12937
Kinerja Boiler dengan Sistem Pembakaran Bersama antara Ampas Tebu dengan Sekam
Padi dan Cangkang Kelapa Sawit
(Boiler Performance Based Co-Firing Bagasse with Rice Husk and Shell Palm Oil)
SAPTYAJI HARNOWO, YUNAIDI
ABSTRAK
Operasional boiler di sebagian besar pabrik gula saat ini banyak yang mengalami
kekurangan pasokan bahan bakar ampas tebu karena penurunan kapasitas giling.
Kondisi ini menimbulkan masalah terhadap kontinuitas pasokan energi uap dan listrik
di pabrik gula, sehingga untuk mengatasi masalah tersebut banyak dilakukan dengan
penambahan bahan bakar alternatif dengan model pembakaran bersama (co-firing).
Penelitian ini mencoba melakukan kajian model pembakaran bersama ampas tebu
dengan sekam padi dan cangkang kelapa sawit berbasis persentase berat bahan bakar.
Penelitian dilakukan berdasarkan data operasional boiler di pabrik gula Trangkil saat
musim giling tahun 2020. Data yang dikumpulkan meliputi tekanan, kapasitas, dan
temperatur uap, serta temperatur air masuk boiler dan temperatur gas buang. Analisis
bahan bakar yang dilakukan adalah uji proksimat dan ultimat. Perhitungan dan
simulasi pemakaian bahan bakar, kebutuhan volume furnace, efisiensi, dan rugi-rugi
boiler dilakukan menggunakan bantuan analisis software Firecad WTPB. Hasil
penelitian menunjukkan bahwa co-firing dapat menaikkan efisiensi boiler,
menurunkan rugi-rugi boiler, menurunkan pemakaian bahan bakar dan kebutuhan
volume furnace, serta menurunkan kecepatan gas buang di sekitar pipa-pipa uap
utama. Mitigasi risiko harus dilakukan karena sistem ini dapat meningkatkan
temperatur furnace, yang dapat meningkatkan potensi slagging dan fouling sehingga
mengganggu kinerja boiler saat musim giling.
Kata kunci: Boiler, Co-firing, Ampas Tebu, Sekam Padi, Cangkang Kelapa Sawit.
ABSTRACT
Boiler operations in most sugar factories are currently experiencing a shortage of
bagasse fuel supply due to a decrease in mill capacity. This condition causes problems
in the continuity of the steam and the electricity supply in the sugar factory. The
research aims to study the co-firing model of bagasse fuel with rice husks and palm
oil shells. The research was conducted based on the boiler’s operational data at
Trangkil sugar factory milling season in 2020. The data collected consisted of the
pressure, the capacity, the steam temperature, and the boiler inlet water and flue gas
temperature. The fuel analysis carried out is the proximate and ultimate test. The
calculations and simulations of fuel consumption, furnace volume requirements,
efficiency and losses carried out the computational analysis with Firecad WTPB
software. The result shows that the boiler efficiency increases by co-firing and
reducing fuel consumption boiler, furnace volume requirements, and gas velocity at
boiler banks. The risk mitigation should be investigated during boiler operations
because this system can increase the furnace temperature, which can escalate the
potential for slagging and fouling as well as pipe erosion so that it interferes with
boiler performance during milling season.
Keywords: Boiler, Co-firing, Bagasse, Rice Husk, Palm Oil Shells.

S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021 103
menjadi berkurang sehingga diperlukan bahan
PENDAHULUAN bakar tambahan alternatif selama masa giling
pabrik. Bahan bakar alternatif biomassa yang
ditambahkan antara lain cacahan gergajian
Perkembangan industri gula nasional di pulau
kayu, sekam padi, daduk (cane trash), dan
Jawa dalam kurun waktu lima tahun terakhir
biomassa lainnya dengan total biaya suplesi
mengalami peningkatan yang sangat cepat
bahan bakar mencapai 12 miliar rupiah (P3GI,
dengan adanya penambahan kapasitas olah
2016).
pabrik gula melalui program PMN (Penyertaan
Modal Negara) dalam pengembangan pabrik Salah satu metode untuk mengatasi kekurangan
gula milik BUMN serta pembangunan pabrik pasokan bahan bakar ampas adalah
gula baru oleh pihak swasta. Dalam kurun menggunakan sistem pembakaran bersama (co-
waktu 10 tahun terakhir telah dibangun 11 firing). Sistem co-firing adalah pembakaran
pabrik gula baru baik di pulau Jawa maupun proses pembakaran dua atau lebih bahan bakar
luar pulau Jawa, sehingga menjadikan kapasitas yang berbeda pada boiler untuk
total terpasang pabrik gula baru pada tahun membangkitkan daya. Tujuan utama sistem ini
2020 mencapai 112 ribu TCD (Asosiasi Gula adalah menggantikan bahan bakar utama
Indonesia, 2020). Disisi lain, produksi gula tebu dengan bahan bakar alternatif untuk
nasional pada tahun 2020 tercatat sebesar 2,13 mendapatkan manfaat tertentu. Co-firing
juta ton atau bisa dikatakan tidak mengalami banyak diaplikasikan dengan menggunakan
peningkatan yang signifikan dalam kurun semua jenis boiler yang ada, padahal untuk
waktu lima tahun terakhir (Nasution, 2021b). sebagian jenis boiler awalnya hanya dirancang
Hal ini disebabkan peningkatan kapasitas untuk membakar jenis bahan bakar tertentu atau
produksi pabrik gula tidak diimbangi dengan tidak dirancang untuk sistem co-firing. Deposisi
penambahan luas areal tanaman tebu dan abu merupakan parameter penting pada
jumlah tebu yang akan digiling, bahkan pembakaran biomassa, karena berkaitan erat
mengalami penurunan (Nasution, 2021a; dengan biaya operasional boiler. Dua tipe
Asosiasi Gula Indonesia, 2020). deposisi abu pada pipa dan dinding boiler
dikenal dengan istilah slagging dan fouling.
Kondisi ini menimbulkan permasalahan bagi
Karakteristik slagging dan fouling dari
pabrik gula karena pasokan bahan baku tebu
biomassa baik secara individu maupun co-firing
menjadi berkurang akibat peningkatan
dapat mempengaruhi perpindahan panas yang
kapasitas olah pabrik gula tidak diimbangi
terjadi dan menyebabkan kerugian panas.
dengan peningkatan jumlah tebu yang akan
digiling, sehingga kapasitas olah maksimum Ampas tebu (bagasse) adalah bahan bakar
pabrik gula sulit dicapai. Pada saat ini terdapat dengan komposisi, konsistensi, dan nilai kalor
62 pabrik gula di Indonesia dengan kapasitas yang bervariasi. Karakteristik ini tergantung
terpasang total 316.95 ribu TCD, dengan 43 pada iklim, jenis tanah tempat tebu ditanam,
pabrik gula dimiliki BUMN dan 19 pabrik gula varietas tebu, metode panen, dan efisiensi
dimiliki perusahaan swasta. Apabila seluruh pabrik gula. Secara umum, ampas tebu
pabrik gula ini dapat beroperasi secara optimal memiliki nilai kalor antara 1600 s.d. 2400
dan efisien, maka dapat menghasilkan produk kkal/kg. Sebagai bahan bakar utama boiler di
gula sebanyak 3,5 juta ton/tahun. Jika hal ini pabrik gula, ampas tebu merupakan bahan
terealisasi, maka swasembada gula konsumsi bakar berserat yang memiliki kadar air antara
akan dapat tercapai (Kemenperin, 2021). 48% - 52%, sedangkan boiler di pabrik gula
Sampai dengan saat ini, meskipun usaha biasanya di desain dengan kemampuan bahan
kerjasama penyiapan lahan tebu baru sistem bakar ampas dengan kadar air 42 – 57% dan
sinergi BUMN antara PT Perkebunan kadar abu dibawah 2,5%. Sementara apabila
Nusantara dengan Perhutani telah dilakukan, terdapat tambahan bahan bakar biomassa lain
tetapi belum menunjukkan hasil yang seperti limbah kayu memiliki kadar air
memuaskan (Fauzan, 2020). bervariasi dari 20% - 60% dan kadar abu 1%-
15%, sehingga dengan sistem pembakaran co-
Hasil kajian efisiensi energi pabrik gula di
firing mengakibatkan terjadinya perubahan
wilayah PT Perkebunan Nusantara IX Jawa
kadar air dan kadar abu sehingga potensi kinerja
Tengah menunjukkan bahwa akibat
boiler akan berubah. Variasi kadar air dan kadar
berkurangnya pasokan bahan baku tebu yang
abu dari bahan bakar baik secara individu
diolah oleh pabrik mengakibatkan ketersediaan
maupun co-firing akan mengakibatkan
ampas tebu sebagai bahan bakar utama boiler

104 S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021
berubahnya nilai kalor pada aliran gas risiko di atas (Yunaidi, Surahmanto, &
pembakaran yang mempengaruhi unjuk kerja Harnowo, 2020).
ruang bakar dan superheater pada boiler
Pemakaian bahan bakar co-firing antara ampas
(Naude, 2001).
tebu dengan sekam padi pada fluidized bed
Dalam pemakaian bahan bakar alternatif boiler combustor menunjukkan bahwa akan
biomassa perlu dipertimbangkan jumlah kadar terjadi kehilangan efisiensi pembakaran antara
abu (%) serta kandungan unsur di dalamnya 1% s.d. 1.5% akibat meningkatnya kadar abu
yang meliputi unsur yang bersifat basa (alkali) dalam bahan bakar serta menghasilkan rugi
yaitu Fe O , CaO, MgO, Na O, dan K O serta panas sebesar 1.5% akibat kandungan oksigen
2 3 2 2
unsur yang bersifat asam yaitu SiO , Al O , dan dalam gas buang (Ninduangdee & Kuprianov,
2 2 3
TiO . Kandungan asam dan basa dalam abu 2018).
2
memberikan dampak terhadap terjadinya
Penelitian tentang pengaruh pemakaian bahan
slagging di dapur boiler dan fouling pada
bakar biomassa pada boiler berbasis batubara
peralatan perpindahan panas boiler (piping,
menunjukkan bahwa pemakaian bahan bakar
superheater, dan air heater). Kandungan abu
co-firing antara batubara dengan biomassa
yang tinggi dalam bahan bakar ampas tebu juga
dapat menurunkan efisiensi boiler seiring
akan menurunkan produksi uap. Semakin tinggi
dengan peningkatan persentase biomassa dalam
kadar abu pada bahan bakar ampas tebu dengan
campuran bahan bakar, menurunkan temperatur
kadar air yang sama maka jumlah uap yang
gas buang, menaikkan kandungan karbon yang
dihasilkan pada boiler semakin kecil (McIntyre,
tidak terbakar dalam fly ash, dan menaikkan
2013).
potensi slagging. Di sisi lain potensi emisi gas
Karakteristik biomassa yang sangat berbeda buang berupa gas NOx akan turun seiring
dari bahan bakar fosil secara umum meliputi dengan meningkatnya persentase biomassa
perbedaan dalam kadar air, kadar abu, nilai sehingga lebih aman bagi lingkungan (Wang et
kalor, dan kandungan alkali logam. Kadar abu al., 2021).
biomassa biasanya memiliki konsentrasi logam
Kinerja boiler sering dinyatakan dalam efisiensi
alkali lebih tinggi seperti kalium (K), klorin
boiler dan rasio penguapan biasanya akan
(Cl), dan silikon (Si), serta memiliki variasi
menurun seiring dengan berjalannya waktu. Hal
kadar air yang tinggi dan kandungan sulfur yang
ini disebabkan oleh pembakaran dan kualitas
lebih rendah. Perbedaan fitur bahan bakar
bahan bakar yang buruk, munculnya slagging
biomassa dan kadar abu tidak hanya
atau fouling yang menghambat perpindahan
berpengaruh pada pembakaran, tetapi juga
panas, kualitas air yang tidak sesuai, dan
secara signifikan mengubah potensi perilaku
buruknya perawatan. Efisiensi boiler secara
kadar abu untuk membentuk deposit pada suhu
umum dipengaruhi oleh tiga komponen utama,
dibawah ruang bakar dapur boiler dan akan
yaitu efisiensi pembakaran, efisiensi termal,
meleleh di atas boiler grate (Rein, 2016).
dan efisiensi bahan bakar menjadi uap air (fuel
Penggunaan berbagai jenis biomassa sebagai to steam). Pengujian efisiensi dilakukan untuk
bahan bakar boiler dapat menimbulkan resiko mendeteksi seberapa besar penyimpangan
kontaminasi dan kerusakan yang berbeda pada efisiensi boiler dari kondisi terbaik. Pengujian
peralatan pemanas boiler seperti slagging, efisiensi dapat dilakukan menggunakan dua
fouling, korosi, aglomerasi dan sintering. metode, yaitu metode langsung atau metode
Sekam padi memiliki nilai kalor yang lebih input-output (metode keseimbangan energi),
rendah dari ampas tebu tetapi memiliki kadar dan metode tidak langsung atau metode
abu yang lebih tinggi, sehingga membutuhkan kerugian panas (heat loss). Berdasar metode
penyesuaian dalam pengoperasian boiler saat kerugian panas ini, efisiensi boiler berbahan
menggunakan sekam padi sebagai bahan bakar bakar ampas dominan dipengaruhi oleh
alternatif untuk sistem pembakaran bersama kerugian panas pada gas buang (flue gas) dan
dengan ampas tebu. Berdasarkan analisis tingkat kebasahan ampas tebu (Patel & Modi,
komposisi abu ampas tebu dan sekam padi, 2016).
penerapan sekam padi sebagai bahan bakar co-
Sebagian besar pengukuran kinerja boiler
firing pada boiler di pabrik gula tidak akan
menggunakan metode kerugian panas mengacu
menimbulkan potensi kerusakan yang serius
pada standar ASME PTC 4 Fire Steam
seperti slagging, fouling, korosi, sintering, dan
Generators yang berbasis boiler berbahan
aglomerasi, tetapi tingginya persentase kadar
bakar batubara. Oleh karena itu, dalam
abu sekam padi dapat meningkatkan potensi

S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021 105
pengukuran kinerja boiler yang menggunakan Keterangan:
bakar biomassa diperlukan beberapa  : efisiensi boiler
penyesuaian standar tersebut karena perbedaan L : kerugian panas dalam gas buang
1
parameter bahan bakar yang dipakai. L : kerugian panas karena kelembaban
2
(H O) dan hidrogen (H ) dalam bahan
Berdasarkan kondisi kebutuhan ampas tebu 2 2
bakar
hasil proses pengolahan pabrik tersebut di atas,
L : kerugian karena kelembaban dalam
peneliti melakukan riset terkait kinerja boiler 3
udara
pabrik gula yang menggunakan bahan bakar co-
L : kerugian kadar abu dalam bahan bakar
firing antara ampas tebu dengan sekam padi dan 4
serta kerugian radiasi dan konveksi
cangkang kelapa sawit menggunakan metode
pada permukaan
kerugian panas (heat loss) sesuai dengan
standar ASME PTC 4 Fire Steam Generators. Persamaan-persamaan yang bisa digunakan
untuk menentukan kerugian (losses) panas
dalam boiler antara lain:
METODE PENELITIAN
a) Udara teoritis yang dibutuhkan untuk
pembakaran:
Pengukuran kinerja boiler dilakukan dengan
metode tidak langsung atau metode kerugian
panas. Metode penentuan efisiensi ini kg/kg
memperhitungkan semua jenis kehilangan ba(h1a1n.6 xb Ca)k+a [r3 4.8 x (H2 − O 2 / 8 ) ] + ( 4 . 3 5 x S ) (3)
= 100
panas yang terjadi di dalam boiler. Efisiensi
boiler dihitung dengan menjumlahkan C, H , O , S adalah berat atom bahan bakar
2 2
persentase semua kerugian dan mengurangi berdasarkan analisis proksimat dan ultimat.
jumlah kerugian yang dihasilkan ini dari 100
persen. Data yang dibutuhkan dalam penelitian b) Persentase excess air supplied (%EA):
ini meliputi analisis bahan bakar dan data
operasional boiler. (4)
oksigen dalam flue gas
Bahan bakar yang digunakan dalam penelitian
% EA=21 − oksigen dalam flue gas x 100
ini adalah ampas tebu (100%), campuran ampas c) Massa gas buang ke cerobong asap (mass
tebu (80%) dan sekam padi (20%), serta flue gas to exhaust chimney):
campuran ampas tebu (80%) dan cangkang
kelapa sawit (20%). Analisis bahan bakar yang
dilakukan meliputi uji nilai kalor, uji proksimat
Mfg= m CO2+ m N2 (dalam bb)+m N2 (dalam A(A5S))
dan uji ultimat. Adapun data operasional boiler +m O2 (dalam FG)
menggunakan data sekunder yang diambil dari Dengan:
data operasional boiler Pabrik Gula Trangkil M fg : massa gas buang (kg/kg bahan
milik PT Kebon Agung Grup yang berlokasi di bakar)
Pati Jawa Tengah saat masa giling pada tahun m CO 2 : massa gas CO 2
2020. bb : bahan bakar
m N : massa gas N
2 2
Data analisis nilai kalor, proksimat dan ultimat
AAS : actual air supplied (kg/kg
bahan bakar serta data operasional boiler
bahan bakar)
tersebut digunakan untuk mengukur kinerja
FG : flue gas
boiler menggunakan metode tidak langsung
atau metode pengukuran efisiensi
d) Kerugian panas dalam gas buang (L ):
1
keseimbangan panas berdasarkan standar
ASME PTC 4 Fire Steam Generators (ASME,
(6)
2008) yang disesuaikan pemakaiannya
𝑚 𝑥 𝐶𝑝 𝑥 (𝑇𝑓− 𝑇𝑎)
berdasarkan bahan bakar biomassa. Efisiensi D𝐿e1n=gan: 𝐺𝐶𝑉 𝑥 100
boiler dapat dinyatakan menggunakan m : massa gas buang kering (kg/kg
persamaan: bahan bakar)
C : kalor spesifik dari gas buang
 (1) p
kering (kCal/kg oC)
energi bahan bakar−kerugian energi
T : temperatur gas buang (oC)
At=au bisa deinneyrgait baakhaann bdaakalarm: x 100% f
T : temperatur ambient (oC)
a
 (2) GCV : nilai kalor biomassa (kCal/kg)
=(100−L1−L2−L3−L4) %

106 S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021
e) Kerugian panas karena kelembaban (H O) (L )
2 4
dan hidrogen (H ) dalam bahan bakar (L ):
2 2 Perhitungan kehilangan panas akibat karbon
yang tidak terbakar didasarkan pada kandungan
karbon dalam abu boiler, dengan asumsi bahwa
𝐿2=[ 𝑀 𝑥 [584 + 𝐺 𝐶 𝐶 𝑝 𝑉+ 𝑥 (𝑇𝑓 − 𝑇𝑎)] 𝑥 100] (7) abu boiler terdiri dari abu bahan bakar dan
karbon yang tidak terbakar. Secara umum perlu
dipertimbangkan bahwa bahan bakar padat
akan kehilangan panas karena adanya abu
9 𝑥 𝐻2 𝑥 [584 + 𝐶𝑝 𝑥 (𝑇𝑓− 𝑇𝑎)]
100 terbang (fly ash) dan abu dasar (bottom ash)
Deng[an: 𝐺𝐶𝑉 𝑥 ]
yang tidak terbakar.
M : massa kelembaban bahan
Kerugian radiasi/konveksi permukaan dan
bakar dalam setiap kilogram
kerugian lain yang tidak terhitung umumnya
bahan bakar
diasumsikan berdasarkan jenis dan ukuran
C : kalor spesifik uap kering
p boiler seperti yang diberikan di bawah ini
(0.47 kCal/kg oC)
(M.Raut, Kumbhare, & Thakur, 2014):
H : massa hidrogen dalam setiap
2
kilogram bahan bakar - Boiler industri pipa-pipa api (fire tube):
1,5% s.d. 2,5%
f) Kerugian karena kelembaban dalam udara
- Boiler industri pipa-pipa air (water tube):
(L ):
3 2% s.d. 3%
- Boiler pembangkit listrik: 0,4% s.d. 1%
(8)
Nilai kerugian karbon dalam abu yang tidak
𝐴𝐴𝑆 𝑥 ℎ𝑢𝑚𝑖𝑑𝑖𝑡𝑦 𝑥 𝐶𝑝 𝑥 (𝑇𝑓− 𝑇𝑎)
D𝐿3en=gan: 𝐺𝐶𝑉 𝑥 100 terbakar dan kerugian radiasi atau konveksi
pada permukaan serta kerugian-kerugian lain
C : kalor spesifik uap kering
p yang tidak dapat dihitung dalam penelitian ini
(0.47 kCal/kg oC)
dianggap memiliki nilai yang sama untuk
humidity : massa air dalam setiap
semua jenis bahan bakar yang digunakan.
kilogram udara
Karena kondisi temperatur dan kelembaban
lingkungan operasional boiler relatif sama, HASIL DAN PEMBAHASAN
maka dalam analisis efisiensi nilainya
dibuat konstan.
Hasil karakterisasi bahan bakar yang meliputi
g) Kerugian karbon dalam abu yang tidak analisa nilai kalor, proksimat, dan ultimat, abu
terbakar (unburnt carbon in ash) dan hasil pembakaran didapatkan sifat-sifat dasar
kerugian radiasi/konveksi pada permukaan bahan bakar yang ditunjukkan pada Tabel 1.
TABEL 1. Kandungan dan Komposisi Biomassa Ampas Tebu, Sekam Padi, dan Cangkang Kelapa Sawit
Satuan Ampas tebu & Ampas tebu &
Ampas Sekam Cangkang
Kandungan & sekam padi cangkang sawit
tebu padi sawit
Simbol (80% ; 20%) (80% : 20%)
GCV kCal/kg 2256 3248 3461 2554 2617
Uji proksimat:
- Moisture % adb 50.00 7.85 19.45 41.57 43.89
- Ash % adb 1.5 20.67 2.1 5.33 1.62
- Volatile % adb 36.9 57.96 50.9 41.11 39.7
12.5 13.52 27.45 12.70 15.49
- Fixed carbon % adb
Uji ultimat:
- Carbon C 23.5 35.7 40.65 27.2 28.6
- Hydrogen H 2.8 4.48 4.69 3.3 3.4
- Oxygen O 15.6 31.30 33.16 20.3 20.9
- Nitrogen N 6.60 0.00 0.00 4.6 4.6
- Sulphur S 0.03 0.05 0.07 0.034 0.038

S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021 107
Berdasarkan tabel 1, nilai kalor terendah boiler. Oleh karena itu perlu penyesuaian
dimiliki oleh ampas tebu sebesar 2256 kCal/kg, pengoperasian boiler pada saat menggunakan
lebih rendah dibandingkan nilai kalor sekam bahan bakar co-firing ampas tebu dengan sekam
padi sebesar 3248 kCal/kg dan nilai kalor padi.
cangkang sawit sebesar 3461 kCal/kg. Saat
Kandungan sulfur yang relatif kecil pada ampas
ampas tebu dicampur dengan sekam padi dan
tebu, sekam padi, dan cangkang sawit maupun
ampas tebu dicampur dengan cangkang sawit
campurannya menjadi suatu kelebihan dari
dengan perbandingan masing-masing sebesar
biomassa ini karena pada saat digunakan
(80%:20%), maka nilai kalornya berturut-turut
sebagai bahan bakar tidak memberikan dampak
berubah menjadi masing-masing 2554 kCal/kg
buruk terhadap lingkungan dalam pembentukan
dan 2617 kCal/kg. Hal ini menunjukkan bahwa
emisi gas NOx dan SOx (Baxter, 2005).
dengan model pembakaran co-firing ampas
tebu dan cangkang sawit dengan perbandingan Hasil pengambilan data sekunder operasional
80%:20%, dapat meningkatkan nilai kalor boiler Pabrik Gula Trangkil milik PT Kebon
bahan bakar sebesar 13% - 16%. Agung Grup yang berlokasi di Pati Jawa
Tengah saat masa giling pada tahun 2020 yang
Ampas tebu memiliki kadar kelembaban
digunakan sebagai acuan perhitungan kinerja
(moisture) yang paling tinggi (50%) apabila
boiler dapat dilihat pada Tabel 2.
dibandingkan dengan sekam padi (7.85%) dan
cangkang sawit (19.45%), oleh karena itu pada Data operasional boiler bersama data analisis
saat dilakukan pembakaran bersama dengan bahan bakar ampas tebu, sekam padi, dan
sekam padi atau cangkang sawit nilai cangkang sawit tersebut digunakan untuk
kelembabannya akan menurun sehingga menghitung kinerja boiler saat dioperasikan
memberikan dampak yang cukup baik untuk dengan bahan bakar tunggal ampas tebu, atau
kinerja pembakaran di boiler (Orang & Tran, saat menggunakan sistem pembakaran bersama
2015). Di sisi lain, sekam padi memiliki kadar (co-firing) berdasarkan metode tidak langsung
abu yang paling tinggi (20.67%) jika menggunakan bantuan analisis komputer
dibandingkan dengan kadar abu ampas tebu (FireCad WTPB 3.0), yang hasilnya seperti
(1.5%) dan cangkang sawit (2.1%), sehingga terlihat pada Tabel 3 dan Tabel 4.
dapat mempercepat penuhnya ruang bakar pada
TABEL 2. Data Rerata Operasional Boiler Pabrik Gula Trangkil Selama Musim Giling Tahun 2020
Parameter Nilai Satuan
Tekanan uap 21.6 Bar
Temperatur uap 327 oC
Aliran uap (steam flow) 50500 Kg/jam
Temperatur air 115 oC
Temperatur gas buang 150 oC
Temperatur lingkungan 33 oC
Oksigen dalam gas 5 %
TABEL 3. Jumlah Pemakaian Bahan Bakar, Kerugian Panas, Efisiensi, dan Kebutuhan Volume Dapur Boiler
Ampas tebu & Ampas tebu &
Satuan & Ampas tebu
sekam padi cangkang sawit
Simbol (100%)
(80%:20%) (80%:20%)
Fuel Consumption kg/jam 19415.46 17160.44 15961.11
Air Fuel Ratio (AFR) % 4.01 4.35 4.76
Gas Fuel Ratio (GFR) % 4.99 5.30 5.75
L % 4.89 5.02 5.15
1
L % 20.94 17.91 17.17
2
L % 0.12 0.12 0.12
3
L % 2.00 2 2
4
Boiler Efficiency % 72.05 74.95 75.56
Excess Air % 31 31 31
Furnace Volume m3 84.53 81.84 81.42
Furnace temperature oC 968.3 997.5 998.9

108 S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021
TABEL 4. Profil Gas Buang yang Melewati Beberapa Peralatan Penukar Panas (Heat Excanger/HE) di Boiler
Bahan bakar ampas (100%)
Pressure drop
Heat exchanger Temperatur (oC) Densitas (kg/m3) Kecepatan (m/s)
(mm kolom air)
Superheater 34.12 793.5 0.35 14.00
Boiler bank 317.79 331 0.58 33.10
Air heater 27.86 212 0.752 8.60
Economizer 34.57 140 0.87 8.90
Bahan bakar ampas (80%):sekam padi (20%)
Pressure drop
Heat exchanger Temperatur (oC) Densitas (kg/m3) Kecepatan (m/s)
(mm kolom air)
Superheater 30.65 809 0.32 13.84
Boiler bank 271.38 333 0.59 30.33
Air heater 26.85 214 0.76 8.41
Economizer 32.42 141 0.88 8.58
Bahan bakar ampas (80%):cangkang sawit (20%)
Pressure drop
Heat exchanger Temperatur (oC) Densitas (kg/m3) Kecepatan (m/s)
(mm kolom air)
Superheater 24.35 809 0.32 12.30
Boiler bank 225.38 335 0.60 27.40
Air heater 26.67 215 0.77 8.30
Economizer 32.30 142 0.88 8.60
Meskipun temperatur gas buang pada dapur kelapa sawit dapat menaikkan efisiensi boiler
boiler yang mengalir ke bagian heat exchanger dari 72.05% menjadi 75.56%, dan menurunkan
cenderung naik (Tabel 3 dan Tabel 4), tetapi jumlah konsumsi bahan bakar karena nilai kalor
kenaikannya masih dalam rentang operasional bahan bakar co-firing lebih tinggi dibandingkan
boiler berbasis biomassa dan masih memenuhi nilai kalor ampas tebu. Kebutuhan volume
standar operasional yang diacu. Selain itu ruang bakar (furnace) boiler juga mengalami
kenaikan temperatur gas buang pada dapur penurunan, hal ini disebabkan bahan bakar
boiler dan komponen heat exchanger masih ampas memiliki densitas rendah dan akan
dibawah titik leleh (melting point) abu bahan terbakar secara melayang di dalam rangka bakar
bakar tersebut yang berkisar pada temperatur boiler. Bahan bakar jenis ini sifatnya cenderung
1350o C (De Palma et al., 2019) (Horák et al., menumpuk sehingga membutuhkan volume
2019) (Fredericci et al., 2014) (Li et al., 2013). furnace yang lebih besar. Pemakaian bahan
Oleh karena itu co-firing ampas tebu dengan bakar secara co-firing dengan sekam padi dan
sekam padi maupun cangkang kelapa sawit cangkang kelapa sawit akan meningkatkan
cukup aman diaplikasikan pada boiler. densitas campuran dan akan mengurangi
volume furnace dari 84.53 m3 menjadi 81.42
Kerugian panas terbesar dalam sistem
m3. Hal ini disebabkan bahan bakar sekam padi
operasional boiler adalah kerugian akibat
dan cangkang sawit akan terbakar di atas rangka
kelembaban (moisture) yang terdapat dalam
bakar boiler.
bahan bakar (L ) diikuti oleh kerugian panas
2
yang terdapat dalam gas buang (L ). Kedua Tabel 4 menunjukkan bahwa kecepatan aliran
1
jenis kerugian ini memiliki peran utama dalam gas buang hasil pembakaran co-firing di bagian
menurunkan atau menaikkan efisiensi boiler. alat penukar panas (heat exchanger) boiler
Semakin rendah kandungan moisture dalam seperti superheater, boiler bank, air heater dan
bahan bakar dan semakin rendah temperatur gas economizer cenderung menurun berbanding
buang maka akan meningkatkan efisiensi boiler langsung dengan pressure drop dan berbanding
(Dzurenda & Banski, 2017). Pembakaran bahan terbalik dengan densitas gas. Hal ini berdampak
bakar biomassa pada tingkat kelembaban yang lebih baik yaitu menurunkan kemungkinan
sesuai sangat penting dari sudut pandang terjadinya erosi pipa boiler akibat benturan
kinerja boiler (Panchal et al., 2016). senyawa kotoran atau larutan padat yang terikut
dalam gas buang (Yang et al., 2009).
Pemakaian bahan bakar secara co-firing antara
ampas tebu dengan sekam padi atau cangkang Selama operasional boiler terlihat adanya

S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021 109
kecepatan gas buang yang mencapai 27.40 – sugarcane straw, and their pellets - Case
30.33 m/s di pipa-pipa utama penghasil uap di study of agro-industrial residues. Energy
sekitar drum atas boiler (boiler bank), sehingga and Fuels, 33(4), 3227–3238.
perlu perhatian khusus terkait pengaturan https://doi.org/10.1021/acs.energyfuels.8
kecepatan gas buang pada sistem IDF (induced b04288
draft fan) untuk mengurangi potensi erosi pipa-
Dzurenda, L., & Banski, A. (2017). Influence of
pipa boiler bank.
moisture content of combusted wood on
the thermal efficiency of a boiler.
Archives of Thermodynamics, 38(1), 63–
KESIMPULAN
74. https://doi.org/10.1515/aoter-2017-
0004
Berdasarkan hasil analisis yang ditemukan
Fauzan, M. R. (2020). Sinergi BUMN &
menunjukkan bahwa pemakaian bahan bakar
swasta, Perhutani kembangkan industri
co-firing antara ampas tebu dengan sekam padi
non-kayu. Retrieved from
dan cangkang kelapa sawit menunjukkan
https://www.wartaekonomi.co.id/read29
kecenderungan menurunkan kerugian panas
8975/sinergi-bumn-swasta-perhutani-
pada boiler, sehingga efisiensi boilernya akan
kembangkan-industri-non-kayu
meningkat, oleh karena itu aplikasi bahan bakar
co-firing dapat dilakukan di pabrik gula. Fredericci, C., Ett, G., Lenz e Silva, G. F. B.,
Substitusi bahan bakar sekam padi dan Neto, J. B. F., Landgraf, F. J. G.,
cangkang kelapa sawit sebesar 20% tidak akan Indelicato, R. L., & Ribeiro, T. R. (2014).
mengubah desain ruang bakar boiler, karena An analysis of Brazilian sugarcane
justru akan menurunkan volume ruang bakar bagasse ash behavior under thermal
boiler. Pemakaian bahan bakar co-firing dapat gasification. Chemical and Biological
meningkatkan temperatur furnace dari 968.3oC Technologies in Agriculture, 1(1), 1–9.
menjadi 998.9oC sehingga perlu diwaspadai https://doi.org/10.1186/s40538-014-
potensi terjadinya slagging dan fouling di dalam 0015-z
alat alat penukar panas boiler. Diperlukan
Horák, J., Kuboňová, L., Dej, M., Laciok, V.,
perhatian dalam operasional boiler terutama
Tomšejová, Š., Hopan, F., & Koloničný,
dari aspek erosi pipa boiler apabila terjadi
J. (2019). Effects of the type of biomass
slagging dan fouling dalam furnace karena
and ashing temperature on the properties
kecepatan aliran gas buang yang cukup besar.
of solid fuel ashes. Polish Journal of
Chemical Technology, 21(2), 43–51.
https://doi.org/10.2478/pjct-2019-0019
DAFTAR PUSTAKA
Kemenperin. (2021). Kemenperin jaga
ketersediaan bahan baku gula untuk
ASME. (2008). Fired steam generators
industri mamin. Retrieved from
performance test codes. New York, NY:
https://www.kemenperin.go.id/artikel/22
American Society of Mechanical
284/Kemenperin-Jaga-Ketersediaan-
Engineers.
Bahan-Baku-Gula-untuk-Industri-
Asosiasi Gula Indonesia. (2020). National sugar Mamin
summit 2020. Buletin AGI IKAGI Edisi 5,
Li, W., Li, Q., Zhang, Y., & Meng, A. (2013).
1–60.
Ashing temperature’s impact on the
Baxter, L. (2005). Biomass-coal co- characteristics of biomass ash. Applied
combustion: Opportunity for affordable Mechanics and Materials, 261–262, 217–
renewable energy. Fuel, 84(10), 1295– 223.
1302. https://doi.org/10.4028/www.scientific.n
https://doi.org/10.1016/j.fuel.2004.09.02 et/AMM.260-261.217
3
M.Raut, S., Kumbhare, S. B., & Thakur, K. C.
De Palma, K. R., García-Hernando, N., Silva, (2014). Energy performance assessment
M. A., Tomaz, E., & Soria-Verdugo, A. of boiler at P.S.S.K. Ltd, Basmathnagar,
(2019). Pyrolysis and combustion kinetic Maharashtra State. International Journal
study and complementary study of ash of Emerging Technology and Advanced
fusibility behavior of sugarcane bagasse, Engineering, 4(12), 1–12.

110 S. Harnowo & Yunaidi/Semesta Teknika, Vol. 24, No. 2, 102-110, November 2021
McIntyre, P. (2013). Case studies of biomass co Wang, X., Rahman, Z. U., Lv, Z., Zhu, Y.,
firing. FFF OIB Workshop, John Ruan, R., Deng, S., … Tan, H. (2021).
Thompson Boiler and Environmental Experimental study and design of
Solution, (September), 2013. biomass co-firing in a full-scale coal-
fired furnace with storage pulverizing
Nasution, D. D. (2021a). Kementan: Lahan tebu
system. Agronomy, 11(4), 1–11.
terus berkurang, daya saing menurun.
https://doi.org/10.3390/AGRONOMY11
Retrieved from
040810
https://republika.co.id/berita/qkal0w370/
kementan-lahan-tebu-terus-berkurang- Yang, H., Zhang, H., Yang, S., Yue, G., Su, J.,
daya-saing-menurun & Fu, Z. (2009). Effect of bed pressure
drop on performance of a CFB boiler.
Nasution, D. D. (2021b). Produksi gula 2020
Energy and Fuels, 23(6), 2886–2890.
capai 2,13 juta ton. Retrieved April 28,
https://doi.org/10.1021/ef900025h
2021, from
https://republika.co.id/berita/qmgl6w370 Yunaidi, Surahmanto, F., & Harnowo, S.
/produksi-gula-2020-capai-213-juta-ton (2020). The risk analysis of rice husk of
co-firing fuel for boilers in sugar mills.
Naude, D. P. (2001). Combustion of bagasse &
Journal of Physics: Conference Series,
woodwaste in boilers for integration into
1446(1). https://doi.org/10.1088/1742-
a cogeneration steam cycle. In
6596/1446/1/012041
Proceedings of the 2001 Conference of
the Australian Society of Sugar Cane
PENULIS:
Technologists held at Mackay,
Queensland, Australia (p. pp.384-389
Saptyaji Harnowo
ref.4).
Program Studi Teknologi Mesin, Politeknik
Ninduangdee, P., & Kuprianov, V. I. (2018).
LPP. Jl. Urip Sumoharjo No.1, Klitren,
Co-combustion of rice husk pellets and
Gondokusuman, Yogyakarta.
moisturized rice husk in a fluidized-bed
combustor using fuel staging at a Email: saptyaji.lpp@gmail.com
conventional air supply. Songklanakarin
Journal of Science and Technology.
Yunaidi
https://doi.org/10.14456/sjst-
psu.2018.134 Program Studi Teknologi Mesin, Politeknik
LPP. Jl. Urip Sumoharjo No.1, Klitren,
Orang, N., & Tran, H. (2015). Effect of
Gondokusuman, Yogyakarta.
feedstock moisture content on biomass
boiler operation. TAPPI Journal, 14(10), Email: ynd@polteklpp.ac.id
629-636.
P3GI. (2016). Laporan audit pabrik gula PTPN
IX tahun 2016. Surakarta.
Panchal, R., Shinde, S., & Panchal, S. (2016).
Effect of Bagasse Moisture on Boiler
Performance. International Research
Journal of Multidisciplinary Studies,
2(1), 1–8.
Patel, D. T., & Modi, K. V. (2016).
Performance evaluation of industrial
boiler by heat loss method ., 2(3), 2081–
2088. Retrieved from
http://ijariie.com/AdminUploadPdf/Perf
ormance_evaluation_of_industrial_boile
r_by_heat_loss_method__ijariie2348.pdf
Rein, P. (2016). Cane Sugar Engineering 2nd
edition. Verlag Dr. Albert Bartens KG.
