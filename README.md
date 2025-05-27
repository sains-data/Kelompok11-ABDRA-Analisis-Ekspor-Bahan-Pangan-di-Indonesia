========

# **📊🌾📦 PEMANFAATAN EKOSISTEM HADOOP UNTUK ANALISIS DATA EKSPOR BAHAN PANGAN DI INDONESIA 📦🌾📊**

Selamat datang di repositori proyek analisis big data untuk menganalisis dan mengoptimalkan data ekspor bahan pangan di Indonesia!

Proyek ini bertujuan untuk memanfaatkan kekuatan ekosistem Hadoop, Apache Spark, dan teknik machine learning untuk memberikan wawasan mendalam terkait volume, nilai, dan tren ekspor bahan pangan Indonesia secara akurat dan sistematis.

Dengan data ekspor bahan pangan yang sangat besar dan kompleks, pendekatan big data ini memungkinkan pengolahan dan analisis data secara efisien serta prediksi tren yang berguna bagi para pemangku kepentingan di bidang perdagangan dan kebijakan pangan.

---

### 📝 Latar Belakang Masalah

<p align="justify">
Ekspor bahan pangan merupakan sektor vital dalam perekonomian Indonesia yang berkontribusi signifikan terhadap pendapatan negara dan kesejahteraan petani. Namun, volume dan nilai ekspor yang sangat besar serta kompleksitas data dari berbagai provinsi dan komoditas memerlukan pengolahan dan analisis yang cermat agar dapat dioptimalkan secara efektif. Data ekspor bahan pangan yang terdistribusi dalam jumlah besar dan beragam format menimbulkan tantangan besar dalam pengelolaan dan analisis menggunakan metode konvensional.
</p>

<p align="justify">
Pemanfaatan ekosistem Hadoop menawarkan solusi komprehensif untuk menangani data besar ini melalui penyimpanan terdistribusi dan pemrosesan paralel. Dengan mengintegrasikan Hadoop bersama teknologi Apache Spark dan machine learning, proses analisis data ekspor bahan pangan dapat dilakukan dengan lebih cepat, akurat, dan skalabel. Pendekatan ini diharapkan dapat menghasilkan insight yang mendalam terkait tren ekspor, potensi pasar, serta faktor-faktor yang mempengaruhi performa ekspor bahan pangan di Indonesia.
</p>

<p align="justify">
Oleh karena itu, proyek ini bertujuan untuk mengimplementasikan dan menguji efektivitas ekosistem Hadoop dalam analisis data ekspor bahan pangan, sehingga memberikan kontribusi positif terhadap pengambilan keputusan strategis di sektor perdagangan dan pertanian nasional.
</p>

---

### 🎯 Tujuan Proyek  
Dokumen ini bertujuan menjelaskan perancangan dan implementasi ekosistem Apache Hadoop untuk analisis data ekspor bahan pangan di Indonesia.

Fokus utama meliputi:

- Mengimplementasikan ekosistem Apache Hadoop untuk mengoptimalkan pengolahan data ekspor bahan pangan yang besar dan kompleks.  
- Membangun pipeline data yang efisien untuk proses ingestion, penyimpanan, dan transformasi data ekspor.  
- Memberikan insight strategis melalui analisis dan visualisasi data guna mendukung pengambilan keputusan di sektor pertanian dan perdagangan Indonesia.

---

### 🛠️ Lingkup Sistem  
Sistem ini dirancang untuk memproses, membersihkan, dan menganalisis data ekspor bahan pangan Indonesia skala besar menggunakan ekosistem Apache Hadoop dan teknologi pendukungnya.

Lingkupnya mencakup:

📥 Akuisisi & Penyimpanan Awal:  
Pengambilan data ekspor bahan pangan mentah dari berbagai sumber resmi menggunakan Bash Script, API, dan curl, lalu disimpan secara terdistribusi di HDFS (Bronze Layer) dalam format CSV/JSON/TSV.

✨ Pembersihan & Transformasi:  
Pengolahan data mentah menggunakan Apache Spark dan Hive SQL untuk pembersihan data (validasi format, penanganan missing value, normalisasi), serta konversi ke format kolumnar efisien Parquet/ORC (Silver Layer).

