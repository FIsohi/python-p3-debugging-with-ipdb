import unittest
from lib.ipdb_debugging import plus_two

class TestIpdbDebugging(unittest.TestCase):
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum'''
        self.assertEqual(plus_two(3), 5)

if __name__ == "__main__":
    unittest.main()
