# HTML Component Interface Summary

The HTML component serves as the user interface layer of the application, responsible for rendering dynamic web pages and facilitating user interactions. It encapsulates various templates for different pages and provides methods to generate HTML content dynamically.

## Interface Methods

1. `start_page(cls)`: Generates the start page HTML code.
2. `create_player_page(cls)`: Generates the player creation page HTML code with a form.
3. `gameboard_page(cls)`: Generates the gameboard page HTML code with a grid of squares.
4. `winner_page(cls, winner)`: Generates the winner page HTML code with a message indicating the winner.
   - Args: `winner` (String) - The name of the winner.
5. `draw_page(cls, current_player)`: Generates the draw page HTML code with a message indicating a draw.
   - Args: `current_player` (String) - The name of the current player.

Each method returns a string containing the corresponding HTML code for the specific page.
