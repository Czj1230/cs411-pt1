from app import app
from flask import render_template

@app.route('/')
def index():
    print("index")
    return render_template('index.html')

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