from flask import Flask, render_template
from teams import get_teams

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    teams = get_teams()
    return render_template('home.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)
