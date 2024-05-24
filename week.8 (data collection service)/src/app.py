"""Module for handling web routes and operations related to data collection."""

from flask import Flask, request, json
import datastorage

app = Flask(__name__)

# Initialize a global data storage instance
global_data_storage = datastorage.DataStorage()


@app.route("/", methods=["GET"])
def index() -> str:
    """Return a simple JSON object of the author"""
    return json.dumps({"name": "David", "mail": "david.herzig@roche.com"})


@app.route("/experiment", methods=["POST", "GET"])
def create_experiment() -> str:
    """Create or get experiments."""
    local_data_storage = datastorage.DataStorage()
    if request.method == "POST":
        form_data = request.data
        data = json.loads(form_data)
        experiment_id = local_data_storage.create_experiment(data["name"])
        return json.dumps({"result": experiment_id})
    return json.dumps({"experiments": local_data_storage.get_experiments()})


@app.route("/patient", methods=["POST", "GET"])
def create_patient() -> str:
    """Create or get patients."""
    local_data_storage = datastorage.DataStorage()
    if request.method == "POST":
        name = request.args.get("name")
        patient_id = local_data_storage.create_patient(name)
        return json.dumps({"result": patient_id})
    return json.dumps({"patients": local_data_storage.get_patients()})


@app.route("/store", methods=["POST"])
def store_data() -> None:
    """Implementation needed."""
    return None


@app.route("/upload", methods=["POST"])
def upload_data() -> None:
    """Implementation needed."""
    return None


if __name__ == "__main__":
    print("Creating and listing experiments:")
    print(global_data_storage.create_experiment("Experiment"))
    print(global_data_storage.get_experiments())

    data_storage2 = datastorage.DataStorage()
    print(data_storage2.create_experiment("Experiment2"))
    print(data_storage2.get_experiments())

    app.run()
