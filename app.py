from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sum")
def sum():
    return render_template("sum.html")


if __name__ == "__main__":
    app.run(debug=True)
