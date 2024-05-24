"""Module for generating unique identifiers"""

import uuid


def generate_unique_identifier():
    """Generates a unique identifier."""
    return str(uuid.uuid1())
