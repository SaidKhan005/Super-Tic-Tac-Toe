### Date: 01/04/2023
### Venue: Class
### Attendance: Chris, Said, Kaleb, Flavio, Mohammad

## code review agenda
all functionalities being tested in the code review:
- User creation works fine
- Database
- Extension form tic-tac-toe to super tic-tac-toe
- Game logic
- User login (these are already from created users)

## Walkthrough
what team members did walkthroughes of code/functionalities they added:
- Chris and Flavio worked on storing the game, loading the game from storage, in addition to storing a user object
properly. 
- Mohammed and Said worked on changing the current features to the game logic (make_move logic and checking the winner)
- Said and Chris added a few functionalities to the server (start_game, login, welcome, and sign_up methods). Also made 
changes to the current functionalities (make move method)
- Kaleb worked on getting the Html templates ready (welcome and login htmls)
- Chris added a few features to the user module (assign_symbol, check_players and get_users) and changed the code structure

## what the walkthrough entailed
Chris explained to us how the user module interacts with the database to store users. Earlier, symbols were assigned 
to users when the users were created. But inorder for the user module to work with the new implementations, changes had
to be made. This changes include;
* Moving the assignment of symbols to users to be done in a separate class method. This was so that user creation should 
not be limited to two. At the end of sprint 1, the game only worked after two users were created and assigned symbols
during creation. But now that yhe user object can be stored and retrieved from the database, the need to assign the symbols
separately was required.
* A check_player class method was added to be used by the server to checked if the two usernames entered during login are
actually usernames stored in the database. And if they are, the get_users method come into play.
* The get_users method returns the user object of the users after the two usernames entered during login are confirmed to 
actually exist

- Chris and Flavio discussed new ways to implement the database. The current implementations did not allow us to easily store
user object, which was essential to getting the user login functionality working. So a new approach was suggested. 
We decided to use SQLAlchemy as the new structure for the database.

- Kaleb was tasked with the welcome and login templates, which he finished quickly due to his proficiency in html coding
The welcome page was now the page that displays when the game starts running, instead of the sign_up page. After the welcome
page comes the login page, where two usernames are required as input to start the game. if there are no players currently
in the database or new players wish to be added, there is a link to do so. This then takes you to the sign_up page from 
sprint 1.

- Said and Mohammad worked together to get the make_move and check_winner functionality working. The new make_move method
now works with a 9x9 board instead of a 3x3 board. The method was modified to ensure that move were only made in valid 
positions. As for the check winner method, a helper method was written to check for winner in each sub_board, whic was used
to determine the winner in the overall board.

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
* There was an issue with the user object storage functionality, but by the time this code review was writen, the issue
was resolved by Chris. It will be checked again on the next code review.
* There is an issue with the draw functionality. When the game ends in a draw (not when all boards are filled) the draw function in the 
server is not called. Still looking on fixing it if there is time to do so.
* The user login functionality was also not working, but by the time this code review was writen, it was resolved by Chris.
Will be looked at again in the next code review meeting.
* Everything else seemed to work just fine.

## Does this particular functionality works with the whole program or if something broke
* The user login and user object storage functionalities did break the whole program. But once again, after they were resolved 
it did not do so anymore. *These functionalities will be looked at again in the next code review meeting*

## Improvements arising from functionality test:
- for each added functionality can we consider principles such as DRY, SOLID, dependency, de-coupling, cohesion, coherence and standard patterns for example decouple the server and html modules
- To reduce cohesion and promote decoupling, kaleb is going to attempt to separate the server api calls from the html logic 
- To de-couple the modules, Chris kept everything related to users in the user module, so that any changes made will only be made
in one place.

## Issues arising from code review:
Mention issues that arise from any added functionality. Add the issue number and description
* A User login issue. Issue #69
* The draw functionality not working issue. Issue #70
* Both were also added to the kanban board as software implementations.

## Coding style and conventions
**Comment on whether any code reviewed follows the current conventions we have or changes need to be made.**
* Code reviewed followed current conventions we have. No changes needed

- Comment on docstrings style agreement 
**Docstrings need to be added to the following modules;** 
- Server
- DBOperations
- User
- Game

## Team agreement and deadline
**Explain what the team agreed upon for this particular code review.** 
* After this code review, the team agreed that the functionalities that had issues today will be looked at again and try
to get is settled before April 3. If it cannot be settled, it will be left as is.
* Task assignment were done in the April 1st meeting notes.
* Deadlines were also set in the April 1st meeting notes.

## That is all we were able to accomplish today!
