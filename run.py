from flask import Flask
from flask import render_template
from flask import url_for
from flask import Blueprint

from yr1.addition.views import yr1_addition

app = Flask(__name__)

# register blueprints
app.register_blueprint(yr1_addition)

@app.route("/")
def hello_world():
    return render_template("template.html", msg="Hello, World!!!!!!!!!!")

if __name__ == "__main__":
        app.run(debug=True)
