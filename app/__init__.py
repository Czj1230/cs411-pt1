from flask import Flask, render_template, redirect, url_for, request, Blueprint, jsonify
from app.backend.games import game_bp
import config
from exts import db
from sqlalchemy import text

from app.backend.userHome import userHome_be
from app.backend.login import userlog

app = Flask(__name__)

app.config.from_object(config)

# allow track and modify database
db.init_app(app)

app.register_blueprint(game_bp)
app.register_blueprint(userHome_be, url_prefix='/userHome')
app.register_blueprint(userlog, url_prefix='/userLogin')



def create_trigger():
    print("HERE!!")
    drop_tri = text("DROP TRIGGER IF EXISTS after_insert_review;")
    db.session.execute(drop_tri)
    print("drop trigger")

    trigger_sql = text("""
        
        CREATE TRIGGER IF NOT EXISTS after_insert_review
        AFTER INSERT ON review
        FOR EACH ROW
        BEGIN
            IF new.comment IS NULL THEN 
                UPDATE review 
                SET comment="This user has no comments yet." 
                WHERE reviewid = new.reviewid;
            END IF;
        END;
    """)
    db.session.execute(trigger_sql)
    db.session.commit()
    print("ADD TRIGGER")
    

def create_stored_procedure():
    stored_procedure_sql = text("""
        DELIMITER //
        CREATE PROCEDURE IF NOT EXISTS AverageGameRatings()
        BEGIN
            DECLARE done INT DEFAULT 0;
            DECLARE currGameId INT;
            DECLARE gameCursor CURSOR FOR SELECT DISTINCT gameid FROM game;

            DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

            DROP TABLE IF EXISTS GameAverageRatings;

            CREATE TABLE GameAverageRatings (
                gameid INT,
                avgRating REAL
            );

            OPEN gameCursor;

            REPEAT
                FETCH gameCursor INTO currGameId;

                IF NOT done THEN
                    INSERT INTO GameAverageRatings(gameid, avgRating)
                    SELECT G.gameid, AVG(R.rating) FROM review R NATURAL JOIN game G
                    WHERE G.gameid = currGameId 
                    GROUP BY G.gameid;
                END IF;
            UNTIL done END REPEAT;

            CLOSE gameCursor;

        END //
        DELIMITER ;
    """)

def run_startup_tasks():
    with app.app_context():
        create_trigger()
        create_stored_procedure()

# Call the startup function before running the app
run_startup_tasks()


from app import views

if __name__ == '__main__':
    print("__init__")
    app.run(debug=True)