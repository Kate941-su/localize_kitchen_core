import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.sdk.sdk import sdk_list
from src.locale_code.code_map import code_map

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(code_map['ja'], 'ja')


if __name__ == '__main__':
    unittest.main()