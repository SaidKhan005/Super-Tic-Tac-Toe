### Date: 05/04/2023
### Venue: Class
### Attendance: Chris, Said, Kaleb, Flavio, Mohammad

## code review agenda
all functionalities being tested in the code review:
- Test SQL Alchemy
- Final game walkthrough and test
- Final merge with team and pr review
- Addition of features not working to the kanban board and update of backlog if necessary
- Decoupling of server and html would need additional time. Issue has already been added to the kanban board
- Update test files for the lastest codes from arch_user. 

## Walkthrough
what team members did walkthroughes of code/functionalities they added:
- Chris and Flavio worked on storing the game, loading the game from storage, in addition to storing a user object
properly.  
- Mohammed and Said worked on changing the current features to the game logic (make_move logic and checking the winner) The game draw function is still not working. 
- Said and Chris added a few functionalities to the server (start_game, login, welcome, and sign_up methods). Also made 
changes to the current functionalities (make move method).
- Kaleb worked on getting the Html templates ready, index, load_game, and user_info template got updated. 
- Flavio worked on implementing SQL Alchemy in his database architecture .

## what the walkthrough entailed

- Chris and Flavio discussed their latest implementation of SQL Alchemy in their latest code. They went through starting a game
with users made before. 

- Kaleb has shown the changes he made in the templates, the index, user_info, and load_game template now fits with the super tic tac toe
game and displays a 9x9 board and not a 3x3 anymore. 

- Said and Mohammad worked together to get the make_move and check_winner functionality working. The new make_move method
now works with a 9x9 board instead of a 3x3 board. The method was modified to ensure that move were only made in valid 
positions. As for the check winner method, a helper method was written to check for winner in each sub_board, whic was used
to determine the winner in the overall board. They also showed the changes they made to check for a game draw. 

- Said and Chris worked together to get the server to work with all the changes made to the other modules. Like the welcome 
and login function to work with the welcome and login html provided by Kaleb, the start_game function properly starts the
game when two username are collected from the html form. If the username are recognised in the database, their user objects
are retrieved as well. When retrieved, they are assigned symbols. Then the game can begin. Other features like players (which
is a list that stores the two players that are ready to play) and player which is used to store user objects. 

## code sent by team members on discord and how others have gone through it
- The Game logic, server, arch_user, database and html files were all shared on discord as progress was made. To ensure
that changes made in one module would work perfectly with its intended modules. An example would be the server and user module
communicating back and forth through user creation, checking if usernames are valid, and getting a somewhat list of user
objects. Basically anything that has to do with users is done in the user module to ensure loose coupling.


## functionality test (correctness test)
what functionalities were tested e.g user login or game reload
* The user login functionality was tested
* User object storage functionality was tested
* The user creation functionality was tested
* The game creation functionality was tested
* Game storage and loading was tested
* The html displays were tested
* The make_move functionality was tested
* The check_winner and draw functionalities were tested

## Issues with  particular functionalities
* There is an issue with the draw functionality. When the game ends in a draw (not when all boards are filled) the draw function in the 
server is not called. Still looking on fixing it if there is time to do so.
* Old games are not being brought back properly. When a game between two users is incompleted and closed, when the game between the same users is reopned, a new game starts. 
* Everything else seemed to work just fine.

## Does this particular functionality works with the whole program or if something broke
* The user login and user object storage functionalities did break the whole program. But once again, after they were resolved 
it did not do so anymore. *These functionalities will be looked at again in the next code review meeting*

## Improvements arising from functionality test:
- No new improvements required. 

## Issues arising from code review:
Mention issues that arise from any added functionality. Add the issue number and description
* The draw functionality not working issue. Issue #70
* Old games are not loading, game id seems to be different on every tests. Issue #77
* Both were also added to the kanban board as software implementations.

## Coding style and conventions
**Comment on whether any code reviewed follows the current conventions we have or changes need to be made.**
* Code reviewed followed current conventions we have. No changes needed

- Comment on docstrings style agreement 
**Docstrings need to be added/updated to the following modules;** 
- Server
- DBOperations
- Game

## Team agreement and deadline
**Explain what the team agreed upon for this particular code review.** 
* No more deadlines. Team has agreed to finish up their current tasks not set any more deadlines. 

## That is all we were able to accomplish today!
