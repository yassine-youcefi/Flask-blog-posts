
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

application = Flask(__name__)
# application config "object"
application.config.from_object(Config)

# init database instance
db = SQLAlchemy(application)
migrate = Migrate(application, db)

from app import routes
