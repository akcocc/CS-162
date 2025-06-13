from flask import Flask, render_template, url_for;

app = Flask(__name__);

@app.route("/about")
def about():
    url_for("static", filename="styles.css")
    url_for("static", filename="mind-blow-galaxy.gif")
    return render_template("about.html");

@app.route("/")
def home():
    url_for("static", filename="styles.css")
    url_for("static", filename="hubble-ultra-deep-field.webp")
    return render_template("index.html");


