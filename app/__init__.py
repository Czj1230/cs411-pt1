from flask import Flask, render_template, redirect, url_for, request, Blueprint
from app.backend.games import game_bp
import config
from exts import db
from flask import request, jsonify
from sqlalchemy import text

app = Flask(__name__)



app.config.from_object(config)
# allow track and modify database
db.init_app(app)



app.register_blueprint(game_bp)



from app import views

if __name__ == '__main__':
    print("__init__")
    app.run(debug=True)