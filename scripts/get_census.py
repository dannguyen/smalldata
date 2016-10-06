from requests import Request, Session
from sys import stdout, stderr
from csv import writer


BASE_SRC_URL = 'http://api.census.gov/data/{year}/acs5'
STATENUM = '06'
FIELDS = {
    "B01001_001E": "total_population",
    "B01002_001E": "median_age",
    "B03002_003E": "white",
    "B03002_004E": "black",
    "B03002_006E": "asian",
    "B03003_001E": "hispanic",
    "B11011_001E": "total_households",
    "B16001_001E": "population_5_and_over",
    "B16001_002E": "english_only_population_5_and_over",
    "B23006_001E": "adults_25_to_64",
    "B23006_001E": "adults_25_to_64_with_bachelors_degree",
    "B06012_002E": "below_poverty_line",
    "B25077_001E": "owner_occupied_homes_median_value",
    "B19013_001E": "per_capita_income",
    "B19013_001E": "median_household_income",
    "B06001_049E": "foreign_born_population"
}

def build_request(year):
    baseurl = BASE_SRC_URL.format(year=year)
    parms = {'for': 'tract:*', 'in': "state:%s" % STATENUM}
    parms['get'] = ','.join(['NAME', 'GEOID'] + list(FIELDS.keys()))
    req = Request('GET', baseurl, params=parms)
    return req.prepare()


FIELDNAMES = ['year', 'tract_name', 'geo_id'] + list(FIELDS.values()) + ['state', 'county', 'tract']


destcsv = writer(stdout)
destcsv.writerow(FIELDNAMES)

for year in [2010, 2014]:
    req = build_request(year)
    stderr.write(req.url + "\n")
    session = Session()
    response = session.send(req, allow_redirects=False)
    data = response.json()
    for row in data[1:]:
        destcsv.writerow([year] + row)



#http://api.census.gov/data/2014/acs5?for=tract:*&in=state:06&get=
