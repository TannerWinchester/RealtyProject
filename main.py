# Base project.
# Hunter will start working on flask routing / setting up template

from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from API import lasherData

app = Flask(__name__)
lash = lasherData()


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
    raw_cost, raw_rev, chart_data = lash.costs()
    total_cost = f"{raw_cost:,}"
    total_rev = f"{raw_rev:,}"
    return render_template("lasher-enterprises.html", total_cost=total_cost, total_rev=total_rev, chart_data=chart_data)






if __name__ == "__main__":
    app.run(debug=True)