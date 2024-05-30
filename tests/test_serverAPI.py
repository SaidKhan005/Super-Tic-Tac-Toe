import unittest
from bottle import Bottle, template, request, FormsDict
from server import app, create_user, delete_player_route, load_game_route

class TestServerModule(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = self.app.test_client()

    def test_user_info_route(self):
        response = self.test_client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user_info', response.data)

    def test_submit_user_info_route(self):
        with self.app.test_request_context('/submit', method='POST', environ_base={'REMOTE_ADDR': '127.0.0.1'},
                                           post_args=FormsDict([('username', 'test_user'), ('age', '25')])):
            response = self.app.get('/submit')
            self.assertEqual(response.status_code, 200)  # As we're redirecting to '/' in case of invalid input


    def test_make_move_route(self):
        with self.app.test_request_context('/make_move/1', method='POST'):
            request.forms['position'] = 1
            response = self.app.get('/make_move/1')
            self.assertEqual(response.status_code, 200)


    def test_reset_game_route(self):
        response = self.test_client.get('/reset_game')
        self.assertEqual(response.status_code, 302)  # Redirects to home page

    def test_create_user_function(self):
        user_data = {'username': 'test_user', 'age': 25, 'symbol': 'X'}
        create_user(user_data)


    def test_delete_player_route(self):
        response = self.test_client.get('/delete_player/test_user')
        self.assertEqual(response.status_code, 200)


    def test_load_game_route(self):
        response = self.test_client.get('/load_game/123')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()