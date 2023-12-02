from flask import Blueprint, render_template, jsonify
from exts import db
from sqlalchemy import text
from flask import request

game_bp = Blueprint('games', __name__)

@game_bp.route('/getGame')
def getGame():
    print("getGame")
    return {"sdf":"hsdf"}


@game_bp.route("/db", methods=['GET'])
def dbTest():
    print("in db")
    result = db.session.execute(text("SELECT * FROM review"))
    response_object = {}
    for row in result:
        response_object[row[0]]=row[1]
    print(response_object)
    try:
        db.session.execute(text("UPDATE review SET rating=0 WHERE reviewid=3"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        print(f"An error occurred: {e}")
    return response_object

@game_bp.route("/db/test/<searchid>", methods=['GET'])
def dbParaTest(searchid):
    result = db.session.execute(text("SELECT * FROM game"))
    return None

@game_bp.route("/db/popular_games", methods=['GET'])
def dbGetPopGames():
    results = db.session.execute(text("SELECT g.name, g.price, e.headerimage, e.website FROM game g NATURAL JOIN extrainfo e WHERE (website AND headerimage) IS NOT NULL ORDER BY g.recommendationcount DESC LIMIT 10"))
    games_list = []
    for game in results:
        games_dict = {
            "name": game[0],
            "price": game[1],
            "header_image": game[2],
            "website": game[3]
        }
        games_list.append(games_dict)
    return jsonify(games_list)

