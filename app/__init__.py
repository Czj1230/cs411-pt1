from flask import Flask, render_template, redirect, url_for, request, Blueprint, jsonify
from app.backend.games import game_bp
import config
from exts import db

from app.backend.userHome import userHome_be
from app.backend.login import userlog

app = Flask(__name__)

app.config.from_object(config)

# allow track and modify database
db.init_app(app)

app.register_blueprint(game_bp)
app.register_blueprint(userHome_be, url_prefix='/userHome')
app.register_blueprint(userlog, url_prefix='/userLogin')

from app import views

if __name__ == '__main__':
    print("__init__")
    app.run(debug=True)