import DBOperations
import logging


class ArchUser:
    """
    Represents a user in the system and provides functionalities for user management.

    Attributes:
        username (str): The username of the user.
        age (int): The age of the user.
        symbol (str): The symbol associated with the user.
    """

    def __init__(self, user_dict):
        """
        Initializes an ArchUser object with the provided user information.

        Args:
            user_dict (dict): A dictionary containing user information with keys 'username', 'age'.
        """
        self.username = user_dict.get('username')
        self.age = user_dict.get('age')
        self.symbol = ''
        self.add_user_to_db()

    @classmethod
    def assign_symbol(cls, user1, user2):
        """
           Assigns a symbol to each user

           Args:
           user1 (user object): The user object of the first player
           user2 (user object): The user object of the second player
        """
        user1.symbol = 'X'
        user2.symbol = 'O'

    @classmethod
    def get_users(cls):
        """
        Returns a list of user objects
        """
        return DBOperations.fetch_users()

    def add_user_to_db(self):
        """
        Adds the created user object to the database.

        Raises:
            AttributeError: If an attribute error occurs while adding the user to the database.
        """
        try:
            DBOperations.add_user(self.username, self.age)
        except AttributeError as ae:
            logging.error(f"Error adding user to the database: {ae}")

    @classmethod
    def check_players(cls, username1, username2):
        """
        Checks if the players with the usernames provided exist in the database

        Args:
        username1 (str): The username of the first player
        username2 (str): The username of the second player

        Returns:
            True if the players exist in the database, False otherwise

        """
        return DBOperations.check_usernames_exist(username1, username2)

    def delete_user(self, username):
        """
        Deletes a user from the list of players.

        Args:
            username (str): The username of the user to be deleted.

        Raises:
            AttributeError: If an attribute error occurs while deleting the user from the database.
        """
        try:
            DBOperations.delete_player(username)
        except AttributeError as ae:
            logging.error(f"Error deleting user from the database: {ae}")
