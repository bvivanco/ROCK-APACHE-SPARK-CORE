from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == '__main__':
    spark = SparkSession.builder.appName('TIME').getOrCreate()
    # spark.conf.set("spark.executor.memory", '8g')
    # spark.conf.set('spark.executor.cores', '3')
    # spark.conf.set('spark.cores.max', '3')
    # spark.conf.set("spark.driver.memory", '8g')
    sc = spark.sparkContext

    inputData = [("2019-07-01 12:01:19",
                  "07-01-2019 12:01:19",
                  "07-01-2019")]
    columns = ["timestamp_1", "timestamp_2", "timestamp_3"]
    df = spark.createDataFrame(
        data=inputData,
        schema=columns)
    df.printSchema()
    df.show(truncate=False)

    from pyspark.sql.functions import *

    df2 = df.select(
        unix_timestamp(col("timestamp_1")).alias("timestamp_1"),
        unix_timestamp(col("timestamp_2"), "MM-dd-yyyy HH:mm:ss").alias("timestamp_2"),
        unix_timestamp(col("timestamp_3"), "MM-dd-yyyy").alias("timestamp_3"),
        unix_timestamp().alias("timestamp_4")
    )
    df2.printSchema()
    df2.show(truncate=False)

    df3 = df2.select(
        from_unixtime(col("timestamp_1")).alias("timestamp_1"),
        from_unixtime(col("timestamp_2"), "MM-dd-yyyy HH:mm:ss").alias("timestamp_2"),
        from_unixtime(col("timestamp_3"), "MM-dd-yyyy").alias("timestamp_3"),
        from_unixtime(col("timestamp_4")).alias("timestamp_4")
    )
    df3.printSchema()
    df3.show(truncate=False)

    spark.stop()
