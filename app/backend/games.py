from flask import Blueprint, render_template, jsonify
from exts import db
from sqlalchemy import text
from flask import request

game_bp = Blueprint('games', __name__)

@game_bp.route('/getGame')
def getGame():
    print("getGame")
    return {"sdf":"hsdf"}



@game_bp.route("/db")
def dbTest():
    print("in db")
    result = db.session.execute(text("SELECT * FROM review"))
    for row in result:
        print(row)
    try:
        db.session.execute(text("UPDATE review SET rating=0 WHERE reviewid=3"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        print(f"An error occurred: {e}")
    return {"su":"ce"}

