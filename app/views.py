from app import app

from flask import render_template, request, session, redirect
from sqlalchemy import text
from exts import db


@app.route('/')
def index():
    return render_template('index.html', user_id=None)

@app.route('/6')
def suc():
    user_id = request.args.get('user_id', '-1')
    user_name = request.args.get('user_name', '-1')
    print(f"user_id: {user_id}, user_name: {user_name}")  # Add this line for debugging
    return render_template('index.html', user_id=user_id, user_name=user_name)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/second_page')
def about():
    user_name = request.args.get('user_name', '-1')
    user_id = request.args.get('user_id','-1')
    return render_template('about.html', user_name=user_name, user_id=user_id)

@app.route('/search_engine')
def search():
    user_name = request.args.get('user_name','-1')
    user_id = request.args.get('user_id','-1')
    return render_template('search.html', user_name = user_name, user_id = user_id)

#within app.route add the html page we are doing changes to
@app.route('/register')
# def is normally how we define a function in python
def register():
    return render_template('register.html')

@app.route('/registerV')
def registerV():
    return render_template('registerV.html')

@app.route('/newpage')
def newpage():
    return render_template('newpage.html')


@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

from .backend.userHome import get_favorite_games
@app.route('/userHome')
def home():
    user_id = request.args.get('user_id','-1')
    user_name = request.args.get('user_name', '-1')
    # print(user_id)
    pre_sql = text("SELECT * FROM user WHERE uid = :uid")
    userNameExist = db.session.execute(pre_sql, {'uid': user_id})
    userNameCnt = userNameExist.fetchall()
    number_of_rows = len(userNameCnt)
    if(user_id== "-1" or user_id=="" or number_of_rows==0):
        # print("==============")
        return render_template('index.html', show_alert=True)
    games = get_favorite_games(int(user_id))  # This function will fetch favorite games

    return render_template('userHome.html', user_id=user_id, user_name=user_name, games=games)



@app.route('/logout')
def logout():
    # Perform logout actions here, such as clearing the user's session
    # You can use session.pop('user_id', None) to clear the user's session
    session.pop('user_id', None)
    # Redirect the user to the homepage or any other desired page after logout
    return redirect('/')