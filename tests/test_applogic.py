import unittest
from game import TicTacToe
from arch_user import ArchUser


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Create two test users
        user1 = {'username': 'Player1', 'age': 30, 'symbol': 'X'}
        user2 = {'username': 'Player2', 'age': 25, 'symbol': 'O'}
        self.player1 = ArchUser(user1)
        self.player2 = ArchUser(user2)
        self.game = TicTacToe([user1, user2])

    def test_initialization(self):
        # Test game initialization
        self.assertEqual(self.game.num_of_moves, 0)
        self.assertEqual(self.game.current_player, self.player1)
        self.assertIsInstance(self.game.user_1, ArchUser)
        self.assertIsInstance(self.game.user_2, ArchUser)

    def test_make_move(self):
        # Test valid moves
        self.assertTrue(self.game.make_move(0, 0))
        self.assertTrue(self.game.make_move(1, 1))
        self.assertTrue(self.game.make_move(3, 3))

        # Test invalid moves
        self.assertFalse(self.game.make_move(0, 0))  # Already occupied
        self.assertFalse(self.game.make_move(0, 9))  # Out of board range

    def test_check_winner(self):
        # Test no winner initially
        self.assertIsNone(self.game.check_winner())

        # Simulate a winning scenario
        self.game.make_move(0, 0)  # Player 1 (X)
        self.game.make_move(1, 0)  # Player 2 (O)
        self.game.make_move(0, 1)  # Player 1 (X)
        self.game.make_move(1, 1)  # Player 2 (O)
        self.game.make_move(0, 2)  # Player 1 (X)
        self.assertEqual(self.game.check_winner(), 'Player1')  # Player 1 wins

    def test_toggle_player(self):
        # Test toggling between players
        self.assertEqual(self.game.current_player, self.player1)
        self.game.toggle_player()
        self.assertEqual(self.game.current_player, self.player2)
        self.game.toggle_player()
        self.assertEqual(self.game.current_player, self.player1)

    def tearDown(self):
        # Clean up after each test if needed
        pass


if __name__ == '__main__':
    unittest.main()
