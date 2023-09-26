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

    def test_print_user_is_online(self):
        user_data = [{"nickname": "Alice", "isOnline": True, "lastSeenDate": None}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nAlice is online\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_yesterday(self):
        user_data = [{"nickname": "Bob", "isOnline": False, "lastSeenDate": "2023-09-25T10:30:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nBob seen yesterday\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_this_week(self):
        user_data = [{"nickname": "Smack", "isOnline": False, "lastSeenDate": "2023-09-24T10:30:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nSmack seen this week\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_a_couple_of_minutes_ago(self):
        user_data = [{"nickname": "Nick", "isOnline": False, "lastSeenDate": "2023-09-26T12:00:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nNick seen a couple of minutes ago\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_an_hour_ago(self):
        user_data = [{"nickname": "Kim", "isOnline": False, "lastSeenDate": "2023-09-26T11:00:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nKim seen an hour ago\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_less_than_a_minute_ago(self):
        user_data = [{"nickname": "John", "isOnline": False, "lastSeenDate": "2023-09-26T12:15:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nJohn seen less than a minute ago\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_just_now(self):
        user_data = [{"nickname": "Mack", "isOnline": False, "lastSeenDate": "2023-09-26T12:16:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nMack seen just now\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_long_time_ago(self):
        user_data = [{"nickname": "Ken", "isOnline": False, "lastSeenDate": "2023-09-10T12:16:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nKen seen long time ago\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_today(self):
        user_data = [{"nickname": "Ben", "isOnline": False, "lastSeenDate": "2023-09-26T01:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nBen seen today\n"
        self.assertEqual(output, expected_output)