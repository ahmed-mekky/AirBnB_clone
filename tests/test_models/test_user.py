#!/usr/bin/python3
"""Unittest for User([..])
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittest for User"""

    def setUp(self):
        """test"""

        self.user = User()

    def test_user_email(self):
        """email test"""

        self.assertEqual(self.user.email, "")

    def test_user_password(self):
        """password test"""

        self.assertEqual(self.user.password, "")

    def test_user_first_name(self):
        """first_name test"""

        self.assertEqual(self.user.first_name, "")

    def test_user_last_name(self):
        """first_name test"""

        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
