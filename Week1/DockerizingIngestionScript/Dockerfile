FROM  python:3.9
RUN apt-get install wget
RUN pip install sqlalchemy pandas numpy psycopg2 pyarrow time
WORKDIR /app
COPY upload_data.py upload_data.py
ENTRYPOINT ["python", "upload_data.py"]
