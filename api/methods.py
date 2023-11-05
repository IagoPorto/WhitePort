from flask import Flask, request, jsonify
from app.main import get_results,insert_whiteport_data

import psycopg2
from psycopg2 import sql
import os


app = Flask(__name)

@app.route('/whiteport', methods=['GET', 'POST'])

def getWhiteport():
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
def PostWhiteport():

    if request.method == 'POST':
        try:
                data = request.get_json()
                type = data.get("type")
                date = data.get("date")
                file = data.get("file").encode('utf-8')

                response, status_code = insert_whiteport_data(type, date, file)

                return response, status_code
        except Exception as e:
                return str(e), 500  