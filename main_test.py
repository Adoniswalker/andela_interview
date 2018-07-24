import unittest
from switch_reverser import switch_reverser as sr
from pig_latin import pig_latin_fun


class SwitchReverserTestCase(unittest.TestCase):
    
    def test_switch_list(self):
        self.assertEqual(sr([3,4,67,2,5]), [5,2,67,4,3])
        
    def test_string_int_list(self):
        self.assertEqual(sr(['dennis',4,67,2,5]), ['dennis',4,67,2,5])
        
    def test_string_list(self):
        self.assertEqual(sr(['dennis','walker']), ['DENNIS','WALKER'])
        
class PigLatinTestCase(unittest.TestCase):
    
    def test_start_consonant(self):
        self.assertEqual(pig_latin_fun('will'),'illway')
        
    def test_start_vowel(self):
        self.assertEqual(pig_latin_fun('andela'),'andelaway')
        
    def test_no_vowel(self):
        self.assertEqual(pig_latin_fun('spy'),'spy')

if __name__ == '__main__':
    unittest.main()
