import unittest
import unittest.mock

import sys
sys.path.append('../')
from nums import evens, check_evens_len 

class TestMock(unittest.TestCase):

    @unittest.mock.patch("nums.evens")
    def test_check_mock(self, evens_mock):
        
        evens_mock.return_value = []
        self.assertEqual(check_evens_len([2, 4, 6]), [])

        self.assertTrue(evens_mock.called)


        
