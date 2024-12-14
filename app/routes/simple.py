from flask import Blueprint, redirect, render_template

from app.forms import SimpleForm
from app.models import db, SimplePerson

bp = Blueprint("simple", __name__)


@bp.route("/")
def index():
    return render_template("main_page.html.j2")


@bp.route("/simple-form")
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html.j2", form=form)


@bp.route("/simple-form", methods=["POST"])
def post_simple_form():
    form = SimpleForm()
    if not form.validate_on_submit():
        return "Bad Data"

    person = SimplePerson()
    # take data from posted form page, (name, age, bio)
    form.populate_obj(person)
    # use SimplePerson to insert it into the db using SimplePerson
    db.session.add(person)
    db.session.commit()
    return redirect("/")
