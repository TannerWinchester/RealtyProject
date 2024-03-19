# Tanner will start API work
# after comfortable save spot
# git add . --> staging will turn to green
# git commit -m 'comment'
# git push origin tanner --> will push to my branch in github
# finally later on when ready --> git merge feature --> git push feature
import json

### explore API calls

import requests
import pandas as pd
from pandas import json_normalize

# home_values = pd.read_csv('data/HomeValues.csv')
# df_home_values = pd.DataFrame(home_values)
# # print(df_home_values.head())
#
# # clean the data
# clean_df_home_values = df_home_values.dropna()
# pd.options.display.float_format = '{:,.2f}'.format
# print(clean_df_home_values.head(30))
#
# print(f'df shape: {clean_df_home_values.shape}')

# if we get access to the API from zillow
# endpoint = 'GET https://rentalsapi.zillowgroup.com/listings/v1/listingsForUser'
# # required parameters
# accessToken = ''
# clientId = ''
# city = 'Boise, ID'
# api_key = ''  # ~ will set ENV variable later
#
# params = {
#     'accessToken': accessToken,
#     'clientId': clientId,
#     'near': city,
#     'api_key': api_key
# }

import requests

endpoint = "https://api.schooldigger.com/v2.0/rankings/schools/{st}"


def school_search():
    params = {
        "q": "Boise",
        "st": "ID",
        "appID": "f607f499",
        "appKey": "da66c0739308a6fef6f4a4e37d0a2c55"
    }

    res = requests.get(endpoint, params=params)
    data = res.json()

    # data fields
    school_name = data['schoolName']
    phone = data['phone']
    address = data['address']['street']
    city = data['address']['city']
    state = data['address']['state']
    zip_code = data['address']['zip']

    print(f'School name: {school_name}')
    print(f'Phone:{phone}')
    print(f'Address: {address}')
    print(f'City: {city}')
    print(f'State: {state}')
    print(f'Zip Code: {zip_code}')




school_search()