🥇 Agregasi dan Pengolahan Lanjutan:  
Melakukan agregasi statistik ekspor (volume, nilai) per bulan, negara tujuan, dan provinsi asal menggunakan Spark SQL dan Hive untuk kebutuhan analitik dan pelaporan (Gold Layer).

🔍 Query dan Analitik:  
Menyediakan kemampuan kueri data menggunakan Apache Hive dengan SQL interface yang mudah diintegrasikan ke berbagai tools analitik dan BI.

🗄️ Penyimpanan Data Real-Time:  
Subset data tertentu disimpan di Apache HBase untuk akses cepat dan real-time sesuai kebutuhan analisis spesifik.

📊 Visualisasi Dashboard:  
Hasil analisis dan insight disajikan melalui dashboard interaktif menggunakan Apache Superset dan Jupyter Notebook.

🐳 Pengembangan dan Deployment Lokal:  

Arsitektur data mengikuti pendekatan Medallion Architecture dengan pemisahan data pada Bronze, Silver, dan Gold Layer untuk efisiensi dan manajemen kualitas data secara sistematis.

---

### 📊 Dataset yang Digunakan  
Proyek ini menggunakan data ekspor beras tahun 2024 yang didapatkan dari situs resmi pertanian.go.id. Data tersebut berisi informasi penting terkait volume dan nilai ekspor beras dari berbagai provinsi di Indonesia setiap bulannya.

Data ini terdiri dari kolom-kolom utama sebagai berikut:

| Provinsi  | Bulan    | Volume (Kg) | Nilai (US$) |
|-----------|----------|-------------|-------------|
| Teks     | Teks     | Numerik     | Numerik     |

Penjelasan kolom:

- **Provinsi**: Nama provinsi asal bahan pangan yang diekspor.  
- **Bulan**: Bulan pengiriman ekspor, dalam format teks (misal Januari, Februari, dst).  
- **Volume (Kg)**: Total volume ekspor dalam kilogram untuk bulan dan provinsi tersebut.  
- **Nilai (US$)**: Total nilai ekspor dalam dolar Amerika Serikat pada bulan dan provinsi tersebut.

Data ini menjadi dasar utama untuk analisis volume dan nilai ekspor beras di Indonesia sepanjang tahun 2024, yang selanjutnya diolah menggunakan ekosistem Hadoop dan Apache Spark untuk memberikan insight strategis.

---

### 🧱 Arsitektur Sistem  
Sistem ini mengadopsi Medallion Architecture dengan pendekatan batch processing dan data lake untuk pengelolaan data ekspor bahan pangan.

- **Bronze Layer**:  
  Menyimpan data mentah (raw) langsung dari sumber eksternal tanpa transformasi. Data diambil menggunakan Bash Script, curl, atau API, lalu disimpan di HDFS dalam format CSV, JSON, atau TSV. Tujuan utama adalah sebagai arsip permanen data asli.

- **Silver Layer**:  
  Data yang telah dibersihkan dan diproses seperti parsing tanggal, penanganan nilai null, validasi skema, dan normalisasi format. Proses ini menggunakan Apache Hive dan Spark SQL dengan format Parquet atau ORC. Data di layer ini siap digunakan untuk query analitik, laporan, visualisasi, dan pelatihan machine learning (ML).

- **Gold Layer**:  
  Data yang telah diolah dan digabungkan melalui agregasi volume ekspor, harga, dan ringkasan statistik penting. Pengolahan dilakukan menggunakan Apache Hive dan Spark SQL dengan format Parquet/ORC. Data ini siap untuk query analitik tingkat lanjut, pembuatan laporan, visualisasi, serta aplikasi machine learning.

[Bronze Layer (HDFS)] --> [Silver Layer (Hive/Spark)] --> [Gold Layer (Hive/Spark)] --> [Analytics/Dashboard (Looker Studio)]

--- 

### 🔧 Teknologi yang Digunakan
Dalam proyek ini, beberapa teknologi utama dari ekosistem Big Data dan Hadoop digunakan untuk membangun sistem analisis data ekspor bahan pangan Indonesia, antara lain:

