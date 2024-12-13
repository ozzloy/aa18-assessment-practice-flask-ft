from flask import Blueprint, redirect, render_template, url_for

from app.models import db, SimplePerson
from ..forms import SimpleForm

bp = Blueprint("simple", __name__)


@bp.route("/")
def index():
    return render_template("main_page.html.j2")


@bp.route("/simple-form", methods=["GET"])
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html.j2", form=form)


@bp.route("/simple-form", methods=["POST"])
def simple_form_data():
    form = SimpleForm()
    if form.validate_on_submit():
        # person = SimplePerson(
        #     name=form.name.data,
        #     age=form.age.data,
        #     bio=form.bio.data,
        # )
        person = SimplePerson()
        form.populate_obj(person)
        db.session.add(person)
        db.session.commit()
        return redirect(url_for("simple.index"))

    return "Bad Data"


@bp.route("/simple-form-data", methods=["GET"])
def get_simple_form_data():
    m_names = SimplePerson.query.filter(
        SimplePerson.name.like("M%")
    ).all()
    return render_template("simple_form_data.html.j2", people=m_names)
