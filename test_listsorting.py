import unittest

from list_sorting import list_sort

class test_sort(unittest.TestCase):
    

    def test_sort_list(self):
        self.assertDictEqual(list_sort([2,0,6,5,1,7,'z','a']),{'evens': [0, 2, 6], 'odds': [1, 5, 7], 'chars': ['a', 'z']})
        self.assertEqual(len(list_sort([2,0,6,5,1,7,'z','a'])),3)
    def test_interger_or_character_in_list(self):
        self.assertEqual(list_sort([2,3,4,{3:9,4:16}]),'invalid input type, the list should have either characters or intergers')

if __name__ == '__main__':
    unittest.main()
    