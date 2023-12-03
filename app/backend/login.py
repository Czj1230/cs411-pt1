from flask import Blueprint, render_template, jsonify, request, Flask, url_for, redirect
from exts import db
from sqlalchemy import text


userlog = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    # Handle the login form submission
    print("true1")
    if (request.method == 'POST') :
        username = request.form['username']
        password = request.form['password']
        
        userexist = db.session.execute(text
        ("SELECT uid FROM user where uid = " + username + " and password = " + password))
        # print(userexist)

        if userexist != None:
            print("true")
            # Login is successful
            return render_template('index.html')
        else:
            # Login failed
            flash('Invalid username or password.', 'danger')

    return render_template('userlogin.html')


# @user.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         # Handle the signup form submission
#         return redirect(url_for(''))
#     # If it's a GET request, just render the signup template
#     return render_template('signup.html')