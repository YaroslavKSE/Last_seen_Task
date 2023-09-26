from io import StringIO
import sys
import unittest
from models import print_20_users


class TestPrint20Users(unittest.TestCase):

    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output  # Redirecting stdout

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__  # Restoring stdout

    def test_print_online_user(self):
        user_data = [{"nickname": "Alice", "isOnline": True, "lastSeenDate": None}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nAlice is online\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_yesterday_user(self):
        user_data = [{"nickname": "Bob", "isOnline": False, "lastSeenDate": "2023-09-25T10:30:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nBob seen yesterday\n"
        self.assertEqual(output, expected_output)

    # Add similar tests for other last seen times (just now, a few minutes ago, etc.)
