from flask import Blueprint, render_template

game_bp = Blueprint('games', __name__)

@game_bp.route('/getGame')
def getGame():
    print("getGame")
    return {"sdf":"hsdf"}
