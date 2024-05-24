"""Module for managing data storage."""

import idgenerator


class DataPoint:
    """Class to represent a data point in an experiment."""

    def __init__(self, patient_id, experiment_id, data):
        self.identifier = idgenerator.generate_unique_identifier()
        self.patient_id = patient_id
        self.experiment_id = experiment_id
        self.data = data


class DataStorage:
    """class to manage patient and experiment data storage."""

    _instance = None

    experiments = {}  # dictionary of all experiments
    patients = {}
    data = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.experiments = {}
            cls._instance.patients = {}
            cls._instance.data = []
        return cls._instance

    def create_patient(self, name):
        """Create a new patient and return their ID."""
        patient_id = len(self.patients)
        self.patients[patient_id] = name
        return patient_id

    def create_experiment(self, name):
        """Create a new experiment and return its ID."""
        experiment_id = len(self.experiments)
        self.experiments[experiment_id] = name
        return experiment_id

    def get_patients(self):
        """Return a dictionary of all patients."""
        return self.patients

    def get_experiments(self):
        """Return a dictionary of all experiments."""
        return self.experiments

    def add_data(self, patient_id, experiment_id, data):
        """Add data to the data storage."""
        data_obj = DataPoint(patient_id, experiment_id, data)
        self.data.append(data_obj)

    def store_data(self):
        """Store data into a file."""
        # store data into file
        self.data.clear()
