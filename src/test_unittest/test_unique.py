import unittest

import sys
sys.path.append('../')
from unique import Unique

class TestUnique(unittest.TestCase):

    def test_unique_any(self):
        self.assertEqual(list(Unique(["F", "f", "f", "F"])), ["F", "f"])

    def test_unique_ignore_case(self):
        self.assertEqual(list(Unique(["F", "f", "f", "F"], bool_ignore_case = True)), ["f"])
    
    def test_empty(self):
        self.assertEqual(list(Unique([])), [])