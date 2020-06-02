import sys
sys.path.append("../")
from suggest import edit_distance
import unittest

class Tests(unittest.TestCase):

    def edit_distance_test(self):
        self.assertEqual(edit_distance("hello", "hel"), 2)
    


if __name__ == '__main__':
    unittest.main()



