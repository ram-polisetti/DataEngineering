# Docker Compose

- By default Docker Compose comes preinstalled with Docker in mac and Windows.
- It is used to specify one file for all the cofigurations for the containers as it is inconvinient to specify multiple files for each container.
  - All the configurations for the containers will be specified in one `YAML` file.

```bash
docker-compose
```

```bash
    volumes:
      - ./ny_taxi_postgres_data:/var/lib/postgresql/data:rw
```

- ./ny_taxi_postgres_data -> hostpath
- /var/lib/postgresql/data -> container path
- rw -> mode (No need to specify it explicitly)

```yaml
services:
  pg-database:
    image: postgres:13
    environment:
      - POSTGRES_USER=root 
      - POSTGRES_PASSWORD=root 
      - POSTGRES_DB=ny_taxi 
    volumes:
      - "./ny_taxi_postgres_data:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
  
  pg-admin:
   image: dpage/pgadmin4
   environment:
    - PGADMIN_DEFAULT_EMAIL=admin@admin.com
    - PGADMIN_DEFAULT_PASSWORD=root
   ports:
    - "8080:80"

```

- No need to specify the network interface. It will happen automatically.
