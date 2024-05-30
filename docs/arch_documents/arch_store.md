# **Super Tic Tac Toe Database**

The persistence solution for this Python project uses a relational database to store
all the data records. It makes use of SQLite3 to accomplish this.


## Functions
- add_player(player): It stores the given player on the database.
  * player: Player object to be stored 


- add_game(game): It stores the given game on the database.
  * game: Game object to be stored


- delete_player(old_username): It deletes the player with matching username from the database.
  * old_username (str): Username of the player to be deleted


## UML Diagram
![UML](../Uml_diagrams/store_uml.png)