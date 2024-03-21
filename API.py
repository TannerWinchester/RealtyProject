# Tanner will start API work
# after comfortable save spot
# git add . --> staging will turn to green
# git commit -m 'comment'
# git push origin tanner --> will push to my branch in GitHub
# finally later on when ready --> git merge feature --> git push feature

import json
import pandas as pd
from pandas import json_normalize
import requests
import numpy as np
from datetime import datetime, timedelta
import random

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


class BoiseMedianPrice:
    def __init__(self):
        self.df_boise = pd.read_csv('data/boise-market-data.csv')

    def get_data(self):
        self.df_boise['Median Sale Price'] = self.df_boise['Median Sale Price'].replace({'\$': '', 'K': 'e3'},
                                                                                        regex=True).astype(
            float).astype(int)

        # values of all median sale price column
        prices = self.df_boise['Median Sale Price'][::12]

        # grabs all values from the prices section and turns it into a list
        boise_median_prices = prices.values.tolist()
        print(boise_median_prices)

        # values of all months column
        months_data = self.df_boise['Month of Period End'][::12]
        # print(months_data)

        # drops the index key and converts into a list of months
        months = months_data.values.tolist()
        years = [datetime.strptime(month, "%B %Y").year for month in months]

        chart_data = {
            'price': boise_median_prices,
            'year': years
        }

        return boise_median_prices, years, chart_data


class ProjectTracker:
    def __init__(self):
        # create fictional data for total cost (in hundreds of thousands)
        self.total_cost = [random.randint(100, 600) * 1000 for _ in range(13)]

        # create fictional data for build projects (up to 15)
        self.build_projects = [random.randint(1, 10) for _ in range(13)]

        # print("Total Cost:", self.total_cost)
        # print("Build Projects:", self.build_projects)

    def get_total_costs(self):
        # list of costs for each project
        investment_cost_list = self.total_cost
        print(investment_cost_list)

        total_investment_added = sum(self.total_cost)
        total_investment = "${:,.2f}".format(total_investment_added)
        print(total_investment)

        projects_list = self.build_projects
        print('project LIST: ', projects_list)

        total_projects = sum(projects_list)
        print('total pojects: ', total_projects)

        bar_chart_data = {
            # sum of all projects
            'total_investment': total_investment,
            # list of projects expenses
            'project_list': projects_list,
            # total number of projects
            'total_projects': total_projects,
            'investment_cost_list': investment_cost_list
        }

        return total_investment, projects_list, total_projects, investment_cost_list, bar_chart_data


i = ProjectTracker()
i.get_total_costs()
