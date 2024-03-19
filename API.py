# # Tanner will start API work
#
#
#
# import requests
import pandas
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
link = "https://api.schooldigger.com/v2.0/rankings/schools/{st}"

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

df = pandas.read_csv("dummy_real_estate_data_homes_and_apartments.csv")
# Save to CSV

# Display DataFrame
print(df)



