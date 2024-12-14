from flask import Blueprint, render_template

from app.forms import SimpleForm

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
    
