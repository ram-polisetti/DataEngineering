

Specifies how exactly we want to connect to spark

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder\
                    .master("local[*]")\
                    .appName("test")\
                    .getOrCreate()
```
-> local[*] : run spark locally with as many worker threads as logical cores on your machine.

-> spark session is locally available at http://localhost:4040/
