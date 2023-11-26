FROM python:3.9

RUN pip install flask psycopg2

WORKDIR /app

COPY . /app

EXPOSE 5000

CMD ["./wait-for-it.sh", "db:5432", "--", "python", "app/main.py","api/methods.py"]