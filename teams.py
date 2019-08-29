import re
import requests
import json
from bs4 import BeautifulSoup as soup
import pprint
pp = pprint.PrettyPrinter(indent=4)

# page = requests.get('http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1')
# page = requests.get('https://www.espn.com/mlb/teams')
# page = requests.get('https://www.baseball-reference.com/')

def get_leagues():
    pass

def get_teams():
    # get html from web
    page = requests.get('https://www.mlb.com/standings')

    # get local html
    # with open(r'teams.html', "r") as f:
    #     page = f.read()
    # page = html.fromstring(page)

    target = soup(page.text, 'lxml')

    pattern = re.compile(r"window.reactHeaderState")
    my_script = target.find('script', text=pattern)
    my_script = my_script.text


    teams_start = my_script.index('"teamData')
    teams = my_script[teams_start :]

    # find the matching '}'
    first_curly = teams.index('{')
    index = first_curly + 1
    count = 1
    while count > 0:
        if teams[index] == '{':
            count += 1
        if teams[index] == '}':
            count -=1
        index += 1
    # print(f'first curly is {first_curly}, last_curly is {index}')
    teams = teams[first_curly:index]

    teams = json.loads(teams)

    return teams

def get_players():
    page = requests.get('https://www.mlb.com/standings')
    # http://m.astros.mlb.com/hou/roster/40-man/

    pass

def get_teams2():
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
