from io import StringIO
import sys
import unittest
from datetime import datetime, timezone
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
        current_datetime = datetime.now(timezone.utc)
        user_data = [{"nickname": "Bob", "isOnline": False,
                      "lastSeenDate": f"2023-09-{current_datetime.day - 1}T10:30:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nBob seen yesterday\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_this_week(self):
        current_datetime = datetime.now(timezone.utc)
        user_data = [{"nickname": "Smack", "isOnline": False,
                      "lastSeenDate": f"2023-09-{current_datetime.day - 4}T10:30:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nSmack seen this week\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_a_couple_of_minutes_ago(self):
        current_datetime = datetime.now(timezone.utc)
        user_data = [{"nickname": "Nick", "isOnline": False,
                      "lastSeenDate": f"2023-09-{current_datetime.day}T{current_datetime.hour}"
                                      f":{current_datetime.minute - 1}:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nNick seen a couple of minutes ago\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_an_hour_ago(self):
        current_datetime = datetime.now(timezone.utc)
        user_data = [{"nickname": "Kim", "isOnline": False,
                      "lastSeenDate": f"2023-09-{current_datetime.day}T{current_datetime.hour - 1}:"
                                      f"{current_datetime.minute}:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nKim seen an hour ago\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_less_than_a_minute_ago(self):
        current_datetime = datetime.now(timezone.utc)
        user_data = [{"nickname": "John", "isOnline": False,
                      "lastSeenDate": f"2023-09-{current_datetime.day}T{current_datetime.hour}"
                                      f":{current_datetime.minute}:{current_datetime.second - 31}+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nJohn seen less than a minute ago\n"
        self.assertEqual(output, expected_output)

    def test_print_seen_user_just_now(self):
        current_datetime = datetime.now(timezone.utc)
        user_data = [{"nickname": "Mack", "isOnline": False,
                      "lastSeenDate": f"2023-09-{current_datetime.day}T{current_datetime.hour}"
                                      f":{current_datetime.minute}:{current_datetime.second - 2}+00:00"}]
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
        current_datetime = datetime.now(timezone.utc)
        user_data = [{"nickname": "Ben", "isOnline": False,
                      "lastSeenDate": f"2023-09-{current_datetime.day}T{current_datetime.hour - 5}:00:00+00:00"}]
        print_20_users(user_data)
        self.held_output.seek(0)
        output = self.held_output.read()
        expected_output = "----------\nBen seen today\n"
        self.assertEqual(output, expected_output)
