Unlike pandas, spark doesnt try to store the datatypes of the columns in the dataframe. It just stores the data as a binary format. So, when we read the data, we need to specify the schema of the data. This is done by using the StructType and StructField classes. The StructType class is used to define the schema of the dataframe. The StructField class is used to define the schema of each column of the dataframe. The StructField class takes in the following parameters:
- name: The name of the column
- dataType: The datatype of the column
- nullable: Whether the column can contain null values or not
- metadata: Any additional information about the column

```python
data.schema
```

```text
StructType([StructField('VendorID', IntegerType(), True),
            StructField('tpep_pickup_datetime', TimestampNTZType(), True),
            StructField('tpep_dropoff_datetime', TimestampNTZType(), True),
            StructField('passenger_count', LongType(), True),
            StructField('trip_distance', DoubleType(), True),
            StructField('RatecodeID', LongType(), True),
            StructField('store_and_fwd_flag', StringType(), True),
            StructField('PULocationID', IntegerType(), True),
            StructField('DOLocationID', IntegerType(), True),
            StructField('payment_type', LongType(), True),
            StructField('fare_amount', DoubleType(), True),
            StructField('extra', DoubleType(), True),
            StructField('mta_tax', DoubleType(), True),
            StructField('tip_amount', DoubleType(), True),
            StructField('tolls_amount', DoubleType(), True),
            StructField('improvement_surcharge', DoubleType(), True),
            StructField('total_amount', DoubleType(), True),
            StructField('congestion_surcharge', DoubleType(), True),
            StructField('Airport_fee', DoubleType(), True)
])
```

```python
from pyspark.sql import types

schema = types.StructType([
            types.StructField('VendorID', types.IntegerType(), True),
            types.StructField('tpep_pickup_datetime', types.TimestampType(), True),
            types.StructField('tpep_dropoff_datetime', types.TimestampType(), True),
            types.StructField('passenger_count', types.IntegerType(), True),
            types.StructField('trip_distance', types.DoubleType(), True),
            types.StructField('RatecodeID', types.IntegerType(), True),
            types.StructField('store_and_fwd_flag', types.StringType(), True),
            types.StructField('PULocationID', types.IntegerType(), True),
            types.StructField('DOLocationID', types.IntegerType(), True),
            types.StructField('payment_type', types.IntegerType(), True),
            types.StructField('fare_amount', types.DoubleType(), True),
            types.StructField('extra', types.DoubleType(), True),
            types.StructField('mta_tax', types.DoubleType(), True),
            types.StructField('tip_amount', types.DoubleType(), True),
            types.StructField('tolls_amount', types.DoubleType(), True),
            types.StructField('improvement_surcharge', types.DoubleType(), True),
            types.StructField('total_amount', types.DoubleType(), True),
            types.StructField('congestion_surcharge', types.DoubleType(), True),
            types.StructField('Airport_fee', types.DoubleType(), True)
])
```
```python
data = spark.read.parquet("yellow_tripdata_2023-10.parquet", schema=schema, header=True)
```
or

```python
data = spark.read\
    .option("header", True)\
    .schema(schema)\
    .csv("yellow_tripdata_2023-10.parquet")
```


