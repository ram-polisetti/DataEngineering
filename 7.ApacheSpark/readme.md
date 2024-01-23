# Installation

1. Install conda
2. Create a conda environment

Follow this article to install [Apache Spark](https://medium.com/@divya.chandana/easy-install-pyspark-in-anaconda-e2d427b3492f)on Ubuntu

3. Install OpenJDK
4. Install Apache Spark
5. Test the installation
```bash
pyspark
```
![Alt text](image.png)

or

```bash
spark-shell
```
![Alt text](image-1.png)


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
