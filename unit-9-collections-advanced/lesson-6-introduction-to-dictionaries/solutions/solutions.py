def banana_dict(num):
    return {'banana'*number: number for number in range(1, num+1)}

import unittest


class BananaDictTest(unittest.TestCase):

    def test_dictionary_one(self):
        self.assertEqual(banana_dict(1), {'banana': 1})
    
    def test_dictionary_zero(self):
        self.assertEqual(banana_dict(0), {})

    def test_dictionary_three(self):
        self.assertEqual(banana_dict(3), {'banana': 1, 'bananabanana': 2, 'bananabananabanana': 3})

unittest.main()