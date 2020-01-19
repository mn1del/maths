# yr1/addition/views.py

from flask import Blueprint, render_template


yr1_addition = Blueprint("year1_addition", __name__, template_folder="templates", static_folder="static")

@yr1_addition.route("/addition")
def load_view():
    return render_template("view.html", test_sum="insert some test sum here!!!")
