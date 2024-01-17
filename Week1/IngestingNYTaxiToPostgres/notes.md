# Postgres DB Docker image creation

```docker
services:
postgres:
image: postgres:13 environment:
POSTGRES_USER: airflow
POSTGRES_PASSWORD: airflow
POSTGRES _DB: airflow 
volumes:
- postgres-db-volume: /var/lib/postgresql/data 
Week1/IngestingNYTaxiToPostgres/ny_taxi_postgres_data
healthcheck:
test: ["CMD", "pg_isready", "-U", "airflow"] interval: 5s
retries: 5
restart: always
```

- Docker image for Postgres DB

```docker
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13
```

```$ pgcli -h localhost -p 5432 -u root -d ny_taxi```

![Alt text](image.png)

- Extract a .gz file

``` gunzip yellow_tripdata_2019-01.csv.gz ```

- Connecting to Postgres DB from jupyter


```python
from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()
```

- postgresql -> db
- root -> username
- root -> password
- 5432 -> portnumber
- ny_taxi -> DB name

![Alt text](image-1.png)

![Alt text](image-2.png)

```%time tmp_df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')```

![Alt text](image-3.png)

## Setting up Pgadmin Using Docker

```docker
docker pull dpage/pgadmin4
```

```docker   

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin
```

- Doing this eventually fails cause postgredb and pgadmin are in different networks and they cant communicate with each other

## Creating Network 

```docker
docker network create pg-network
```

- postgresdb
```docker
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name=pg-database \ 
    postgres:13
```

- --network -> assign the network name to this variable
- --name -> how the pgadmin is going to discover postgres db


- Now we have to run pg-admin in the same network 

```docker   

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name=pgadmin \ 
    dpage/pgadmin
```

- here the name is not important because we are not connecting any container to pgadmin whereas we need connection to postgresdb to access the data 