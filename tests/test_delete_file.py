import unittest
from unittest.mock import patch
from scripts.delete_file import delete_file

class TestDeleteFile(unittest.TestCase):
    @patch('scripts.delete_file.github_api_request')
    def test_delete_file(self, mock_github_request):
        # Mock responses for GET and DELETE calls
        mock_github_request.side_effect = [
            {"sha": "abc12345def67890"},  # Mock GET response for SHA
            {"commit": {"message": "Delete settings.json"}}  # Mock DELETE response
        ]

        response = delete_file(
            path="src/config/app/settings.json",
            message="Delete settings.json"
        )

        self.assertIn("commit", response)
        self.assertEqual(response["commit"]["message"], "Delete settings.json")

if __name__ == "__main__":
    unittest.main()
