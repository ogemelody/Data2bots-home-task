from main import read_json_content
import unittest
from unittest.mock import mock_open, patch


class TestMain(unittest.TestCase):
    def test_read_json_content(self):
        json_content = read_json_content('test/sample.json')
        self.assertDictEqual(json_content, {'key': 'This is a test'})

if __name__ == '__main__':
    unittest.main()
