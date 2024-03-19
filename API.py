# Tanner will start API work
# after comfortable save spot
# git add . --> staging will turn to green
# git commit -m 'comment'
# git push origin tanner --> will push to my branch in GitHub
# finally later on when ready --> git merge feature --> git push feature


import pandas as pd
from pandas import json_normalize
import requests

# schooldigger API endpoint
endpoint = "https://api.schooldigger.com/v2.0/rankings/schools/{st}"


def school_search():
    params = {
        "q": "Boise",
        "st": "ID",
        "appID": "f607f499",
        "appKey": "da66c0739308a6fef6f4a4e37d0a2c55"
    }

    res = requests.get(endpoint, params=params)
    # API is restricting access, I put the response data in here locally for now.
    # data = res.json()

    # remove dummy data when API access is reset again
    data = {
        'schoolid': '160210000955',
        'schoolName': 'School #1465943059',
        'phone': '(555) 555-5555',
        'url': 'https://www.schooldigger.com/(pathtoitem)',
        'urlCompare': 'https://www.schooldigger.com/(pathtoitem)',
        'address': {
            'latLong': {
                'latitude': 40.65,
                'longitude': -121.4
            },
            'street': '123 Main St.',
            'city': 'Anytown',
            'state': 'CA',
            'stateFull': 'California',
            'zip': '99999',
            'zip4': '9999',
            'cityURL': 'https://www.schooldigger.com/go/CA/city/Anytown/search.aspx',
            'zipURL': 'https://www.schooldigger.com/go/CA/zip/99999/search.aspx',
            'html': '123 Main St.<br />Anytown, CA 99999-9999'
        },
        'lowGrade': 'PK',
        'highGrade': '5',
        'schoolLevel': 'Elementary',
        'isCharterSchool': 'No',
        'isMagnetSchool': '(n/a)',
        'isVirtualSchool': 'No',
        'isTitleISchool': '(n/a)',
        'isTitleISchoolwideSchool': '(n/a)',
        'hasBoundary': False,
        'district': {
            'districtID': '1602100',
            'districtName': 'School District #1309938082',
            'url': 'https://www.schooldigger.com/(pathtoitem)',
            'rankURL': 'https://www.schooldigger.com/(pathtorank)'
        },
        'county': {
            'countyName': 'AnyCounty',
            'countyURL': 'https://www.schooldigger.com/go/CA/county/AnyCounty/search.aspx'
        },
        'rankHistory': [
            {
                'year': 2023,
                'rank': 235,
                'rankOf': 1000,
                'rankStars': 0,
                'rankLevel': 'Elementary',
                'rankStatewidePercentage': 98.3,
                'averageStandardScore': 55.94
            },
            {
                'year': 2022,
                'rank': 660,
                'rankOf': 1000,
                'rankStars': 1,
                'rankLevel': 'Elementary',
                'rankStatewidePercentage': 77.97,
                'averageStandardScore': 34.57
            }
        ],
        'rankMovement': -1,
        'schoolYearlyDetails': [
            {
                'year': 2023,
                'numberOfStudents': 188,
                'percentFreeDiscLunch': 51.94,
                'percentofAfricanAmericanStudents': 72.51,
                'percentofAsianStudents': 97.98,
                'percentofHispanicStudents': 57.78,
                'percentofIndianStudents': 26.65,
                'percentofPacificIslanderStudents': 83.2,
                'percentofWhiteStudents': 3.46,
                'percentofTwoOrMoreRaceStudents': 18.31,
                'percentofUnspecifiedRaceStudents': None,
                'teachersFulltime': 26.0,
                'pupilTeacherRatio': 19.2,
                'numberofAfricanAmericanStudents': 77,
                'numberofAsianStudents': 23,
                'numberofHispanicStudents': 34,
                'numberofIndianStudents': 70,
                'numberofPacificIslanderStudents': 57,
                'numberofWhiteStudents': 29,
                'numberofTwoOrMoreRaceStudents': 8,
                'numberofUnspecifiedRaceStudents': None
            }
        ],
        'isPrivate': False,
        'privateDays': None,
        'privateHours': None,
        'privateHasLibrary': None,
        'privateCoed': None,
        'privateOrientation': None
    }

    # data fields
    school_name = data['schoolName']
    phone = data['phone']
    address = data['address']['street']
    city = data['address']['city']
    state = data['address']['state']
    zip_code = data['address']['zip']
    rank = data['rankHistory'][0]['rank']
    grade_level = data['rankHistory'][0]['rankLevel']

    print(f'school rankings {rank}')
    print(f'school level: {grade_level}')

    print(f'School name: {school_name}')
    print(f'Phone:{phone}')
    print(f'Address: {address}')
    print(f'City: {city}')
    print(f'State: {state}')
    print(f'Zip Code: {zip_code}')


school_search()


# # Tanner will start API work
#
#
#
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
