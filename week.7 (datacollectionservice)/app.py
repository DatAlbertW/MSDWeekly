import json
from flask import Flask, request
import datastorage

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def add_data():
    """Add data to storage."""
    data = request.get_json()
    if 'id' in data:
        ds = datastorage.DataStorage()
        ds.store_data(data['id'], data)
        return "Data added", 201
    else:
        return "Missing ID", 400

@app.route('/data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    """Retrieve data by ID."""
    ds = datastorage.DataStorage()
    result = ds.retrieve_data(data_id)
    if result:
        return json.dumps(result), 200
    else:
        return "Data not found", 404

if __name__ == '__main__':
    app.run(debug=True)
