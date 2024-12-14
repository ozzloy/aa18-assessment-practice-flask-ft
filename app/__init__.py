from flask import Flask

from app.config import Configuration
from app.routes.simple import bp

app = Flask(__name__)
app.register_blueprint(bp)
app.config.from_object(Configuration)

from app.models import db

db.init_app(app)
