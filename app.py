# Import library for requests
import requests

# Import library related to JSON
import json

# Import flask
from flask import Flask
app = Flask(__name__)

# Variables?
api_url = 'https://arrivelah.herokuapp.com/?id=27301'

# Set root route
@app.route('/')

# When visiting root route, it will run this function below
def hello():

    api_data = requests.get(api_url).json()

    # json.dumps() convert json to string
    return json.dumps(api_data)