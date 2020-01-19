from flask import Flask
from flask import render_template
from flask import url_for
from flask import Blueprint

from year1.addition.routes import yr1_addition

app = Flask(__name__)

# register blueprints
app.register_blueprint(yr1_addition, url_prefix="/year1")

@app.route("/")
def load_base_view():
    return render_template("base.html", msg="Hello, World!!!!!!!!!!")

if __name__ == "__main__":
        app.run(debug=True)
