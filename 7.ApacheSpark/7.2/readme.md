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
            StructField('Airport_fee', DoubleType(), True)]
)
```