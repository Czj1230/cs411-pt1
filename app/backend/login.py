from flask import Blueprint, render_template, jsonify, request, Flask, url_for, redirect, flash
from exts import db
from sqlalchemy import text


userlog = Blueprint('user', __name__)

@userlog.route('/login', methods=['GET', 'POST'])
def login():
    # Handle the login form submission

    if (request.method == 'POST') :
        username = request.form['username']
        password = request.form['password']
        
        sql = text("SELECT * FROM user WHERE username = :username AND password = :password")
        userexist = db.session.execute(sql, {'username': username, 'password': password})
        result = userexist.fetchall()
        number_of_rows = len(result)

        print(number_of_rows)
        print(result)
        print(type(result))
        if number_of_rows != 0:
            # Login is successful
            return render_template('index.html', user_id = result[0][0], user_name=result[0][1])
        else:
            # Login failed
            flash('Invalid username or password.', 'danger')

    return render_template('userlogin.html', show_alert=True)


# @user.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         # Handle the signup form submission
#         return redirect(url_for(''))
#     # If it's a GET request, just render the signup template
#     return render_template('signup.html')