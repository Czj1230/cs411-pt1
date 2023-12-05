from flask import Blueprint, render_template, jsonify, Flask, request, redirect, url_for
from exts import db
from sqlalchemy import text
from flask import request
from datetime import datetime

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
    curDate = datetime.now().strftime("%Y-%m-%d")
    sql2 = text("INSERT INTO include VALUES("+str(last_insert_id)+","+str(request.form.get('game_id'))+")")
    # print(sql2)
    db.session.execute(sql2)
    sql3 = text("INSERT INTO writereview VALUES("+str(last_insert_id)+","+str(uid)+",\""+str(curDate)+"\")")
    
    # sql3 = text("INSERT INTO write(reviewid, uid, date) VALUES(:rid, :uid, :date)")
    # db.session.execute(sql3, {'rid': last_insert_id, 'uid': uid, 'date':curDate})   
    print("********")
    # print(sql3)
    db.session.execute(sql3)
    db.session.commit()
    return redirect(url_for('home', user_id=uid))
    # return redirect(url_for('home'))

# @userHome_be.route('/write_review', methods=['POST'])
# def write_review():
#     # Here you would handle the review submission
#     print("Review received:", request.form)
#     return redirect(url_for('home'))

@userHome_be.route('/delete_game', methods=['POST'])
def delete_game():
    # Here you would handle the deletion logic
    game_id = request.args.get('game_id')
    user_id = request.args.get('user_id')
    sql = text("DELETE FROM favorite WHERE uid = :user_id AND gameid = :game_id")
    db.session.execute(sql, {'user_id': user_id, 'game_id': game_id})
    db.session.commit()

    return redirect(url_for('home', user_id=user_id))