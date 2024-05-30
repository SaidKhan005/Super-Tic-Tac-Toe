from bottle import Bottle, run, template, request, redirect
from game import TicTacToe
from arch_user import ArchUser
import random

host = "localhost"
server_port = 8080
app = Bottle()
global game
global player
players = []


@app.route('/')
def welcome():
    """
    Render the user information template.

    This function renders the template for collecting user information.

    Returns:
    str: Rendered HTML template for collecting user information.
    """
    return template('templates/welcome')


@app.route('/login')
def login_page():
    """
    Render the login page.

    This function renders the login page of the application.

    Returns:
    str: Rendered HTML template for the login page.
    """
    return template('templates/login')


@app.route('/sign_up')
def sign_up():
    """
    Render the sign-up page.

    This function renders the sign-up page of the application.

    Returns:
    str: Rendered HTML template for the sign-up page.
    """
    return template('templates/user_info')


@app.route('/submit_signup_form', method='POST')
def submit_user_info():
    """
    Submit user information and create a new game if enough players.

    This function handles the submission of user information and creates a new game
    if there are enough players.

    Returns:
    str: HTML template for the next page or an error message if failed to create a game.
    """
    username = request.forms.get('username')
    age = request.forms.get('age')
    if username and age:
        user_data = {'username': username, 'age': age}
        create_user(user_data)
        return login_page()
    else:
        return "Please enter both username and age."


@app.route('/start_game', method='POST')
def start_game():
    """
    Start a new game of Tic-Tac-Toe between two players.

    This function handles the process of starting a new game between two players. It receives the usernames of the two players through a POST request,
    checks if they are valid players, assigns symbols to them, initializes a new game of Tic-Tac-Toe, and stores the game information.

    Returns:
    str: HTML content for the next page if the game is successfully started, or an error message if there was an issue starting the game.
    """
    global game
    global players

    username1 = request.forms.get('username1')
    username2 = request.forms.get('username2')

    if ArchUser.check_players(username1, username2):
        player1 = get_user(username1)
        player2 = get_user(username2)

        ArchUser.assign_symbol(player1, player2)

        players.append(player1)
        players.append(player2)

        game = TicTacToe(players)
        # Create a game and get the game ID
        game_id = game.get_game_id()
        if game_id is not None:
            game.store_game_info()
            players = []
            return next_page()
        else:
            return "Error: Unable to create a game. Please try again."
    else:
        return login_page()


@app.route('/make_move/<row:int>/<col:int>', method='POST')
def make_move(row, col):
    """
    Make a move in the Tic Tac Toe game.

    This function handles making a move in the Tic Tac Toe game.

    Parameters:
    position (int): The position on the board where the move is to be made.

    Returns:
    str: HTML template for the next page or an error message if the move is invalid.
    """
    if game.make_move(row, col):
        winner = game.check_winner()
        if winner != 'Draw' and winner is not None:
            return winner_page(winner)
        elif winner == 'Draw':
            return game_draw_page()
        else:
            return next_page()
    else:
        return next_page()


@app.route('/reset_game')
def reset_game():
    """
    Reset the Tic Tac Toe game.

    This function resets the Tic Tac Toe game to start a new one.

    Returns:
    str: HTML template for the game board and current player.
    """
    if game:
        game.reset_game()
        return template('templates/index', board=game.board, current_player=game.get_current_player_name(),
                        game_id=game.get_game_id())
    else:
        return redirect('/')


def create_user(user_data):
    """
    Create a new user.

    This function creates a new user and adds it to the list of users.

    Parameters:
    user_data (dict): User information including username, age, and symbol.
    """
    global player

    player = ArchUser(user_data)


def get_user(username):
    """
    Retrieve a user by their username.

    This function searches for a user with the provided username in the list of all users.

    Args:
    username (str): The username of the user to retrieve.

    Returns:
    ArchUser or None: The user object if found, or None if no user with the specified username exists.
    """
    users = ArchUser.get_users()
    for user in users:
        if user.username == username:
            return user


@app.route('/delete_player/<username>')
def delete_player_route(username):
    """
    Delete a player.

    This function deletes a player from the game.

    Parameters:
    username (str): Username of the player to be deleted.

    Returns:
    str: Confirmation message of successful deletion or an error message.
    """
    try:
        game.delete_player(username)
        return f"Player {username} deleted successfully."
    except IOError as e:
        return str(e)


@app.route('/load_game/<game_id:int>')
def load_game_route(game_id):
    """
    Load a saved game.

    This function loads a saved game using the provided game ID.

    Parameters:
    game_id (int): ID of the game to be loaded.

    Returns:
    str: HTML template for the loaded game or an error message if the game is not found.
    """
    game_info = game.load_game(game_id)
    if game_info:
        return template('templates/load_game', game_info=game_info)
    else:
        return f"Game with ID {game_id} not found."


def winner_page(winner):
    """
    Render the winner page.

    This function renders the template for displaying the winner of the game.

    Parameters:
    winner (str): Username of the winner.

    Returns:
    str: Rendered HTML template for the winner page.
    """
    return template('templates/winner', winner=winner)


def next_page():
    """
    Render the next page.

    This function renders the template for the next page in the game.

    Returns:
    str: Rendered HTML template for the next page.
    """
    return template('templates/index', board=game.board, current_player=game.get_current_player_name(),
                    game_id=game.get_game_id())


def game_draw_page():
    """
    Render the game draw page.

    This function renders the template for displaying a draw in the game.

    Returns:
    str: Rendered HTML template for the draw page.
    """
    return template('templates/draw', current_player=game.get_current_player_name())


if __name__ == '__main__':
    run(app, host=host, port=server_port, debug=True)


