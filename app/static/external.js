document.addEventListener('DOMContentLoaded', function() {

    function searchGames() {
        var searchTerm = document.getElementById('searchBox').value;
        var categoryFilter = document.getElementById('categoryFilter').value;
        var minPrice = document.getElementById('minPrice').value;
        var maxPrice = document.getElementById('maxPrice').value;
    
        var queryURL = '/db?query=' + encodeURIComponent(searchTerm);

        // Only append the filters to the URL if they have values
        if (categoryFilter) {
            queryURL += '&category=' + encodeURIComponent(categoryFilter);
        }
        if (minPrice) {
            queryURL += '&minPrice=' + encodeURIComponent(minPrice);
        }
        if (maxPrice) {
            queryURL += '&maxPrice=' + encodeURIComponent(maxPrice);
        }
    
        fetch(queryURL)
            .then(response => response.json())
            .then(games => {
                console.log(games); // Log the JSON data
                displayGames(games);
            })
            .catch(error => console.error('Error:', error));

    
    }


    function displayGames(games) {
        var resultsDiv = document.getElementById('searchResults');
        resultsDiv.innerHTML = ''; // Clear previous results

        if (!Array.isArray(games) || games.length === 0) {
            resultsDiv.innerHTML = '<p>No games found or invalid data format.</p>';
            return;
        }

        games.forEach(function(game) {
            var gameDiv = document.createElement('div');
            gameDiv.className = 'game-item';

            gameDiv.innerHTML = '<h3>' + game.name + '</h3>';
            var img = document.createElement('img');
            img.src = game.Image;
            img.alt = "Game Image";
            gameDiv.appendChild(img)
            gameDiv.innerHTML += '<p>Description: ' + game.description + '</p>' +
                                '<p>Price: $' + game.price.toFixed(2) + '</p>';
            gameDiv.innerHTML += '<p>Category: ';
            if (game.Indie == 'Y') {
                gameDiv.innerHTML += '<p>Indie' + '</p>';
            }
            if (game.Action == 'Y') {
                gameDiv.innerHTML += '<p>Action' + '</p>';
            }
            if (game.Adventure == 'Y') {
                gameDiv.innerHTML += '<p>Adventure' + '</p>';
            }
            if (game.Casual == 'Y') {
                gameDiv.innerHTML += '<p>Casual' + '</p>';
            }
            if (game.Strategy == 'Y') {
                gameDiv.innerHTML += '<p>Strategy' + '</p>';
            }
            if (game.RPG == 'Y') {
                gameDiv.innerHTML += '<p>RPG' + '</p>';
            }
            if (game.Simulation == 'Y') {
                gameDiv.innerHTML += '<p>Simulation' + '</p>';
            }
            if (game.Earlyaccess == 'Y') {
                gameDiv.innerHTML += '<p>Early-access' + '</p>';
            }
            if (game.Freetoplay == 'Y') {
                gameDiv.innerHTML += '<p>Free-to-play' + '</p>';
            }
            if (game.Sports == 'Y') {
                gameDiv.innerHTML += '<p>Sports' + '</p>';
            }
            if (game.Racing == 'Y') {
                gameDiv.innerHTML += '<p>Racing' + '</p>';
            }
            
            gameDiv.innerHTML += '</p>';
            var gameLink = document.createElement('a');
            gameLink.href = '/game/' + game.gameid + 
                '?user_name=' + encodeURIComponent(user_name) +
                '&user_id=' + encodeURIComponent(user_id);
            gameLink.textContent = game.name;
            gameDiv.appendChild(gameLink)
            resultsDiv.appendChild(gameDiv);
            
        });
    }

    document.getElementById('searchBox').addEventListener('keyup', searchGames);
    document.getElementById('categoryFilter').addEventListener('change', searchGames);
    document.getElementById('minPrice').addEventListener('input', searchGames);
    document.getElementById('maxPrice').addEventListener('input', searchGames);

});
