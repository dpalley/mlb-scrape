from flask import Flask, render_template, url_for
from teams import get_teams
from players import get_players
from stats import get_stats

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/league")
def league():
    teams = get_teams()
    return render_template('league.html', teams=teams, title='Teams')

@app.route("/players")
def players():
    players = get_players()
    return render_template('players.html', players=players, title='Players')

@app.route("/stats")
def player():
    stats = get_stats()
    return render_template('player.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
