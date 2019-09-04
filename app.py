from flask import Flask, render_template, url_for, request
from teams import get_teams, get_players
from stats import get_stats
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(24)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/league", methods=['GET', 'POST'])
def league():
    teams = get_teams()
    if request.method == 'POST':
        team = request.form.get('team')
        player_names, player_ids = get_players(team)

        return render_template('players.html', team=team,
            player_info=zip(player_names, player_ids), title='Players')

    else:
        return render_template('league.html', teams=teams, title='Teams')

@app.route("/players", methods=['GET', 'POST'])
def players():
    player_names, player_ids = get_players(team)
    return render_template('players.html', team=team,
        player_info=zip(player_names, player_ids), title='Players')

# @app.route("/stats")
# def player():
#     stats = get_stats()
#     return render_template('player.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
