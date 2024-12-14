from flask import Flask
from flask_migrate import Migrate

from app.routes.simple import bp
from app.config import Configuration

app = Flask(__name__)
app.register_blueprint(bp)
app.config.from_object(Configuration)

from app.models import db

db.init_app(app)

Migrate(app, db)
