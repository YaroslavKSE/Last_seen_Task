import unittest
from unittest.mock import patch, Mock
from models import get_20_users


class TestGet20Users(unittest.TestCase):

    @patch('requests.get')
    def test_successful_response(self, mock_get):
        # Mocking a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_data = {
            "total": 217,
            "data": [{"nickname": "Alice", "isOnline": True, "lastSeenDate": None},
                     {"nickname": "Bob", "isOnline": False, "lastSeenDate": "2023-09-25T10:30:00+00:00"}]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Calling the function
        result = get_20_users({'offset': 0})

        # Asserting the result
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['nickname'], "Alice")

    @patch('requests.get')
    def test_failed_response(self, mock_get):
        # Mocking a failed response
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        # Calling the function
        result = get_20_users({'offset': 0})

        # Asserting the result
        self.assertEqual(result, [])


