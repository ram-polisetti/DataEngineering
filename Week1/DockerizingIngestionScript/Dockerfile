FROM  python:3.9
RUN pip install sqlalchemy pandas numpy psycopg2 pyarrow time

WORKDIR /app
COPY pipeline.py pipeline.py

# ENTRYPOINT ["bash"]
ENTRYPOINT ["python", "pipeline.py"]
# CMD ["app.py"]