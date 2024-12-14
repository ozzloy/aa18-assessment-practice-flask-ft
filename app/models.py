from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
column = db.Column
integer = db.Integer
string = db.String


class SimplePerson(db.Model):
    __tablename__ = "simple_people"

    id = column(integer, primary_key=True)

    name = column(string(50), nullable=False)
    age = column(integer)
    bio = column(string(2000))
