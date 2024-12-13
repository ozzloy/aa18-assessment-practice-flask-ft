from flask import Blueprint, render_template
from ..forms import SimpleForm

bp = Blueprint("main", __name__, "/")


@bp.route("/")
def index():
    return render_template("main_page.html.j2")


@bp.route("/simple-form")
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html.j2", form=form)
