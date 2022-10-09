"""
test_photo_album_app.py
"""

import unittest
import photo_album_app

class TestPhotoAlbumApp(unittest.TestCase):
    """Tests getting json response from album id url"""

    def test_get_json_response_with_large_id(self):
        """A large id should return an empty list because it does not exist."""
        actual = photo_album_app.get_json_response(9999999999)
        expected = []
        self.assertEqual(actual, expected)

    def test_get_json_response(self):
        """Uses an ID which should return a JSON respose.
        The result should have more than 0 results."""
        response = photo_album_app.get_json_response(1)
        self.assertTrue(len(response) > 0)
        