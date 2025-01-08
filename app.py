from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection string
server = 'task-database-server.database.windows.net'
database = 'task-database'
username = 'admin!'
password = 'Jor4phms!!J0r4phms!!'
driver = '{ODBC Driver 17 for SQL Server}'

def get_db_connection():
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
    return conn

@app.route('/api/store', methods=['POST'])
def store_data():
    data = request.json['data']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Data (Value) VALUES (?)", data)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Data stored successfully'})

@app.route('/api/retrieve', methods=['GET'])
def retrieve_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Data")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'id': row[0], 'value': row[1]} for row in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
