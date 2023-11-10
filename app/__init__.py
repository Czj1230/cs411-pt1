from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

from app import views
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/second_page')
def about():
    return render_template('about.html')

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

if __name__ == '__main__':
    app.run(debug=True)