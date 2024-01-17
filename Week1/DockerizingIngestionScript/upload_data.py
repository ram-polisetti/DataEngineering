
import pandas as pd
from sqlalchemy import create_engine
# !pip install sqlalchemy --quiet
import argparse



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
    
    # engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    engine.connect()
    
    taxi_data = pd.read_csv(url, iterator=True, chunksize=100000)
    df = next(taxi_data)
    
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    
    df.head(0).to_sql(name=table, con=engine, if_exists='replace')
    df.to_sql(name=table, con=engine, if_exists='append')
    
    try:
        while True:
            df = next(taxi_data)
            df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
            df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
            df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
    except StopIteration:
        print('Finished Ingesting data')
    
parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
# user
# password
# host
# port
# database name
# table name
# url of csv
parser.add_argument('user', type=str, default='root', help='user name')
parser.add_argument('password', type=str, default='root', help='password')
parser.add_argument('host', type=str, default='localhost', help='host')
parser.add_argument('port', type=str, default='5432', help='port')
parser.add_argument('database', type=str, default='ny_taxi', help='database name')
parser.add_argument('table', type=str, default='yellow_taxi_data', help='name of the table where we will write the results')
parser.add_argument('url', type=str, default='Yellow Taxi 2019 Jan.csv', help='url of csv')


if __name__ == "__main__":
        main(parser.parse_args())