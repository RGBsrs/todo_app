import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object(config.Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.database import models
from src import routes

cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
