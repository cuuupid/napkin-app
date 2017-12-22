import os
import json

def load_dataset():
    with open('data.json') as f:
        return json.load(f)