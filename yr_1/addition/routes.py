# yr1/addition/views.py

from flask import Blueprint, render_template


yr1_addition = Blueprint("yr1_addition", __name__, template_folder="templates", static_folder="static")

@yr1_addition.route("/yr1/addition")
def load("/yr1/addition"):
    return render_template("view.html")