- Hadoop HDFS: Sistem penyimpanan terdistribusi yang menyimpan data besar secara efisien dalam berbagai layer (Bronze, Silver, Gold).

- Apache Spark: Framework pemrosesan data cepat untuk pembersihan, transformasi, dan agregasi data menggunakan PySpark.

- Apache Hive: Penyedia SQL interface untuk query dan analitik data di data lake.

- Apache HBase: Database NoSQL untuk akses data real-time berbasis key-value.

- Apache Ambari: Alat monitoring dan manajemen cluster Hadoop untuk memastikan performa dan ketersediaan layanan.

- Apache Superset: Platform dashboard interaktif untuk visualisasi hasil analisis data.

- Docker & Docker Compose: Virtualisasi layanan Hadoop dan komponen pendukung agar mudah dikelola dan di-deploy secara lokal maupun skala besar.

- WSL2 (Windows Subsystem for Linux 2): Lingkungan Linux di Windows untuk menjalankan Docker dan Hadoop secara stabil.

- Bash Script & Crontab: Otomatisasi pengambilan dan penjadwalan data ingestion dari sumber resmi.

- MobaXterm: Untuk aplikasi terminal yang serbaguna untuk pengguna Windows, yang memungkinkan akses jarak jauh ke server berbasis Unix/Linux, menjalankan aplikasi GUI dari server, serta transfer file melalui SFTP atau SCP

- Visual Studio Code (VSCode): Integrated Development Environment (IDE) untuk pengembangan dan debugging skrip PySpark.

--- 

### 📋 Metodologi Proyek (Model Waterfall)

Proyek ini menggunakan pendekatan Waterfall yang terdiri dari tahapan-tahapan berurutan dan sistematis untuk memastikan implementasi yang terstruktur dan terkontrol. Berikut tahapan utama yang diterapkan:

1. Analisis Kebutuhan (Requirement Analysis)
   Memahami permasalahan utama terkait pemanfaatan data ekspor bahan pangan yang tersebar dan berformat tidak seragam. Mengidentifikasi stakeholder utama seperti Kementerian Pertanian, BPS, eksportir, dan analis data perdagangan. Mendefinisikan output yang diharapkan seperti statistik volume dan nilai ekspor, tren harga, serta visualisasi data.

2. Perancangan Sistem (System Design)
   Merancang arsitektur sistem berbasis Medallion Architecture dengan tiga lapisan utama: Bronze (data mentah), Silver (data bersih dan terstruktur), dan Gold (data agregasi dan analitik). Mendesain infrastruktur klaster Hadoop lokal menggunakan Docker dan WSL2 serta mendefinisikan pipeline batch processing data.

3. Implementasi (Implementation)
   Membangun sistem di lingkungan Docker dengan menjalankan layanan Hadoop, Spark, Hive, dan HBase. Mengembangkan skrip ETL untuk ingestion, pembersihan, transformasi, dan agregasi data menggunakan PySpark dan Bash Script. Mengatur orkestrasi pipeline batch secara berkala.

4. Pengujian (Testing)
   Melakukan pengujian unit, integrasi, performa, dan end-to-end untuk memastikan pipeline data berjalan lancar, akurat, dan dapat diandalkan. Memeriksa kualitas data dan validasi proses transformasi serta query analitik.

5. Analitik dan Visualisasi (Analytics & Visualization)
   Melakukan analisis lanjutan menggunakan Apache Spark MLlib untuk prediksi dan clustering data ekspor. Menyajikan hasil analitik melalui dashboard interaktif menggunakan Apache Superset dan Jupyter Notebook.

6. Deployment dan Monitoring
   Menyiapkan deployment sistem secara lokal dengan Docker dan mengelola monitoring cluster menggunakan Apache Ambari untuk memastikan ketersediaan dan performa layanan.

Model Waterfall ini memberikan kerangka kerja yang jelas untuk pengembangan dan pengelolaan proyek secara sistematis dari tahap awal hingga hasil akhir, memastikan kualitas dan keberhasilan implementasi.

---

### 🧪 Kajian Analitik & Fitur Unggulan Proyek

