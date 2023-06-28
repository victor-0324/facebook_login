from flask import Blueprint, request, render_template, url_for, redirect

initial_app = Blueprint("initial_app", __name__, url_prefix="/", template_folder='templates',static_folder='static')



@initial_app.route("/", methods=["GET", "POST"])
def mostrar():
    return render_template("index.html")


@initial_app.route("/thanks.html", methods=["GET", "POST"])
def login():
    return render_template("thanks.html")

@initial_app.route("/forget.html", methods=["GET", "POST"])
def forget():
    return render_template("forget.html")