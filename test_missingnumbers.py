import unittest
from missingnumber import missing_number_list

class test_missing(unittest.TestCase):
    

    def test_missingNumber(self):
        self.assertEqual(missing_number_list([ 1, 2, 3, 5, 6, 7,9]),[4,8])


if __name__ == '__main__':
    unittest.main()
