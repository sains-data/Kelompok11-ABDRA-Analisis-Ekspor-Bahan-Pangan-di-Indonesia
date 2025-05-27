from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Inisiasi SparkSession
spark = SparkSession.builder.appName("LinearRegressionModel").getOrCreate()

# Load dataset CSV
df = spark.read.csv("/tmp/Book1.csv", header=True, inferSchema=True)

# Pilih fitur dan label
assembler = VectorAssembler(inputCols=["Volume (Kg)"], outputCol="features")
data = assembler.transform(df).select("features", "Nilai (US$)").withColumnRenamed("Nilai (US$)", "label").na.drop()

# Split data train-test
train, test = data.randomSplit([0.8, 0.2], seed=42)

# Inisiasi model Linear Regression
lr = LinearRegression(featuresCol="features", labelCol="label", maxIter=10, regParam=0.3, elasticNetParam=0.8)

# Latih model
model = lr.fit(train)

# Prediksi test set
predictions = model.transform(test)

# Tampilkan hasil prediksi
predictions.select("features", "label", "prediction").show(10)

# Evaluasi model
trainingSummary = model.summary
print(f"RMSE: {trainingSummary.rootMeanSquaredError}")
print(f"R2: {trainingSummary.r2}")

spark.stop()
