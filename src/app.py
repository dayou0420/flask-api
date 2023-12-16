import os
import json
from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import PyMongo
from bson import json_util

load_dotenv()

app = Flask(__name__)

# Ensure that the environment variable is set and not empty
if os.getenv('MONGODB_ENDPOINT') is None:
    raise ValueError("MONGO_URI not found in the environment. Please check your .env file.")

app.config['MONGO_URI'] = os.getenv('MONGODB_ENDPOINT')
mongo = PyMongo(app)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/api/v1/data', methods=['GET'])
def get_data():
    data = list(mongo.db.deviceReadings.find())
    return parse_json(data), 200

if __name__ == '__main__':
    app.run(debug=True)
