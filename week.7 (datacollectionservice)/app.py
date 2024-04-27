import json
from flask import Flask, request
import datastorage
import logging

#Welcomoe to the App!: http://127.0.0.1:5000/

# Setup logging configuration
logging.basicConfig(filename='datacollection.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """Route to welcome users to the Flask App."""
    return 'Welcome to the App!'

@app.route('/data', methods=['POST'])
def add_data():
    """Add data to storage and log the process."""
    logging.info("Attempting to add data")
    data = request.get_json()
    if 'id' in data:
        ds = datastorage.DataStorage()
        ds.store_data(data['id'], data)
        logging.info(f"Data added with ID {data['id']}")
        return "Data added", 201
    else:
        logging.warning("Attempted to add data without ID")
        return "Missing ID", 400

@app.route('/data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    """Retrieve data by ID and log the attempt."""
    ds = datastorage.DataStorage()
    result = ds.retrieve_data(data_id)
    if result:
        logging.info(f"Data retrieved for ID {data_id}")
        return json.dumps(result), 200
    else:
        logging.warning(f"Data not found for ID {data_id}")
        return "Data not found", 404

if __name__ == '__main__':
    app.run(debug=True)
