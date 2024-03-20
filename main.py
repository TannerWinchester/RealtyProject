# Base project.
# Hunter will start working on flask routing / setting up template

from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from API import BoiseMedianPrice

app = Flask(__name__)
boise_median = BoiseMedianPrice()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/login")
def login():
    pass


@app.route("/signup")
def signup():
    pass


@app.route("/lasher-enterprises")
def lasher():
    return render_template("lasher-enterprises.html")


@app.route("/boise")
def boise():
    boise_median.get_data()

    return render_template("boise-enterprises.html")



if __name__ == "__main__":
    app.run(debug=True)