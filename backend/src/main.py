from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from routes.geo import GeoBlueprint
from routes.test import TestBlueprint
from routes.highscore import HighscoreBlueprint
from routes.practice import PracticeBlueprint

load_dotenv('.env')

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": [os.getenv('DOMAIN', '*')]}})

app.debug = os.getenv('ENVIRONMENT') == 'local'
app.config["JWT_SECRET_KEY"] = os.getenv('SUPABASE_JWT')

jwt = JWTManager(app)

@app.route('/')
def home():
    return 'Api is running'

app.register_blueprint(GeoBlueprint, url_prefix='/geo')
app.register_blueprint(TestBlueprint, url_prefix='/test')
app.register_blueprint(HighscoreBlueprint, url_prefix='/highscore')
app.register_blueprint(PracticeBlueprint, url_prefix='/practice')


if __name__ == '__main__':
    app.run(port=5000)