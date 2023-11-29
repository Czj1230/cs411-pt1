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

