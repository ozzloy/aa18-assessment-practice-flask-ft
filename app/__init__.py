from flask import Flask

from app.routes import simple

app = Flask(__name__)
app.register_blueprint(simple.bp)
