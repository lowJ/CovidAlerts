from signup.state_abbreviations import us_abbrev_state
from signup.data_processing import counties_of_state, list_all_counties, get_state

def checkCounty(county_get: str):
    #check case where state abbreviations included
    if '(' in county_get:
        county_get = county_get.split(' (')
        county_get[1] = county_get[1][:-1]
        if county_get[1] not in us_abbrev_state:
            return f"{county_get[1]} is an invalid State Abbreviation."
        county_get[1] = us_abbrev_state[county_get[1]]
        state_counties = counties_of_state(county_get[1])
        if county_get[0] not in state_counties:
            return f"{county_get[0]} is an invalid county in {county_get[1]}."
        return county_get

    county_get = county_get.rstrip()
    all_counties = list_all_counties()
    count = all_counties.count(county_get)
    if count > 1:
        return f"There are {count} {county_get} Counties in the US. Please specify the State."
    if count == 0:
        return f"{county_get} is an invalid County in the US."
    return [county_get, get_state(county_get)[0]]