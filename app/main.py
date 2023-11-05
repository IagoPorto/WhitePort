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


def get_results():
   
    
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    query = sql.SQL("SELECT * FROM " + os.environ["POSTGRES_TABLE"])
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    
    return results




def insert_whiteport_data(type, date, file):
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        query = sql.SQL("INSERT INTO {} (type, date, file) VALUES (%s, %s, %s)").format(
            sql.Identifier(os.environ["POSTGRES_TABLE"]))
        cur.execute(query, (type, date, file))
        conn.commit()

        cur.close()
        conn.close()

        return "WhitePort data inserted successfully", 201  
    except Exception as e:
        return str(e), 500  




if __name__ == "__main__":
    print("Initializing")
    results = get_results()
    for row in results:
        print(row)


