from app import app
from flask import render_template, request
from sqlalchemy import text
from exts import db

@app.route('/')
def index():
    return render_template('index.html', user_id=None)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/second_page')
def about():
    return render_template('about.html')

@app.route('/search_engine')
def search():
    return render_template('search.html')

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
    # print(user_id)
    pre_sql = text("SELECT * FROM user WHERE uid = :uid")
    userNameExist = db.session.execute(pre_sql, {'uid': user_id})
    userNameCnt = userNameExist.fetchall()
    number_of_rows = len(userNameCnt)
    if(user_id== "-1" or user_id=="" or number_of_rows==0):
        # print("==============")
        return render_template('index.html', show_alert=True)
    games = get_favorite_games(int(user_id))  # This function will fetch favorite games
    return render_template('userHome.html', games=games, uid=user_id)


