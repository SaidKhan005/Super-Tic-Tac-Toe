from unittest import TestCase
from arch_user import ArchUser

class TestArchUser(TestCase):

    def setUp(self):
        self.user_dict = {'username': 'JohnDoe', 'age': 25}
        self.user_dict2 = {'username': 'Chris', 'age': 10}

    def test_create_user_valid_input(self):

        user_obj = ArchUser(self.user_dict)
        user_obj2 = ArchUser(self.user_dict2)

        self.assertEqual(user_obj.username, 'JohnDoe')
        self.assertEqual(user_obj.age, 25)

        self.assertEqual(user_obj2.username, 'Chris')
        self.assertEqual(user_obj2.age, 10)

        user_obj.delete_user('JohnDoe')
        user_obj2.delete_user('Chris')

    def test_delete_user_valid_input(self):
        # Delete the user using ArchUser method
        user_obj = ArchUser(self.user_dict)
        user_obj.delete_user(user_obj.username)

        # Attempt to create a new user with the same username
        new_user = ArchUser(self.user_dict)

        # Verify that the new user is created successfully
        self.assertEqual(new_user.username, 'JohnDoe')
        self.assertEqual(new_user.age, 25)

    def test_assign_symbols(self):
        user_obj = ArchUser(self.user_dict)
        user_obj2 = ArchUser(self.user_dict2)
        ArchUser.assign_symbol(user_obj, user_obj2)

        self.assertEqual(user_obj.symbol, 'X')
        self.assertEqual(user_obj2.symbol, 'O')

        user_obj.delete_user('JohnDoe')
        user_obj2.delete_user('Chris')
