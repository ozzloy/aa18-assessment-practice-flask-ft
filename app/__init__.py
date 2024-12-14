from flask import Flask
from app.routes.simple import bp

app = Flask(__name__)
app.register_blueprint(bp)
