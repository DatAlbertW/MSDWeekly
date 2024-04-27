import idgenerator

class DataPoint:
    """Class to represent a data point."""
    def __init__(self, identifier, data):
        self.id = identifier
        self.data = data

class DataStorage:
    """Class to handle storage and retrieval of data points."""
    def __init__(self):
        self.storage = {}

    def store_data(self, identifier, data):
        """Store data with a unique identifier."""
        if identifier not in self.storage:
            self.storage[identifier] = DataPoint(identifier, data)

    def retrieve_data(self, identifier):
        """Retrieve data by its unique identifier."""
        return self.storage.get(identifier, None)
