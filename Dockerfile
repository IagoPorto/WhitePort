FROM python:3.13.0a1-bookworm

RUN pip install flask psycopg2

WORKDIR /app

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]