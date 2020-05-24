import unittest
from app.models import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.u = User(username='u', password='cat')
        self.u1 = User(username='u1')
        self.u1.password = 'dog'
        self.u2 = User(username='u2', password='cat')

    def test_password_is_hashed(self):
        self.assertTrue(self.u.password_hash is not None)

    def test_cant_access_not_hashed_password(self):
        with self.assertRaises(AttributeError):
            self.u.password

    def test_hashed_password_and_password_are_match(self):
        self.assertTrue(self.u.verify_password('cat'))
        self.assertFalse(self.u.verify_password('dog'))

    def test_usernames_are_unique(self):
        with self.assertRaises(Exception):
            u3 = User(username='u')

    def test_password_hashes_are_not_unique(self):
        self.assertNotEqual(self.u.password_hash, self.u2.password_hash)
