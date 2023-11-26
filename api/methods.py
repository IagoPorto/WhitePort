from flask import Flask, request, jsonify
from app.main import get_results,insert_whiteport_data,db_params

import psycopg2
from psycopg2 import sql
import os


app = Flask(__name)

@app.route('/whiteport', methods=['GET', 'POST'])

def getWhiteport():
    print("ha entrado en el metodo get")
    if request.method == 'GET':
        try:
            results = get_results()
            whiteport_data = []
            for row in results:
                whiteport_data.append({
                    "ID": row[0],
                    "type": row[1],
                    "date": row[2].isoformat(),
                    "file": row[3].tobytes().decode('utf-8', errors='ignore')
                })

            return jsonify(whiteport_data)
        except Exception as e:
            return str(e), 500  
def postWhiteport(type,date,file):

    if request.method == 'POST':
        try:
                # data = request.get_json()
                # type = data.get("type")
                # date = data.get("date")
                # file = data.get("file").encode('utf-8')

                response, status_code = insert_whiteport_data(type, date, file)

                return response, status_code
        except Exception as e:
                return str(e), 500  
        

def updateWhiteport(id):
        try:
            conn = psycopg2.connect(db_params)
            cur = conn.cursor()

            data = request.get_json()
            type = data.get("type")
            date = data.get("date")
            file = data.get("file").encode('utf-8')

            query = sql.SQL("UPDATE {} SET type = %s, date = %s, file = %s WHERE ID = %s").format(
                sql.Identifier(os.environ["POSTGRES_TABLE"]))
            cur.execute(query, (type, date, file, id))
            conn.commit()

            cur.close()
            conn.close()

            return "updated successfully", 200  
        except Exception as e:
            return str(e), 500  
        
def deleteWhiteport(id):
        try:
            conn = psycopg2.connect(db_params)
            cur = conn.cursor()

            query = sql.SQL("DELETE FROM {} WHERE ID = %s").format(
                sql.Identifier(os.environ["POSTGRES_TABLE"]))
            cur.execute(query, (id,))
            conn.commit()

            cur.close()
            conn.close()

            return "eleted successfully", 200  
        except Exception as e:
            return str(e), 500  

       
if __name__ == "__main__":
    print("Methods")
    results = get_results()
if  __name__ == "__main__":
    print("Methods")
    result = getWhiteport
    print(result)