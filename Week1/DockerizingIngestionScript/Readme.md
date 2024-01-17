
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
    dpage/pgadmin4
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


## Python ingestion for dockerfile

```docker
URL = 
python upload_data.py \
--user=root \
--password=root \
--host=localhost \
--port=5432 \
--dbname=ny_taxi \
--table=yellow_taxi_data \
--url=${URL} \
```