## General Framework for an online server based Game
- In this document we use the Super Tictactoe architecture we have to design a more generalized architecture and make comparisons between the two.
- The following are the Five modules that would be required to have an online Server Game running.
- The overall archtecture and Uml diagram can be found here [Architectural Description and UML Diagram](project_architecture.md)
## 1. App Logic Module
### Existing Super Tic Tac Toe Framework
- Contains game-specific logic for super tic-tac-toe, including rules, state management, and various algorithms (e.g., for checking the game winner).
- [Architectural Description and UML Diagram](../arch_documents/arch_appLogic.md)
- The existing game logic can serve as a good starting point for the generalized framework. However, to make it more flexible and reusable, we'll need to refactor it into smaller, more modular components that can be easily adapted to different types of games.
### Interface changes for the Super Tic Tac Toe Framework for redesign:
- Refactor specific game logic into more generic functions or classes.
- Break down the existing monolithic logic into smaller, reusable components.
- Ensure that interfaces focus on initializing game state, validating moves, and determining outcomes.

### Redesigned Framework
- The core logic is abstracted to support various types of games, allowing for easy adaptation to different game rules and mechanics. We'll organize the logic into separate functions or classes for initializing game state, handling player moves, and checking for game outcomes. These components will be designed to be modular and extensible, making it easy to add new features or customize existing ones for different games.
- [Architectural Description and UML Diagram](appLogic_Architecture.md)

### Interface Changes a Game Designer Would Need to Make
- Refactor your own specific game logic into generic functions/classes. Interfaces should focus on initializing game state, validating moves, and determining outcomes.

## 2. User Logic Module
### Existing Super Tic Tac Toe Framework
- Represents a user in the system and provides functionalities for user management
- [Architectural Description and UML Diagram](../arch_documents/arch_user.md)

### Redesigned Framework
- The user module remains largely unchanged in the redesigned framework. However, it's refactored to ensure its reusability in a generalized game framework. The class ArchUser is designed to encapsulate user information and provide methods for user management. It can be easily adapted to handle users in different types of games.
- [Architectural Description and UML Diagram](userLogic_Architecture.md)

### Interface Changes a Game Designer Would Need to Make
- Ensure that the ArchUser class provides generic methods for user management that can be easily customized for different games.
- Design the user module to be modular and extensible, allowing for the addition of new functionalities or modifications without significant changes to the existing codebase.

## 3. Storage Logic Module

### Existing Super Tic Tac Toe Framework
- Handles database operations related to storing player information, game data, and managing game statistics.
- [Architectural Description and UML Diagram](../arch_documents/arch_store.md)

### Redesigned Framework
- The database operations module is refactored to support the generalized framework. It remains responsible for storing player and game data in the database, but the implementation is modified to make it more flexible and reusable. Functions are designed to handle generic game data, allowing them to be adapted for different types of games
- [Architectural Description and UML Diagram](storageLogic_Architecture.md)

### Interface Changes a Game Designer Would Need to Make
- Ensure that database operations support generic game data, allowing them to be easily integrated into different game implementations.
- Design functions to handle common database operations, such as storing player information, game state, and updating player statistics.
- Make the database operations module flexible and extensible, allowing for the addition of new features or modifications without significant changes to the existing codebase.

## 4. Server Logic Module

### Existing Super Tic Tac Toe Framework
- The web application module is responsible for handling user interactions, managing game flow, and rendering HTML templates for the user interface.
- [Architectural Description and UML Diagram](../arch_documents/arch_serverAPI.md)

### Redesigned Framework
- The existing web application module is refactored to support the generalized framework. It abstracts game-specific logic into reusable components, making it adaptable to different types of games. The module is organized into functions that handle user actions, game state management, and rendering HTML templates.

[Architectural Description and UML Diagram](serverLogic_Architecture.md)

### Interface Changes a Game Designer Would Need to Make
- Ensure that the web application module supports generic game logic, allowing it to be easily integrated into different game implementations.
- Design functions to handle user actions, game state management, and rendering HTML templates in a modular and reusable manner.
- Make the module flexible and extensible, allowing for the addition of new features or modifications without significant changes to the existing codebase.

## 5. HTML Template Module

### Existing Super Tic Tac Toe Framework
- The HTML module consists of a folder containing HTML templates for different pages of the web application, including login, welcome, index (game board), game win, and game draw templates.
- [Architectural Description and UML Diagram](../arch_documents/arch_html.md)

### Redesigned Framework
- The HTML module remains largely unchanged in the redesigned framework. It continues to contain HTML templates for various pages of the web application, with each template serving a specific purpose such as user authentication, displaying game board, announcing game outcomes (win or draw), etc.
- [Architectural Description and UML Diagram](htmlTemplate_Architecture.md)

### Interface Changes a Game Designer Would Need to Make
- Ensure that HTML templates follow best practices for web development, including semantic markup, separation of concerns, and accessibility considerations.
- Design templates to be modular and reusable, allowing for easy customization and extension across different game implementations.
- Provide placeholders and dynamic content insertion points within templates to accommodate game-specific data and user interactions.
- Incorporate CSS and JavaScript as needed to enhance user experience and interactivity within the web application






