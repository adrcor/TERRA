from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv('.env')

app = Flask(__name__)
CORS(app)

app.debug = os.getenv('ENVIRONMENT') == 'local'

@app.route('/')
def home():
    return 'Api is running'

if __name__ == '__main__':
    app.run(port=5000)