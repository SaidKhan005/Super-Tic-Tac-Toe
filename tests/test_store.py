from unittest import TestCase
import DBOperations


class TestDBOps(TestCase):
    def setUp(self):
        self.player_test_1 = "player_1"
        self.player_test_2 = "player_2"
        self.game_matrix_test = [[0, 0, 0], [0, 0, 0]]

    def test_add_player(self):
        temp_username = "player_1"
        DBOperations.add_player(self.player_test_1)
        with self.assertRaises(IOError):
            DBOperations.add_player(temp_username)
        DBOperations.delete_player(self.player_test_1)

    def test_add_game(self):
        player_saved = self.player_test_1
        player_not_saved = self.player_test_2
        DBOperations.add_player(self.player_test_1)
        with self.assertRaises(IOError):
            DBOperations.add_game(self.game_matrix_test, player_saved, player_not_saved)
        DBOperations.delete_player(player_saved)

    def test_delete_player(self):
        temp_username = "player_not_saved"
        with self.assertRaises(IOError):
            DBOperations.delete_player(temp_username)
