from flask import Flask
from .routes.simple import bp

app = Flask(__name__)
app.register_blueprint(bp)
