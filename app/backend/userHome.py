from flask import Blueprint, render_template, jsonify, Flask, request, redirect, url_for
from exts import db
from sqlalchemy import text
from flask import request

userHome_be = Blueprint('userHome', __name__)

def get_favorite_games(id : int):
    # This should be replaced with your actual logic to fetch games
    # For example, a call to a database or an external API
    result = db.session.execute(text("SELECT * FROM favorite natural join game WHERE favorite.uid="+str(id)))
    response_object = []
    
    for row in result:
        print(row)
        one_game = {}
        one_game['id']=row[0]
        one_game['title']=row[2]
        one_game['description']=row[3]
        response_object.append(one_game)
        
    return response_object
    



@userHome_be.route('/submit_review/<uid>', methods=['POST'])
def rate_game(uid):
    # Here you would handle the rating logic
    print("===========")
    print(uid)
    print("Rating received:", request.form)
    print(request.form.get('game_id'))
    print(request.form.get('rating'))
    print(request.form.get('review'))
    sql = text("INSERT INTO review(rating, comment) VALUES(" + str(request.form.get('rating')) + ", \"" + str(request.form.get('review')) + "\")")
    # print(sql)
    result = db.session.execute(sql)
    last_insert_id = result.lastrowid # Get the last insert ID
    # print(last_insert_id)
    sql2 = text("INSERT INTO include VALUES("+str(last_insert_id)+","+str(request.form.get('game_id')+")"))
    # print(sql2)
    db.session.execute(sql2)
    db.session.commit()
    return {"haha":"lalal"}
    # return redirect(url_for('home'))

# @userHome_be.route('/write_review', methods=['POST'])
# def write_review():
#     # Here you would handle the review submission
#     print("Review received:", request.form)
#     return redirect(url_for('home'))

@userHome_be.route('/delete_game/<int:game_id>', methods=['POST'])
def delete_game(game_id):
    # Here you would handle the deletion logic
    global games
    games = [game for game in games if game['id'] != game_id]
    return redirect(url_for('home'))