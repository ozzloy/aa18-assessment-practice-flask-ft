from flask import Flask

from app.config import Configuration
from .routes.simple import bp

app = Flask(__name__)
app.register_blueprint(bp)
app.config.from_object(Configuration)
