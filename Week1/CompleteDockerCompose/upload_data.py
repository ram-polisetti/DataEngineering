
import pandas as pd
from sqlalchemy import create_engine
# !pip install sqlalchemy --quiet
import argparse
import os
import pyarrow.parquet as pq
from time import time


def main(params):
    """_summary_

    Args:
        params (_type_): _description_
    """
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table = params.table
    url = params.url
    
    parquet_name = 'output.parquet'  # Change file extension to .parquet
    os.system(f'wget {url} -O {parquet_name}')  # Downloading the Parquet file
    
    # engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    with engine.connect() as connection:
    
        parquet_file = pq.ParquetFile(parquet_name)
        schema = parquet_file.schema

        # Extract and print column names
        column_names = schema.names
        # Create an empty DataFrame with these columns
        empty_df = pd.DataFrame(columns=column_names)
        empty_df.head(0).to_sql(name=table, con=connection, if_exists='replace')
        # Iterating over Parquet file in chunks
        i = 1
        for df in parquet_file.iter_batches(batch_size=100000):
            t_start = time()
            df = df.to_pandas()
            df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
            df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
            df.to_sql(name=table, con=connection, if_exists='append')
            t_end = time()
            print(f'Inserted Chunk {i}, time taken- {t_end-t_start}')
            i+=1
        
    print('Finished Ingesting data')
    




if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    # user
    # password
    # host
    # port
    # database name
    # table name
    # url of csv
    parser.add_argument('--user', type=str, default='root', help='user name')
    parser.add_argument('--password', type=str, default='root', help='password')
    parser.add_argument('--host', type=str, default='localhost', help='host')
    parser.add_argument('--port', type=str, default='5432', help='port')
    parser.add_argument('--database', type=str, default='ny_taxi', help='database name')
    parser.add_argument('--table', type=str, default='yellow_taxi_data', help='name of the table where we will write the results')
    parser.add_argument('--url', type=str, default='https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-10.parquet', help='url of parquet file')
    
    args = parser.parse_args()
    # print(args.accumulate(args.integers))
    main(args)