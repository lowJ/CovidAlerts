import pandas as pd
from datetime import datetime, timedelta

ago = pd.read_csv("ago-us-counties.csv")
today = pd.read_csv("live-us-counties.csv")

def getday(state, county):
    print(state, county)
    r = today.loc[(today['state'] == state) & (today['county'] == county)]
    if len(r) == 0:
        return None
    r = r.iloc[0]
    return r['cases'], r['deaths']

def getweek(state, county):
    week_ago = str(datetime.today() - timedelta(days=7)).split()[0]
    r = ago.loc[(ago['state'] == state) & (ago['county'] == county) & (ago['date'] == week_ago)].iloc[0]
    week_ago_cases, week_ago_deaths = r['cases'], r['deaths']
    today = getday(state, county)
    return today[0] - week_ago_cases, today[1] - week_ago_deaths