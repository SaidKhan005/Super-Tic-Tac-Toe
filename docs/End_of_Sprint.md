## End of Sprint 1 Document

**Project Overview:**
Our team has successfully completed the development of a Tic Tac Toe game server, 
involving five key modules: User, Server, Game Logic, Store, and HTML. This collaborative 
effort has resulted in a functional game server that seamlessly integrates these 
components to provide an engaging gaming experience.

**Main Functionalities:**

1. **User Information Collection:**
   - Upon launching the game server, a user form is presented to collect essential 
   information from players, including their username and age.

2. **Player Assignment:**
   - After two users have been created, the game automatically starts.
   - Players are randomly assigned symbols, X or O, ensuring a fair and unpredictable 
   gaming experience.

3. **Gameplay:**
   - The Tic Tac Toe game commences with the assigned symbols, and players take turns 
   making moves on the game board.

4. **Game Outcome:**
   - The game concludes when a player achieves victory or when the board is filled, 
   resulting in a draw.

**Additional Functionalities Implemented:**

1. **Game Information Storage:**
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

2. **Data Retrieval and Loading:**
   - Developed functionality to properly load a game from storage.
   - Enables retrieval of stored game data to display (previous) game information 

3. **Delete User Method:**
   - Created a method to delete user data from the system.
   - Currently not in use due to complications that arose during implementation.
   - Potential for future integration once complications are resolved.

4. **Reset Game Route:**
   - Implemented a route to reset the game in the event of a draw.
   - Allows for the game to be reset, enabling a new opportunity for a winner to be determined.

**Project Stability and Future Considerations:**
At the conclusion of this sprint, the project's master branch is in a stable state. The implemented
functionalities have been thoroughly tested to ensure a smooth and  error-free gaming experience. 
The collaboration between the modules (User, Server, Game Logic, Store, and HTML) has been successful, 
demonstrating the effectiveness of  the integrated system. Despite the temporary exclusion of the delete 
user method, the project remains stable and functional. Moving forward, addressing the complications with the 
delete user method and potentially integrating it into the system would be beneficial. Additionally, ongoing 
testing and maintenance will ensure the continued reliability and performance of the game server.