import unittest
from html_game import websiteRequestHandler, start_page_template, create_player_template, game_page_template, winners_page_template, draw_page_template

class TestWebsiteRequestHandler(unittest.TestCase):
    def test_start_page(self):
        # Arrange
        expected_response = """
        to be filled later
            """
        
        # Act
        response = websiteRequestHandler.start_page()
        
        # Assert
        self.assertEqual(response.strip(), expected_response.strip())
    
    def test_bad_start_page(self):
        # Arrange
        expected_response = """
        to be filled later
            """
        
        # Act
        response = websiteRequestHandler.start_page()
        
        # Assert
        self.assertEqual(response.strip(), expected_response.strip())

    def test_create_player_page(self):
        # Arrange
        expected_response = """
        to be filled later
            """
        
        # Act
        response = websiteRequestHandler.create_player_page()
        
        # Assert
        self.assertEqual(response.strip(), expected_response.strip())

    def test_bad_create_player_page(self):
        # Arrange
        expected_response = """
        to be filled later
            """

    def test_gameboard_page(self):
        # Arrange
        expected_response = game_page_template
        
        # Act
        response = websiteRequestHandler.gameboard_page()
        
        # Assert
        self.assertEqual(response.strip(), expected_response.strip())

    def test_bad_gameboard_page(self):
        # Arrange & Act
        with self.assertRaises(TypeError):
            websiteRequestHandler.gameboard_page()  # Method should be called with 'cls' parameter

    def test_winner_page(self):
        # Arrange
        winner = "Player X"
        expected_response = winners_page_template.replace('{{winner}}', winner)
        
        # Act
        response = websiteRequestHandler.winner_page(winner)
        
        # Assert
        self.assertEqual(response.strip(), expected_response.strip())

    def test_bad_winner_page(self):
        # Arrange & Act
        with self.assertRaises(TypeError):
            websiteRequestHandler.winner_page()  # Method should be called with 'winner' parameter
    
    def test_draw_page(self):
        # Arrange
        current_player = "Player O"
        expected_response = draw_page_template.replace('{{current_player}}', current_player)
        
        # Act
        response = websiteRequestHandler.draw_page(current_player)
        
        # Assert
        self.assertEqual(response.strip(), expected_response.strip())

        
        # Act
        response = websiteRequestHandler.create_player_page()
        
        # Assert
        self.assertEqual(response.strip(), expected_response.strip())
        
    def test_bad_draw_page(self):
        # Arrange & Act
        with self.assertRaises(TypeError):
            websiteRequestHandler.draw_page()  # Method should be called with 'current_player' parameter

if __name__ == '__main__':
    unittest.main()
    