Berikut adalah sorotan kajian analitik dan fitur unggulan yang menjadi inti dari kontribusi proyek ini dalam mengelola dan menganalisis data ekspor bahan pangan di Indonesia:

1. 🎯 **Analisis Agregasi Data Ekspor:**

   - Penghitungan total volume dan nilai ekspor per provinsi dan bulan secara akurat.
   - Analisis tren ekspor bahan pangan sepanjang tahun 2024.
   - Visualisasi ringkasan ekspor untuk mendukung pengambilan keputusan.

2. 🔍 **Arsitektur Medallion Layer untuk Data Lake:**

   - Pemisahan data pada Bronze (raw), Silver (bersih), dan Gold (agregasi) Layer.
   - Optimalisasi penyimpanan dan pemrosesan data menggunakan format Parquet dan ORC.
   - Efisiensi pipeline batch processing dengan integrasi Hadoop dan Spark.

3. ⚙️ **Integrasi Ekosistem Hadoop yang Komprehensif:**

   - Penggunaan HDFS, Apache Spark, Hive, dan HBase untuk manajemen data besar.
   - Automasi pipeline data menggunakan Bash Script dan scheduling Crontab.
   - Pengelolaan metadata dan query data melalui Hive Metastore.

4. 📊 **Dashboard Interaktif Visualisasi Data (Apache Superset):**

   - Penyajian data ekspor dalam dashboard yang mudah dipahami.
   - Dukungan eksplorasi data interaktif untuk pemangku kepentingan.
   - Visualisasi tren ekspor dan perbandingan antar provinsi dan bulan.

5. 🚀 **Lingkungan Pengembangan dan Deployment yang Portabel:**

   - Implementasi cluster Hadoop pseudo-distributed menggunakan Docker dan WSL2.
   - Kemudahan pengembangan skrip PySpark dengan Visual Studio Code.
   - Monitoring cluster dan performa menggunakan Apache Ambari.

6. 🤖 **Pengembangan Model Machine Learning untuk Prediksi:**

   - Penerapan regresi linear untuk prediksi volume ekspor di masa depan.
   - Analisis faktor yang mempengaruhi fluktuasi ekspor.
   - Penyimpanan model dan integrasi hasil prediksi ke dalam pipeline analitik.

---

### 📂 Struktur Repositori
```
bigdata_expor_pangan_indonesia/
│
├── 📄 00_documentation/
│   ├── 📝 proposal/
│   │   └── proposal_penelitian.pdf
│   ├── 📚 laporan_akhir/
│   │   └── laporan_akhir.pdf
│   └── 🎤 presentasi/
│       └── presentasi_proyek.pptx
│
├── 📥 01_data_acquisition/
│   ├── 💾 bronze_raw_data/
│   │   ├── Book1.csv
│   │   └── README.md
│   ├── 📜 ingestion_scripts/
│   │   ├── ingest.sh
│   │   └── README.md
│
├── 🛠️ 02_infrastructure_setup/
│   ├── 🐳 docker_configs/
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   ├── ⚙️ config_files/
│   │   ├── core-site.xml
│   │   ├── hdfs-site.xml
│   │   ├── hive-site.xml
│   │   └── hbase-site.xml
│   ├── 🚢 cluster_start_stop_scripts/
│   │   ├── start.sh
│   │   ├── stop.sh
│   │   └── build.sh
│
├── 🔄 03_data_processing_pipeline/
│   ├── ✨ etl_spark_scripts/
│   │   ├── etl_spark.py
│   │   ├── analisis_volume.py
│   │   ├── linear_regression_model.py
│   │   └── README.md
│
├── 📊 04_exploratory_analysis_and_visualization/
│   ├── notebooks/
│   │   ├── eksplorasi_data.ipynb
│   │   ├── visualisasi_ekspor.ipynb
│   │   └── README.md
│   ├── dashboard_Looker Studio/
│   │   └── konfigurasi_Looker Studio/
│
├── 🧠 05_machine_learning_models/
│   ├── model_training_scripts/
│   │   ├── train_regression.py
│   │   └── README.md
│   ├── saved_models/
│
├── 📁 06_logs/
│   └── pipeline_logs/
│
├── 📦 07_dependencies_and_binaries/
│   ├── apache-hadoop/
│   │   ├── apache-hive-4.0.1-bin.tar.gz
│   │   ├── apache-tez-0.10.4-bin.tar.gz
│   │   ├── apache-zookeeper-3.8.4-bin.tar.gz
│   │   ├── hadoop-3.4.1.tar.gz
│   │   ├── hbase-2.5.11-bin.tar.gz
│   │   └── mysql-connector-java-8.0.28.jar
│
├── .gitignore
├── LICENSE
└── README.md
```
---

