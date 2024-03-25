# # Tanner will start API work
#
#
#
# import requests
import pandas
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
from datetime import timedelta
# link = "https://api.schooldigger.com/v2.0/rankings/schools/{st}"

# def school_search():
#     params = {
#         "q": "Boise",
#         "st": "ID",
#         "appID": "f607f499",
#         "appKey": "da66c0739308a6fef6f4a4e37d0a2c55"
#     }
#     query = requests.get(link, params=params)
#     print(query.json())
#
# school_search()

# df = pd.read_csv("dummy_real_estate_data_with_projects.csv")
#
# test = df.columns
#
# print(test)

import pandas as pd

class lasherData():
    def __init__(self):
        self.df = pd.read_csv("dummy_real_estate_data_homes_and_apartments.csv")
    def costs(self):
       total_cost = self.df["Actual Cost"].sum()
       total_rev = self.df["Sales Price"].sum()
       chart_data = {
           'costs': [],
           'revenue': [],
       }
       for cost in self.df['Actual Cost'].head(12):
           chart_data['costs'].append(cost)

       for rev in self.df['Sales Price'].head(12):
           chart_data['revenue'].append(rev)
       return total_cost, total_rev, chart_data

    def monthly_rev(self):
        total_cost = self.df["Actual Cost"].sum()
        total_rev = self.df["Sales Price"].sum()


    def forecast_profit_and_costs(self):
        chart_data = {
            'costs': [],
            'profit': [],
        }
        self.df['Profit'] = self.df['Sales Price'] - self.df['Actual Cost']
        # Extract relevant columns
        data = self.df[['Start Date', 'Net Profit ($)', 'Actual Cost']].copy()

        # Convert 'Start Date' to datetime
        data['Start Date'] = pd.to_datetime(data['Start Date'])

        # Convert 'Start Date' to numeric
        data['Start Date'] = (data['Start Date'] - data['Start Date'].min()).dt.days

        # Prepare data for linear regression
        X = data['Start Date'].values.reshape(-1, 1)
        y_profit = data['Net Profit ($)'].values
        y_costs = data['Actual Cost'].values

        # Fit linear regression models
        model_profit = LinearRegression()
        model_costs = LinearRegression()
        model_profit.fit(X, y_profit)
        model_costs.fit(X, y_costs)

        # Forecast profit and costs for 5 years
        future_dates = np.arange(X.max() + 1, X.max() + 61).reshape(-1, 1)
        forecasted_profit = model_profit.predict(future_dates)
        forecasted_costs = model_costs.predict(future_dates)

        # Calculate average profit and costs for each year
        num_years = 5
        avg_profit_per_year = []
        avg_costs_per_year = []
        for i in range(num_years):
            start_index = i * 12
            end_index = (i + 1) * 12
            avg_profit = np.mean(forecasted_profit[start_index:end_index])
            avg_costs = np.mean(forecasted_costs[start_index:end_index])
            avg_profit_per_year.append(avg_profit)
            avg_costs_per_year.append(avg_costs)

        for profit in avg_profit_per_year:
            chart_data['profit'].append(profit)
        for cost in avg_costs_per_year:
            chart_data['costs'].append(cost)

        return chart_data





