import re
import requests
import json
from bs4 import BeautifulSoup as soup

def get_teams():
    # get html from web
    page = requests.get('https://www.mlb.com/standings')

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

def get_players(team):
    page = requests.get('http://m.' + team + '.mlb.com/roster/40-man/')

    target = soup(page.text, 'lxml')
    roster = target.find('div', id='content')
    player_names = []
    player_ids = []

    for a in roster.find_all('a', class_=''):
        href = a['href']
        junk1, junk2, player_id, name = href.split('/')
        player_name = name.title().replace('-', ' ')
        player_names.append(player_name)
        player_ids.append(player_id)

    return player_names, player_ids

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
    return teams