### ⚙️ Panduan Singkat Instalasi dan Pengaturan Sistem

1. **Persiapan Lingkungan**  
   - Gunakan Windows 10/11 dengan WSL2 (Ubuntu 22.04)  
   - Instal Docker Desktop dan aktifkan integrasi WSL2  
   - Siapkan Visual Studio Code untuk pengembangan (opsional)

2. **Clone Repository**  
   Clone repository proyek dan masuk ke folder proyek.

3. **Build dan Jalankan Cluster**  
   Gunakan Docker Compose untuk membangun dan menjalankan layanan Hadoop, Spark, Hive, HBase, dan Superset secara lokal.

4. **Ingestion Data (Bronze Layer)**  
   Jalankan skrip ingestion untuk mengambil data ekspor bahan pangan dari sumber resmi dan upload ke HDFS.

5. **ETL dan Transformasi Data (Silver Layer)**  
   Jalankan job Apache Spark untuk pembersihan data dan konversi format ke Parquet.

6. **Agregasi dan Analitik Data (Gold Layer)**  
   Jalankan skrip agregasi data ekspor menggunakan Spark SQL dan Hive.

7. **Visualisasi Data**  
   Menggunakan Visualisasi data Looker Studio untuk membuat visualisasi

8. **Monitoring dan Pengelolaan Cluster**  
   Gunakan Apache Ambari untuk memonitor status cluster dan cek log pipeline di direktori logs.

9. **Deployment dan Pemeliharaan**  
   Sistem dapat dipindahkan ke host atau VM lain dengan Docker Compose.  
   Pipeline batch bisa dijadwalkan dengan cron job atau Apache Airflow.  
   Lakukan backup data dan konfigurasi secara berkala.

10. **Catatan Penting**  
    - Sistem mendukung akses berbasis peran (role-based access control).  
    - Data disimpan dalam format efisien untuk menghemat storage.  
    - Sistem dirancang scalable dan high availability.

---

### 📊 Hasil dan Pembahasan

1. Hasil Analisis Data Volume dan Nilai Ekspor Berdasarkan Bulan

Data ekspor bahan pangan selama tahun 2024 menunjukkan variasi yang signifikan pada volume dan nilai ekspor antar bulan. Bulan **April** mencatat volume ekspor tertinggi, yaitu sebesar **425.000 kg**, dengan nilai ekspor mencapai **240.000 USD**. Hal ini menandakan bahwa April merupakan periode puncak ekspor bahan pangan.

Sebaliknya, pada bulan **November, Januari, dan Agustus** tercatat volume dan nilai ekspor yang sangat rendah bahkan mencapai **0**, kemungkinan disebabkan oleh faktor musiman atau kebijakan perdagangan yang mempengaruhi ekspor.

Bulan **Oktober, Juli, dan Juni** juga menunjukkan volume ekspor yang cukup besar berturut-turut sebesar **19.143 kg, 17.495 kg, dan 2.683 kg**, dengan nilai ekspor sekitar **36.394 USD, 22.136 USD, dan 10.767 USD**. Fluktuasi ini mengindikasikan pengaruh permintaan pasar, musim panen, dan ketersediaan bahan pangan terhadap pola ekspor.

 2. Hasil Analisis Data Volume dan Nilai Ekspor Berdasarkan Provinsi

Distribusi volume dan nilai ekspor menurut provinsi menunjukkan dominasi Provinsi **DKI Jakarta**, dengan volume ekspor mencapai **435.690 kg** dan nilai ekspor sebesar **262.281 USD**. Hal ini mengindikasikan peran penting Jakarta sebagai pusat ekspor bahan pangan di Indonesia.

