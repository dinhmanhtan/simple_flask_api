from flask import Flask
from config import Config
from models import db
from api import api

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
