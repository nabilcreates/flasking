# Import library for requests
import requests

# Import library related to JSON
import json

# Import flask
from flask import Flask, render_template

# Initialize the app (equivalent to let app = express())
app = Flask(__name__)

# Variables?
api_url = 'https://arrivelah.herokuapp.com/?id=27301'

# Set root route (equivalent to app.get())
@app.route('/')

# When visiting root route, it will run this function below
def hello():

    api_data = requests.get(api_url).json()

    # render_template function while passing the file name as a string (Flask will automatically look for the template folder with your html files inside)
    return render_template('home.html')

@app.route('/hey')
def hey():
    return 'hey'