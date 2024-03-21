# Base project.
# Hunter will start working on flask routing / setting up template

from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from API import BoiseMedianPrice, ProjectTracker

app = Flask(__name__)
boise_median = BoiseMedianPrice()
project_tracker = ProjectTracker()


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
    # Boise property values 2012 - 2024 graph
    prices, years, chart_data = boise_median.get_data()
    boise_prices = prices
    boise_years = years

    # Total costs of projects and project tracker graph
    total_investment, projects_list, total_projects, investment_cost_list, bar_chart_data = project_tracker.get_total_costs()

    return render_template("boise-dashboard.html", boise_prices=boise_prices, boise_months=boise_years,
                           chart_data=chart_data, total_investment=total_investment, projects_list=projects_list, total_projects=total_projects, investment_cost_list=investment_cost_list,
                           bar_chart_data=bar_chart_data)


if __name__ == "__main__":
    app.run(debug=True)
