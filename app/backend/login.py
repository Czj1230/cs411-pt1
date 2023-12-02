from flask import Blueprint, render_template, jsonify, request, Flask, url_for, redirect
from exts import db
from sqlalchemy import text


userlog = Blueprint('user', __name__)

@user.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle the signup form submission
        return redirect(url_for('main.about'))
    # If it's a GET request, just render the signup template
    return render_template('signup.html')

@user.route('/login', methods=['GET', 'POST'])
def login():
    # Handle the login form submission
    # ...
    return render_template('login.html')