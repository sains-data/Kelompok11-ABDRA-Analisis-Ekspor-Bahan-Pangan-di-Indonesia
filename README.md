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

🛠️ Lingkup Sistem  
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

