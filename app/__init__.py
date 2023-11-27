from flask import Flask, render_template, redirect, url_for, request, Blueprint
from app.backend.games import game_bp

app = Flask(__name__)

app.register_blueprint(game_bp)

from app import views

if __name__ == '__main__':
    app.run(debug=True)