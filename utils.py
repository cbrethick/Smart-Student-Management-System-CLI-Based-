import json, os
from functools import wraps

def load_students(path='data/students.json'):
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)

def save_students(data, path='data/students.json'):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def catch_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Error:", e)
    return wrapper
