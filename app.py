from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/reglamentos")
def reglamentos():
    return render_template("reglamentos.html")

@app.route("/formularios")
def inicio():
    return render_template("formularios.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")
    
@app.route("/notas")
def notas():
    return render_template("notas.html")

if __name__ == "__main__":
    app.run(debug=True)