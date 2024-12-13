from flask import Flask

from app.routes import simple
from app.config import Configuration

from app.models import db

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(simple.bp)
db.init_app(app)
