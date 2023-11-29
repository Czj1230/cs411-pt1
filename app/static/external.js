document.addEventListener('DOMContentLoaded', function() {
    var games = [
        { name: 'Game 1', category: 'action', country: 'USA', system: 'Windows', price: 20 },
        { name: 'Game 2', category: 'adventure', country: 'Japan', system: 'Mac', price: 30 },
        // ... more games
    ];

    function searchGames() {
        var searchTerm = document.getElementById('searchBox').value;
        var categoryFilter = document.getElementById('categoryFilter').value;
        var countryFilter = document.getElementById('countryFilter').value;
        var systemFilter = document.getElementById('systemFilter').value;
        var minPrice = document.getElementById('minPrice').value;
        var maxPrice = document.getElementById('maxPrice').value;
    
        var queryURL = '/db?query=' + encodeURIComponent(searchTerm) +
                       '&category=' + encodeURIComponent(categoryFilter) +
                       '&country=' + encodeURIComponent(countryFilter) +
                       '&system=' + encodeURIComponent(systemFilter) +
                       '&minPrice=' + encodeURIComponent(minPrice) +
                       '&maxPrice=' + encodeURIComponent(maxPrice);
    
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
            gameDiv.innerHTML = '<h3>' + game.name + '</h3>' +
                                '<p>Category: ' + game.category + '</p>' +
                                '<p>Country: ' + game.country + '</p>' +
                                '<p>System: ' + game.system + '</p>' +
                                '<p>Price: $' + game.price.toFixed(2) + '</p>';
            resultsDiv.appendChild(gameDiv);
        });
    }

    document.getElementById('searchBox').addEventListener('keyup', searchGames);
    document.getElementById('categoryFilter').addEventListener('change', searchGames);
    document.getElementById('countryFilter').addEventListener('change', searchGames);
    document.getElementById('systemFilter').addEventListener('change', searchGames);
    document.getElementById('minPrice').addEventListener('input', searchGames);
    document.getElementById('maxPrice').addEventListener('input', searchGames);

});
