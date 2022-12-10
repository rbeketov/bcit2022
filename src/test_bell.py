import unittest

from collections.abc import Generator
from bell import bell

class TestUnique(unittest.TestCase):

    def setUp(self):
      self.bell_gen = bell()

    def test_bell_negativ(self):
        self.assertEqual([next(self.bell_gen) for _ in range(-1)], [])

    def test_bell_void(self):
        self.assertEqual([next(self.bell_gen) for _ in range(0)], [])

    def test_bell_result(self):
        self.assertEqual([next(self.bell_gen) for _ in range(5)], [1,1,2,5,15])
    
    def test_bell_lazy(self):
        self.assertIsInstance(self.bell_gen, Generator)

if __name__ == "__main__":
    unittest.main()