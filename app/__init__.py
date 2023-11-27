from flask import Flask, render_template, redirect, url_for, request, Blueprint
from app.backend.games import game_bp
import config
from exts import db
from flask import request

app = Flask(__name__)
app.config.from_object(config)
# allow track and modify database
db.init_app(app)

@game_bp.route('/search')
def search_games():
    search_term = request.args.get('query')
    result = db.session.execute(text(f"SELECT * FROM games WHERE name LIKE '%{search_term}%'"))
    games = [dict(row) for row in result]
    return jsonify(games)

app.register_blueprint(game_bp)



from app import views

if __name__ == '__main__':
    print("__init__")
    app.run(debug=True)