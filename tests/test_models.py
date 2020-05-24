import unittest
from app.models import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.u = User(username='u', password='cat')
        self.u1 = User(username='u1')
        self.u1.password = 'dog'
        self.u2 = User(username='u2', password='cat', is_admin=True)

    def test_password_is_hashed(self):
        self.assertTrue(self.u.password_hash is not None)

    def test_cant_access_not_hashed_password(self):
        with self.assertRaises(AttributeError):
            self.u.password

    def test_hashed_password_and_password_are_match(self):
        self.assertTrue(self.u.verify_password('cat'))
        self.assertFalse(self.u.verify_password('dog'))

    def test_password_hashes_are_not_unique(self):
        self.assertNotEqual(self.u.password_hash, self.u2.password_hash)

    def test_is_admin_default_false(self):
        self.assertFalse(self.u.is_admin)
        self.assertTrue(self.u2.is_admin)
