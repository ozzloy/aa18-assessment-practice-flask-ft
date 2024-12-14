from flask import Flask

from app.routes.simple import bp
from app.config import Configuration

app = Flask(__name__)
app.register_blueprint(bp)
app.config.from_object(Configuration)
