## Code Review Agenda
All functionalities being tested in the code review:
- Perform a code overview from an outsider's percpective.
- User creation and management
- Database operations
- Game logic and state management
- Server functionalities
- Unit tests

## Walkthrough
- No walkthrough conducted today. The agenda was focused on functionality testing and overview

### Code Overview
- **Purpose:** Understand the system as a whole from an outsider's perspective.
- **Reviewed By:** All team members collectively.
- **Key Points:**
  - Discussed the overall structure and interactions between modules.
  - Identified key functionalities and their implementations.
  - Ensured cohesion and coherence across modules.
  - Explored how each module contributes to the system's functionality.

### Server Module
- **Functionality:** Handles requests and communication between client and server.
- **Reviewed By:** Said and Chris
- **Key Points:**
  - Implemented methods for user login, signup, and starting the game.
  - Interacts with other modules for user management and game state.
  - Utilizes HTML templates for user interface.

### Game Module
- **Functionality:** Implements the Tic Tac Toe game logic and state management.
- **Reviewed By:** Mohammad and Said
- **Key Points:**
  - Allows players to make moves on a 9x9 grid, considering sub-boards.
  - Checks for winners in sub-boards and overall board state.
  - Provides methods for storing and loading game information from the database.

### Database Module
- **Functionality:** Manages database operations for users and game information.
- **Reviewed By:** Chris and Flavio
- **Key Points:**
  - Implements SQLite database operations for storing user and game data.
  - Ensures data integrity and proper error handling.
  - Provides methods for adding, deleting, and updating user and game information.

### User Module
- **Functionality:** Represents users in the system and provides user management functionalities.
- **Reviewed By:** Chris and Flavio
- **Key Points:**
  - Handles user creation, deletion, and storage in the database.
  - Ensures proper interaction with the database for user-related operations.
  - Implements methods for checking player existence and managing player statistics.
 
### Unit Tests
- Current Unit tests work but are not perfect. This has been added to the backlog but we might not have enough time to do this

## Functionality Test (Correctness Test)
- Tested functionalities including user login, signup, game state management, and database interactions.
- Ensured proper error handling and data validation.

## Issues and Resolutions
- No major issues reported during the code review.
- Minor issues related to user login and game state management were resolved during the meeting.
- Like mentioned before Kaleb will do a decoupling for the server and Html which we will review on Friday April 5th

## Coding style and conventions
Code reviewed followed current conventions we have. No changes needed

If we have time before friday we will add updated docstring to the following:
Server
DBOperations
User
Game

## Improvements and Agreements
- Code follows SOLID principles and provides cohesive functionalities. Decoupling for server and html to be done by Kaleb.
- Further testing required for robustness and edge cases.
- Enhancements planned for logging and documentation However, we will first focus on documentation required for sprint 2.

## Team Agreement and Deadline
- Task assignments and pull request deadlines recorded in April 3rd meeting notes.
- Final pull request will be done on April 5th.

## Conclusion
The code review session addressed  'the bare minimum and key functionalities' and interactions between modules. The modules provide necessary functionalities for user management, game logic, and database operations. Further testing and documentation enhancements are needed for completeness and robustness.

