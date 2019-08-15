import re
import requests
import json
from bs4 import BeautifulSoup as soup
import pprint
pp = pprint.PrettyPrinter(indent=4)

# page = requests.get('http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1')
# page = requests.get('https://www.espn.com/mlb/teams')
# page = requests.get('https://www.baseball-reference.com/')

def get_teams():
    page = requests.get('https://www.mlb.com/')


    target = soup(page.text, 'lxml')
    pattern = re.compile(r"window.team_info")
    my_script = target.find('script', text=pattern)
    my_script = my_script.text

    start = my_script.index('[')
    stop = my_script.index(']')+1
    stripped = my_script[start: stop]

    # teams is a list of dictionaries
    teams = json.loads(stripped)

    # for team in teams:
    #     print(f"{team['name']} - {team['division']['name']} - {team['springLeague']['name']}")
    #
    # pp.pprint(teams)

    return teams
