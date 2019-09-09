from flask import Flask, render_template, url_for, request, redirect
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
        team_info = request.form.get('team')
        # team, dashed_name, division_id = request.form.get('team')
        team, dashed_name, division_id = team_info.split('.')
        player_names, player_ids = get_players(team)

        return redirect(url_for('.players', team=team, dashed_name = dashed_name,
            division_id = division_id, player_names=player_names, player_ids=player_ids, title='Players'))

    else:
        return render_template('league.html', teams=teams, title='Teams')

@app.route("/players", methods=['GET', 'POST'])
def players():
    #retrieve data from the return redirect statement in the league() method
    team = request.args['team']
    dashed_name = request.args['dashed_name']
    division_id = request.args['division_id']
    player_names = request.args.getlist('player_names')
    player_ids = request.args.getlist('player_ids')
    title = request.args['title']

    return render_template('players.html', team=team, dashed_name = dashed_name,
        division_id = division_id, player_info=zip(player_names, player_ids), title=title)

# @app.route("/stats")
# def player():
#     stats = get_stats()
#     return render_template('player.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
