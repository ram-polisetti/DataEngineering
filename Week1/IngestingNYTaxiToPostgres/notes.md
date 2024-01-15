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