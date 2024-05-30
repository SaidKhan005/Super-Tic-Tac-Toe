# Comprehensive Description of an Imagined Interaction with the System

I would have liked the super Tic Tac Toe game to have a leadership board, so that there could be a tournament for the top 10 players.
On the leadership board, information like the players' usernames, number of games, number of wins, number of losses and number of draws
will be displayed.
* When on the login page, there will be a button to start a tournament. When clicked, it takes you to the leadership board page where you can 
see a list of all players and their ranks. 
* When on this page, there will be another button that says let's begin. When clicked, the tournament begins.
* The last player standing is declared the ultimate winner and is added to the tournament board.

# Implementation Steps
1) A button to start a tournament is added to the login html template
2) An @app.route('/start_tournament') is added to the server for when the button is clicked.
3) In this function, the leadership board template is simply returned.
4) The database takes care of storing the necessary information into the leadership table
5) When the leadership board template is displayed, there is a button that says let's begin. When clicked, it goes to the
lets_begin function in the server.
6) In this function, the top 10 ranking players are gotten from the database as a list by making a query to the database. This isn't done
directly from the server, but from game logic. When this data (user objects) is retrieved, the list of players are passed to a split_players_into_list 
function that takes care of splitting players into pairs of 2 randomly and store them in a list. The 5 lists are added to another list giving you 
a list of lists which is returned
7) When this list is returned, using a for_loop, the first list of players is passed to the manage_tournament function.
8) The manage_tournament function creates a game object with the list provided. And the game plays as per usual (this implementation is working in the current system,
so is not discussed here)
9) At the end of the game when there is a winner, the winner is added to the global quarter_finals list. Then the function exist and the next list of players are passed
and the same process repeats until all lists have been passed.
10) After the iteration of the for_loop, the players in the quarter_finals list are split as described in step 6. The function checks for even or odd 
number of players and splits accordingly. Because at this point, the number of players are odd, a list has one player. This player is randomly paired with a player from the previous stage of the game.
That is, if the player is in the semi_finals list, the player is paired with another player from the quarter_finals list who is not already in the current (semi_final) list.
11) Steps 7 through 10 are repeated, but this time the winners are added to the global semi_finals list. It is not added to the quarter_finals list because of a check
such as this "if quarter_finals == []".
12) After the iteration for handling the semi_finals, another iteration is used to handle the finals. Once again following steps 7 through 10.
13) The ultimate winner is then stored in the tournament table in the database.
14) After the tournament has ended, the quarter_finals, semi_finals and finals list are set to []. To enable for the next tournament.

With this implementation I can imagine the tournament functionality could have worked. Since not tested, there might be minor errors that need to be addressed.