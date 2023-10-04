import unittest
import json
from unittest.mock import patch, Mock
from models import get_users_data


class TestGet20Users(unittest.TestCase):

    @patch('requests.get')
    def test_successful_response(self, mock_get):
        # Mocking a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_data = {
            "total": 217,
            "data": [{"nickname": "Alice", "isOnline": True, "lastSeenDate": None},
                     {"nickname": "Bob", "isOnline": False, "lastSeenDate": "2023-09-25T10:30:00+00:00"},
                     {"nickname": "Snack", "isOnline": False, "lastSeenDate": "2023-09-24T10:30:00+00:00"},
                     {"nickname": "Nick", "isOnline": False, "lastSeenDate": "2023-09-26T12:00:00+00:00"}]
        }
        mock_response.json.return_value = mock_data
        mock_response.text = json.dumps(mock_data)  # mock the .text attribute
        mock_get.return_value = mock_response

        # Calling the function
        result = get_users_data({'offset': 0})

        # Asserting the result
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0]['nickname'], "Alice")
        self.assertEqual(result[1]['nickname'], "Bob")
        self.assertEqual(result[2]['nickname'], "Snack")
        self.assertEqual(result[3]['nickname'], "Nick")

    @patch('requests.get')
    def test_failed_response(self, mock_get):
        # Mocking a failed response
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        # Calling the function
        result = get_users_data({'offset': 0})

        # Asserting the result
        self.assertEqual(result, [])
