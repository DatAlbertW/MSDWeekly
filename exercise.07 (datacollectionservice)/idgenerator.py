"""Creating unique ID for patient"""
import uuid

def generate_unique_identifier():
  return str(uuid.uuid1())