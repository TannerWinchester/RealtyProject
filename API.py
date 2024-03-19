# Tanner will start API work



import requests
link = "https://api.schooldigger.com/v2.0/rankings/schools/{st}"

def school_search():
    params = {
        "q": "Boise",
        "st": "ID",
        "appID": "f607f499",
        "appKey": "da66c0739308a6fef6f4a4e37d0a2c55"
    }
    query = requests.get(link, params=params)
    print(query.json())

school_search()