Provinsi lain seperti **Jawa Tengah** juga memberikan kontribusi signifikan dengan volume ekspor sekitar **31.308 kg** dan nilai ekspor sebesar **55.807 USD**.

Sementara itu, provinsi dengan volume dan nilai ekspor yang relatif kecil seperti **Kalimantan Barat, Nusa Tenggara Timur, dan Jawa Timur** menunjukkan potensi ekspor yang masih terbatas.  
- **Kalimantan Barat:** Volume ekspor 200 kg, nilai ekspor 153.6 USD  
- **Nusa Tenggara Timur:** Volume ekspor 50 kg, nilai ekspor rendah  
- **Jawa Timur:** Volume ekspor 6.88 kg, nilai ekspor relatif kecil

#### Kesimpulan

Data ini menunjukkan adanya variasi musiman dan regional dalam volume serta nilai ekspor bahan pangan di Indonesia. Provinsi-provinsi dengan kapasitas ekspor besar dapat menjadi fokus pengembangan lebih lanjut, sementara provinsi dengan kontribusi kecil berpotensi dikembangkan untuk meningkatkan performa ekspor nasional.

---

# 🧑‍💻 Tim Pengembang Proyek Sistem Analisis Data Ekspor Bahan Pangan Indonesia

Proyek ini merupakan hasil kolaborasi dan dedikasi dari tim mahasiswa Program Studi Psikologi. Setiap anggota tim berkontribusi secara signifikan sesuai keahlian dan tanggung jawabnya:

---

### 💡 Abit Ahmad Oktarian (122450042)  
**Fokus Utama:** Engineering & Pengembangan Kode  
**Kontribusi:**  
Memimpin pengembangan pipeline ETL menggunakan Apache Spark dan PySpark, implementasi skrip batch processing untuk Bronze, Silver, dan Gold Layer, serta optimasi kode dan konfigurasi Docker untuk menjalankan cluster Hadoop secara lokal. Bertanggung jawab atas pengelolaan dependensi dan debugging sistem.

---

### 💡 Arafi Ramadhan Maulana (122450002)
**Fokus Utama:** Akuisisi Data & Pengolahan Awal  
**Kontribusi:**  
Mengembangkan skrip ingestion data ekspor dari sumber resmi, validasi data mentah, dan manajemen penyimpanan data di Bronze Layer (HDFS). Melakukan proses pembersihan awal dan transformasi data ke Silver Layer serta memastikan integritas data untuk analisis lebih lanjut.

---

### 💡 Nurul Alfajar Gumel (122450127)  
**Fokus Utama:** Analisis Data & Agregasi  
**Kontribusi:**  
Melakukan analisis volume dan nilai ekspor berdasarkan provinsi dan bulan menggunakan Spark SQL dan Hive, serta pengembangan skrip agregasi untuk Gold Layer. Membantu pembuatan visualisasi dan dashboard data menggunakan Apache Superset dan Jupyter Notebook.

---

### 💡 Renisha Putri Giani (122450079)  
**Fokus Utama:** Dokumentasi, Pengujian & Visualisasi  
**Kontribusi:**  
Menyusun dokumentasi teknis proyek, mengelola proses pengujian pipeline mulai dari ingestion hingga visualisasi, dan mengembangkan dashboard interaktif di Apache Superset. Bertanggung jawab memastikan kualitas dan validitas hasil analitik.

---

## Pembimbing

👨‍🏫 Ardika Satria, S.Si., M.Si 
Dosen Pembimbing Mata Kuliah Big Data, Program Studi Sains Data, ITERA.

Terima kasih atas kerja sama dan kontribusi seluruh anggota tim.
---

# 🙏 Kutipan Singkat

Terima kasih banyak buat semua yang sudah bantu dan dukung proyek ini sampai selesai.  
Untuk dosen pembimbing, teman-teman tim, dan keluarga yang selalu kasih semangat—kalian keren banget!

Semoga hasil kerja kita ini bisa bermanfaat dan jadi langkah kecil buat kemajuan ekspor bahan pangan di Indonesia.




