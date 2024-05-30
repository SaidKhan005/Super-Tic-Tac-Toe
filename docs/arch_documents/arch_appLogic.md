Architecture Document for Super Tic-Tac-Toe Application

Module: SuperTicTacToeGame

Overview:
The SuperTicTacToeGame module is responsible for managing the core logic of the Super Tic-Tac-Toe game. It encapsulates the functionalities related to making moves, checking for wins and draws, and maintaining the game state.

Classes and Methods:
Class: SuperTicTacToeGame

game_state:
Purpose: Makes the grid for the game. 

Constructor (__init__ method):
Purpose: Initializes the Super Tic-Tac-Toe game state.
Parameters: None.

make_move Method:
Purpose: Handles a player's move in the game.
Parameters: Takes the player making the move, smaller grid index, row, and column as input.
Returns: Returns a boolean indicating whether the move was successful.

is_valid_move Method:
Purpose: Checks if a move is valid.
Parameters: Takes the smaller grid index, row, and column as input.
Returns: Returns a boolean indicating whether the move is valid.

update_game_state Method:
Purpose: Updates the game state after a valid move.
Parameters: Takes the player making the move, smaller grid index, row, and column as input.
Example: Modifies the internal data structure to reflect the player's move.

determine_next_move Method:
Purpose: Determines the next move in the larger grid (if applicable).
Parameters: Takes the smaller grid index, row, and column of the last move as input.
Example: Calculates the next valid move based on the last player's move.

check_win Method:
Purpose: Checks for a win in the smaller grid.
Parameters: Takes the player making the move and the smaller grid index as input.
Returns: Returns a boolean indicating whether there is a win.

check_draw Method:
Purpose: Checks for a draw in the smaller grid.
Parameters: Takes the smaller grid index as input.
Returns: Returns a boolean indicating whether there is a draw.

![UML](../Uml_diagrams/UML_AppLogic.png)

