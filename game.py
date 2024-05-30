"""
Tic Tac Toe Game Implementation.

This class represents a Tic Tac Toe game. It allows players to make moves on a 3x3 grid,
checks for winners, and manages the game state.

Attributes:
    games (list): List of ongoing Tic Tac Toe games.

Methods:
    __init__: Initialize the Tic Tac Toe game with two users.
    make_move: Make a move on the game board.
    toggle_player: Toggle between players.
    check_winner: Check if there is a winner in the current game state.
    is_board_full: Check if the game board is full.
    get_current_player: Get the current player.
    get_current_player_name: Get the name of the current player.
    get_game_id: Get the game ID.
    delete_player: Delete a player from the game.
    store_game_info: Store game information in the database.
    load_game: Load a game from the database.
    update_game: Update the game information in the database.
    reset_game: Reset the game state.
"""

from arch_user import ArchUser
import DBOperations
import random


class TicTacToe:

    games = []

    def __init__(self, users):
        """
        Initialize the Tic Tac Toe game with two users.

        Args:
            users (list): A list containing two ArchUser instances representing the players.
        """
        self.game_id = random.randint(1, 99) + 100
        self.board = [[" " for _ in range(9)] for _ in range(9)]  # 9x9 board
        self.sub_boards = [[[[' ' for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]  # 3x3 boards
        self.sub_board_winners = [[' ' for _ in range(3)] for _ in range(3)]
        self.user_1 = users[0]
        self.user_2 = users[1]
        self.current_player = self.user_1
        self.num_of_moves = 0

    def make_move(self, row, col):
        """
        Make a move on the game board.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            bool: True if the move is valid and made successfully, False otherwise.
        """

        sub_row = row // 3  # Determine the sub-board row index
        sub_col = col // 3  # Determine the sub-board column index

        sub_board_row = row % 3  # Determine the row index within the sub-board
        sub_board_col = col % 3  # Determine the column index within the sub-board

        # Check if the sub-board already has a winner
        if self.sub_board_winners[sub_row][sub_col] != ' ':
            return False

        if self.board[row][col] == ' ' and self.sub_boards[sub_row][sub_col][sub_board_row][sub_board_col] == ' ':
            self.board[row][col] = self.current_player.symbol
            self.sub_boards[sub_row][sub_col][sub_board_row][sub_board_col] = self.current_player.symbol

            # Check for winner in the current sub-board
            sub_board_winner = self.check_sub_board_winner(sub_row, sub_col)
            if sub_board_winner is not None:
                self.sub_board_winners[sub_row][sub_col] = sub_board_winner

            self.num_of_moves += 1

            if self.check_winner() is None:
                self.toggle_player()

            return True

        return False

    def check_sub_board_winner(self, sub_row, sub_col):
        """
        Check for a winner in a specific sub-board.

        Args:
            sub_row (int): The row index of the sub-board.
            sub_col (int): The column index of the sub-board.

        Returns:
            str or None: The winning player's symbol ('X' or 'O') or None if no winner.
        """
        sub_board = self.sub_boards[sub_row][sub_col]
        sub_board = self.sub_boards[sub_row][sub_col]

        # Check rows, columns, and diagonals for a winner in the sub-board
        for i in range(3):
            if sub_board[i][0] == sub_board[i][1] == sub_board[i][2] != ' ':
                return sub_board[i][0]
            if sub_board[0][i] == sub_board[1][i] == sub_board[2][i] != ' ':
                return sub_board[0][i]
        if sub_board[0][0] == sub_board[1][1] == sub_board[2][2] != ' ':
            return sub_board[0][0]
        if sub_board[0][2] == sub_board[1][1] == sub_board[2][0] != ' ':
            return sub_board[0][2]

        return None

    def check_winner(self):
        """
        Check if there is a winner in the current game state.

        Returns:
            str or None: The username of the winning player or 'Draw' if the game is a draw, None otherwise.
        """
        
        # Check for winner in the entire 9x9 board
        for i in range(3):
            for j in range(3):
                if self.sub_board_winners[i][0] == self.sub_board_winners[i][1] == self.sub_board_winners[i][2] != ' ':
                    return self.current_player.username
                if self.sub_board_winners[0][j] == self.sub_board_winners[1][j] == self.sub_board_winners[2][j] != ' ':
                    return self.current_player.username
            if self.sub_board_winners[0][0] == self.sub_board_winners[1][1] == self.sub_board_winners[2][2] != ' ':
                return self.current_player.username
            if self.sub_board_winners[0][2] == self.sub_board_winners[1][1] == self.sub_board_winners[2][0] != ' ':
                return self.current_player.username

        # Check for a draw in the entire board
        if all(cell != ' ' for row in self.board for cell in row):
            return 'Draw'

        return None

    def draw(self):
        """
        Check if the game board is in a draw state.

        Returns:
            bool: True if all sub-boards are filled and no winner exists, False otherwise.
        """
        for row in self.sub_board_winners:
            if all(cell != ' ' for cell in row):
                return False  # At least one sub-board has a winner

        # Check if the entire board is filled
        if all(cell != ' ' for sub_board in self.sub_boards for row in sub_board for cell in row):
            return True  # All sub-boards are filled

        # If neither condition is met, return False
        return False

    def toggle_player(self):
        """
        Toggle between players.
        """
        # Check if any sub-board has a winner or is filled
        for row in self.sub_board_winners:
            if all(cell != ' ' for cell in row):
                return False  # At least one sub-board has a winner

        # Check if the entire board is filled
        if all(cell != ' ' for sub_board in self.sub_boards for row in sub_board for cell in row):
            return True  # All sub-boards are filled

        # If neither condition is met, return False
        return False

    def toggle_player(self):
        """
        Toggle between players.
        """
        self.current_player = self.user_2 if self.current_player == self.user_1 else self.user_1



    def get_current_player(self):
        """
        Get the current player.

        Returns:
            ArchUser: The current player.
        """
        return self.current_player

    def get_current_player_name(self):
        """
        Get the name of the current player.

        Returns:
            str: The name of the current player.
        """
        return self.current_player.username

    def get_game_id(self):
        """
        Get the game ID.

        Returns:
            int: The game ID.
        """
        return self.game_id

    def delete_player(self, username):
        """
        Delete a player from the game.

        Args:
            username (str): The username of the player to delete.
        """
        if username == self.user_1.username:
            self.user_1.delete_user(username)
        else:
            self.user_2.delete_user(username)

    def store_game_info(self):
        """
        Store game information in the database.
        """
        game_info = {
            'game_id': self.game_id,
            'matrix': self.board,
            'player1': self.user_1.username,
            'player2': self.user_2.username,
            'winner': self.current_player.username,
            'num_of_moves': self.num_of_moves
        }
        DBOperations.store_game_info(game_info)

    def load_game(self, game_id):
        """
        Load a game from the database.

        Args:
            game_id (int): The ID of the game to load.

        Returns:
            dict: Information about the loaded game.
        """
        self.update_game()
        return DBOperations.load_game(game_id)

    def update_game(self):
        """
        Update the game information in the database.
        """
        game_id = self.game_id
        matrix = self.board
        num_of_moves = self.num_of_moves
        if self.check_winner() is not None and self.check_winner() != 'Draw':
            winner = self.current_player.username
        else:
            winner = 'No winner, game ended in draw'
        DBOperations.update_game_info(game_id, matrix, num_of_moves, winner)

    def reset_game(self):
        """
        Reset the game state.
        """
        self.board = [[" " for _ in range(9)] for _ in range(9)]  # 9x9 board
        self.sub_boards = [[[[' ' for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in
                           range(3)]  # 3x3 boards
        self.sub_board_winners = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = self.user_1
        self.num_of_moves = 0