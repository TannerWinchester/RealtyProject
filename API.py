# # Tanner will start API work
#
#
#
# import requests
import pandas
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
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






