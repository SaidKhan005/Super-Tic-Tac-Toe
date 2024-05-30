start_page_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple HTML Page</title>
        </head>
        <body>
            <h1>Tic Tac Toa</h1>
            <p>Start</p>
        </body>
        </html>"""
create_player_template = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>User Info</title>
        </head>
        <body>
            <form action="/submit" method="post">
                <h1>User Info Page</h1>
                <p>Users collected: {{len(users)}}</p>

                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>

                <label for="age">Age:</label>
                <input type="number" id="age" name="age" required>

                <input type="submit" value="Submit">
            </form>
        </body>
    </html>"""
game_page_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super Tic Tac Toe</title>
    <style>
        /* Add CSS styling here */
        .super-tic-tac-toe {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 5px;
            width: 300px;
            height: 300px;
            margin: auto;
            border: 2px solid black;
            border-radius: 5px;
            overflow: hidden;
        }
        .sub-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 3px;
            border: 1px solid black;
            border-radius: 5px;
            overflow: hidden;
        }
        .cell {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            cursor: pointer;
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <div class="super-tic-tac-toe">
        <!-- Sub grids -->
        <div class="sub-grid">
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
        </div>
        <div class="sub-grid">
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
        </div>
        <div class="sub-grid">
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
            <div class="cell"></div>
        </div>
    </div>
</body>
</html>"""
winners_page_template = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tic Tac Toe - Winner</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                }
                h1 {
                    color: #333;
                }
                p {
                    font-size: 20px;
                    color: green;
                }

            </style>
        </head>
        <body>
            <h1>Tic Tac Toe</h1>
            <p>{{winner}} wins!</p>
        </body>
    </html>"""
draw_page_template = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tic Tac Toe - Winner</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                }

                h1 {
                    color: #333;
                }

                p {
                    font-size: 20px;
                    color: green;
                }

            </style>
        </head>
        <body>
            <h1>Tic Tac Toe</h1>
            <p> Game ended in a draw add /reset_game to url to play again </p>
            <p>Current turn: {{current_player}}</p>
        </body>
    </html>"""

class Templates():
   
    @classmethod
    def start_page(cls):
        """
        This function creates the start page of the website.
        It contains a link to the create player page.
        
        Returns:
        - string, containing the HTML code for the start page.
        """
        return start_page_template
    
    @classmethod
    def create_player_page(cls):
        """
        This function creates a new player page with a form to enter the player's name and a submit button.
        
        Returns:
        - String, containing the HTML code for the player creation page.
        """
        return create_player_template
    
    @classmethod
    def gameboard_page(cls):
        """
        This function creates a new gameboard page with a grid of squares where players can place their tokens.
        
        Returns:
        - String, containing the HTML code for the gameboard page.
        """
        return game_page_template
    
    @classmethod
    def winner_page(cls, winner):
        """
        This function creates a new winner page with a message indicating the winner of the game.
        
        Args:
        - winner: String, the name of the winner
        
        Returns:
        - String, containing the HTML code for the winner page.
        """
        return winners_page_template.replace('{{winner}}', winner)
    
    @classmethod
    def draw_page(cls, current_player):
        """
        This function creates a new draw page with a message indicating that the game ended in a draw.

        Args:
        - current_player: String, the name of the current player
        
        Returns:
        - String, containing the HTML code for the draw page.
        """
        return draw_page_template.replace('{{current_player}}', current_player)
