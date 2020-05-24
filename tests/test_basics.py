import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def test_if_app_exists(self):
        self.assertFalse(current_app is None)

    def test_if_app_if_configured_as_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
