from flask import Flask, render_template, url_for;

app = Flask(__name__);

@app.route("/about")
def about():
    url_for("static", filename="styles.css")
    return render_template("about.html");

@app.route("/")
def home():
    url_for("static", filename="styles.css")
    return render_template("index.html");

