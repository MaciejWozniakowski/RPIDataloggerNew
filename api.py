import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#DB_PATH = '/home/MaciejWozniakowski/programowanko/pythonProjects/RPIDataloggerNew/data_from_all_meters.db'
DB_PATH = '/home/pwee/MaciejWozniakowskiDatalogger/temp/data_from_all_meters.db'
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This will return rows as dictionaries
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/api/query', methods=['GET'])
def get_data():
    meter = request.args.get('meter')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not meter or not start_date or not end_date:
        return jsonify({"error": "'meter', 'start_date', and 'end_date' must all be provided"}), 400

    query = f'''
        SELECT * FROM {meter} 
        WHERE date BETWEEN ? AND ?
    '''
    results = query_db(query, [start_date, end_date])

    if results:
        results_list = [dict(row) for row in results]
        return jsonify(results_list)
    else:
        return jsonify({"message": "No data found"}), 404

app.run(host = "10.0.10.5", port = 5000 ,debug = True)
