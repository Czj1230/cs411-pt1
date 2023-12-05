from flask import Blueprint, render_template, jsonify, request
from exts import db
from sqlalchemy import text

game_bp = Blueprint('games', __name__)

@game_bp.route('/getGame')
def getGame():
    print("getGame")
    return {"sdf":"hsdf"}


@game_bp.route('/db', methods=['GET'])
def search_games():
    search_term = request.args.get('query', '')
    category = request.args.get('category', '')
    min_price = request.args.get('minPrice', 0)
    max_price = request.args.get('maxPrice', 0)
    search = "SELECT * FROM game NATURAL JOIN genre WHERE name LIKE :searchid"
    
    if category:
        if category == "action":
            search += " AND genreisaction = 'Y'"
        elif category == "adventure":
            search += " AND genreisadventure = 'Y'"
        elif category == "RPG":
            search += " AND genreisrpg = 'Y'"
        elif category == "simulation":
            search += " AND genreissimulation = 'Y'"
        elif category == "casual":
            search += " AND genreiscasual = 'Y'"
        elif category == "strategy":
            search += " AND genreisstrategy = 'Y'"
        elif category == "indie":
            search += " AND genreisindie = 'Y'"
    if min_price:
        search += " AND price >= " + min_price + ""
    if max_price:
        search += " AND price <= " + max_price + ""
        
    search += " LIMIT 3"
    sql_query = text(search)
    result = db.session.execute(sql_query, {'searchid': f'{search_term}%'})
        

    games = []
    for row in result:
        
        gameid = row[0]
        
        genre_query = text("SELECT * FROM genre WHERE gameid = :searchid")
        genre_result = db.session.execute(genre_query, {'searchid': gameid})
        genres = [genre_row for genre_row in genre_result]
        genres_list = [item for item in genres[0]]
            
        
        picture_query = text("SELECT * FROM extrainfo WHERE gameid = :searchid")
        picture_result = db.session.execute(picture_query, {'searchid': gameid})
        image = [item for item in picture_result]
        image_list = [item for item in image[0]]
        
        game = {
            'gameid': row[0],
            'name': row[1],
            'description': row[2],
            'price': row[6],
            'Indie': genres_list[1],
            'Action': genres_list[2],
            'Adventure': genres_list[3],
            'Casual': genres_list[4],
            'Strategy': genres_list[5],
            'RPG': genres_list[6],
            'Simulation': genres_list[7],
            'Earlyaccess': genres_list[8],
            'Freetoplay': genres_list[9],
            'Sports': genres_list[10],
            'Racing': genres_list[11],
            'Image': image_list[5]
        }
        games.append(game)

    return jsonify(games)

@game_bp.route('/game/<int:game_id>')
def game_detail(game_id):
    user_name = request.args.get('user_name', None)
    user_id = request.args.get('user_id', None)
    # Fetch game details from the database using the game_id
    # ...
    game_query = text("SELECT * FROM game WHERE gameid = :game_id")
    game_result = db.session.execute(game_query, {'game_id': game_id}).fetchone()
    if game_result is None:
        # Handle the case where no game is found
        return "Game not found", 404
    
    rating = text("SELECT * FROM GameAverageRatings WHERE gameid = :game_id")
    rating_result = db.session.execute(rating, {'game_id': game_id}).fetchone()
    
    
    picture_query = text("SELECT * FROM extrainfo WHERE gameid = :searchid")
    picture_result = db.session.execute(picture_query, {'searchid': game_id})
    image = [item for item in picture_result]
    image_list = [item for item in image[0]]
    favorite_status = check_favorite_status(user_id, game_id)
    
    game = {
        'gameid': game_result[0],
        'name': game_result[1],
        'description': game_result[2],
        'image': image_list[5],
        'website': image_list[4],
        'background': image_list[6],
        'favorite_status': favorite_status,
        'avg_rating': rating_result[1]
        # ... other fields ...
    }

    # Render the template with game details
    return render_template('detail.html', game=game, user_name=user_name, user_id=user_id)

@game_bp.route("/db/test/<searchid>", methods=['GET'])
def dbParaTest(searchid):
    sql_query = text("SELECT * FROM game WHERE game_id = :searchid")

    result = db.session.execute(sql_query, {'searchid': searchid})

    response_object = {}
    for row in result:
        response_object[row[0]] = row[1]

    return jsonify(response_object)

@game_bp.route("/db/popular_games", methods=['GET'])
def dbGetPopGames():
    results = db.session.execute(text("SELECT g.name, g.price, e.headerimage, e.website FROM game g NATURAL JOIN extrainfo e WHERE (website AND headerimage) IS NOT NULL ORDER BY g.recommendationcount DESC LIMIT 10"))
    games_list = []
    for game in results:
        games_dict = {
            "name": game[0],
            "price": game[1],
            "header_image": game[2],
            "website": game[3]
        }
        games_list.append(games_dict)
    return jsonify(games_list)


@game_bp.route('/update_favorite', methods=['POST'])
def update_favorite():
    game_id = request.form.get('game_id')
    user_id = request.form.get('user_id')
    
    check = text("SELECT * FROM favorite WHERE uid = :user_id AND gameid = :game_id")
    check_game = db.session.execute(check, {'user_id': user_id, 'game_id': game_id})
    gameExist = check_game.fetchall()
    if len(gameExist) == 0:
        # Update the favorite status in your database based on the provided data
        sql = text("INSERT INTO favorite(uid, gameid) VALUES (:user_id, :game_id)")
        game_add = db.session.execute(sql, {'user_id': user_id, 'game_id': game_id})
        
        db.session.commit()
        response_data = {'Added': True}
        return jsonify(response_data)
        
    else:
        # Remove the favorite file
        sql = text("DELETE FROM favorite WHERE uid = :user_id AND gameid = :game_id")
        game_delete = db.session.execute(sql, {'user_id': user_id, 'game_id': game_id})
        
        db.session.commit()
        response_data = {'Deleted': True}
        return jsonify(response_data)
    

def check_favorite_status(user_id, game_id):
    # Implement this function to check if the game is in the user's favorites
    # Return 'added' or 'deleted' based on the status
    # You can use your database queries for this
    check = text("SELECT * FROM favorite WHERE uid = :user_id AND gameid = :game_id")
    check_game = db.session.execute(check, {'user_id': user_id, 'game_id': game_id})
    gameExist = check_game.fetchall()
    if len(gameExist) == 0:
        return 'None'
    return 'added'  # Replace with actual logic
    