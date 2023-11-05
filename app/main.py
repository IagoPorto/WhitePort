import os
import psycopg2
from psycopg2 import sql

db_params = {
    "host": os.environ.get("DB_HOST", "db"), 
    "port": int(os.environ.get("DB_PORT", 5432)), 
    "user": os.environ["POSTGRES_USER"],
    "password": os.environ["POSTGRES_PASSWORD"],
    "database": os.environ["POSTGRES_DB"]
}

if  __name__ == "__main__":
    print("Initializating")
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    query = sql.SQL("SELECT * FROM " + os.environ["POSTGRES_TABLE"])  
    cur.execute(query)
    results = cur.fetchall()
    for row in results:
        print(row)


    cur.close()
    conn.close()
