from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from routes.user import UserBlueprint

load_dotenv('.env')

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.debug = os.getenv('ENVIRONMENT') == 'local'
app.config["JWT_SECRET_KEY"] = os.getenv('SUPABASE_JWT')

jwt = JWTManager(app)

@app.route('/')
def home():
    return 'Api is running'

app.register_blueprint(UserBlueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(port=5000)