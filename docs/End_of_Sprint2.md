## End of Sprint 2 Document

**Project Overview:**
Our team did not successfully complete the development of a Super Tic Tac Toe game server, 
involving five key modules: User, Server, Game Logic, Store, and HTML. We were unable to get the 
draw functionality working properly. But other than that, our collaborative effort has resulted in a good enough
functional game server that seamlessly integrates these components to provide an engaging gaming experience.

**Main Functionalities:**

1. **User login:**
   - Upon launching the game server, a welcome page is presented with a button to the login page
   - In the login page is presented a form to collect two usernames for the players ready to play

2. **SignUp:**
    - If you would like to create a new player, there is a signup link on the login page. The signup page provides
    a form to collect user information such as username and age.

3. **Player Storage:**
   - After two users have been created, they are stored to the database.

4. **Symbol Assignment:**
    - After the usernames have been validated, their user objects are retrieved from the database and symbols 'X' or 'O'
    are assigned to each player respectively.
   
5. **Get Users:**
    - This feature was added so that the user object of the players could be retrieved. It was also because of this feature that the logic used
    in the database had to be changed to SQLAlchemy. Without this feature we won't be able to assign symbols to users because all we had was strings,
    and we can't assign symbols to strings.

6. **Start Game:**
    - The super Tic Tac Toe game commences with the assigned symbols, and players take turns making moves on the new 9x9 game board.
    - information displayed on the start game page includes; game_id, current_player, and the board

7. **Gameplay:**
   - Changes were made to the make_move logic to accommodate for the new 9x9 game board.
   - Moves are made on the board only in valid positions. 
   - If there is a winner in the sub_board no further move can be made on that board
   - If there is a winner, the winner_page is displayed
   - If the board is not completely filled and no further moves can be made, meaning there is a winner or draw on each 
   sub_board but in a way that there is no overall winner, the draw_page doesn't get displayed.
   - But if the game board is completely filled then the draw_page is displayed, and that is the error we have with the draw functionality.

8. **Game Outcome:**
   - The game concludes when a player achieves victory or when the board is filled, resulting in a draw.

9. **Game Information Storage:**
   - Implemented functionality to store game information in the database.
   - Stored data includes:
     - Game ID
     - Player information
     - Number of moves
     - Winner (if applicable)
     - Game board matrix
   - Upon creation of a game, all relevant information is stored in the database.
   - Updates are made to the stored game information when the game ends, reflecting changes such as board 
   updates, move count adjustments, and winner identification.

10. **Game Data Retrieval and Loading:**
   - Developed functionality to properly load a game from storage.
   - Enables retrieval of stored game data to display game information given the game_id

11. **Delete User Method:**
   - Created a method to delete user data from the system.
   - Still not in use due to complications that arose during implementation.
   - Problems with integration into the current system was not resolved.

12. **Reset Game Route:**
   - Implemented a route to reset the game in the event of a draw.
   - Allows for the game to be reset, enabling a new opportunity for a winner to be determined.

**Project Stability and Future Considerations:**
At the conclusion of sprint 2, the project's master branch is in a stable state. The implemented
functionalities have been thoroughly tested to ensure a smooth gaming experience.  Although we could not add other intended
software implementations due to time constraints, the system have the functionalities of a super Tic Tac Toe game. The collaboration between 
the modules (User, Server, Game Logic, Store, and HTML) has been successful, demonstrating the effectiveness of  the integrated system. Despite the faults 
with the draw implementations, the project remains stable and functional.