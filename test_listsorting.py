import unittest

from list_sorting import list_sort

class test_sort(unittest.TestCase):
    

    def test_sort_list(self):
        self.assertDictEqual(list_sort([2,0,6,5,1,7,'z','a']),{'evens': [2, 0, 6], 'odds': [5, 1, 7], 'chars': ['z', 'a']})


if __name__ == '__main__':
    unittest.main()
    