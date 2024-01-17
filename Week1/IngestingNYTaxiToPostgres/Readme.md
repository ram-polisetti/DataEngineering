# Postgres DB Docker image creation

```bash
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

```bash
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13
```

```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

![Alt text](image.png)

- Extract a .gz file

```bash
gunzip yellow_tripdata_2019-01.csv.gz 
```

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

```bash
docker pull dpage/pgadmin4
```

```bash

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4
```

- Doing this eventually fails cause postgredb and pgadmin are in different networks and they cant communicate with each other

## Creating Network 

```bash
docker network create pg-network
```

- postgresdb

```bash
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

Accessing PostgreSQL from PgAdmin

- Now we have to run pg-admin in the same network

```bash

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name=pgadmin \ 
    dpage/pgadmin4
```

- here the name is not important because we are not connecting any container to pgadmin whereas we need connection to postgresdb to access the data.
- Login using credentials "admin@admin.com" and "root"
  - Right click on servers 
  - create new server
  - hostname -> pg-database
  - username -> root
  - password -> root
- Then go to databases and inspect the ny_taxi database
![Alt text](image-4.png)