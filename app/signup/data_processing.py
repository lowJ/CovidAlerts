import pandas as pd
from datetime import datetime, timedelta
from signup.state_abbreviations import us_state_abbrev

ago = pd.read_csv("signup/ago-us-counties.csv")
today = pd.read_csv("signup/live-us-counties.csv")

def getday(state, county):
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

def liststates():
    return list(today['state'].unique())

def listcounties():
    state_abr = []
    for state in today['state']:
        state_abr.append(us_state_abbrev[state])
    return list(today['county'] + " (" + state_abr + ")")

def list_all_counties():
    return list(today['county'])

def get_state(county):
    r = today.loc[today['county'] == county]
    return list(r['state'])

def counties_of_state(state):
    return list(today.loc[today['state'] == state]['county'])