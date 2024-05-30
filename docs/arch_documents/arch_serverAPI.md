# **Tic Tac Toe Web Application**

This is a python-based WSGI server, that uses the URL endpoint routing provided by the Bottle web framework
It uses a Bottle application to implement a Super Tic Tac Toe game with a web-based user interface.

Routes:
- GET /: Displays the User info page.
- POST /make_move/<position:int>: Handles player moves on the Tic Tac Toe board.
- POST /submit: Processes user information collected
- GET /reset_game: Resets the game to its initial state.
- ...

Below is a UML diagram showing the server architecture interface


![UML](../Uml_diagrams/arc_server.jpg)
