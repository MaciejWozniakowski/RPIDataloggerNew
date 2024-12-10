import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Path to your SQLite database
DB_PATH = '/home/MaciejWozniakowski/programowanko/pythonProjects/RPIDataloggerNew/data_from_all_meters.db'
#DB_PATH = '/home/MaciejWozniakowski/programowanko/pythonProjects/RPIDataloggerNew/data_from_all_meters.db'

# Function to query the database
def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This will return rows as dictionaries
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# API to fetch data from the database
@app.route('/api/query', methods=['GET'])
def get_data():
    # Get the start_date and end_date from the query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Both 'start_date' and 'end_date' must be provided"}), 400

    # Query to fetch data from the database
    query = '''
        SELECT * FROM meter 
        WHERE timestamp BETWEEN ? AND ?
    '''
    results = query_db(query, [start_date, end_date])

    # Return the results as JSON
    if results:
        # Convert each row to a dictionary
        results_list = [dict(row) for row in results]
        return jsonify(results_list)
    else:
        return jsonify({"message": "No data found"}), 404

app.run(debug=True)
