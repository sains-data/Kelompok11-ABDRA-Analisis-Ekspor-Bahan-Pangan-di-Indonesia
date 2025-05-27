from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum

# Inisialisasi Spark
spark = SparkSession.builder.appName("AnalisisVolumePerProvinsi").getOrCreate()

# Baca data CSV
df = spark.read.option("header", "true").option("inferSchema", "true").csv("/tmp/Book1.csv")

# Cek schema
df.printSchema()

# Agregasi total volume dan nilai per provinsi
hasilProvinsi = df.groupBy("Provinsi").agg(
    spark_sum("Volume (Kg)").alias("Total_Volume_Kg"),
    spark_sum("Nilai (US$)").alias("Total_Nilai_USD")
)

# Tampilkan hasilnya
hasilProvinsi.orderBy("Total_Volume_Kg", ascending=False).show()

# Agregasi total volume dan nilai per bulan
hasilBulan = df.groupBy("Bulan").agg(
    spark_sum("Volume (Kg)").alias("Total_Volume_Kg"),
    spark_sum("Nilai (US$)").alias("Total_Nilai_USD")
)

# Tampilkan hasilnya
hasilBulan.orderBy("Total_Volume_Kg", ascending=False).show()

spark.stop()
