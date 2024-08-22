import unittest
from soal import add, sub, multiplication, division, count_capital_letters,reverse_sentence, check_palindrome

class TestSoal(unittest.TestCase):
    def test_add(self):
        res = add(1,2)
        self.assertEqual(res,3)
        res = add(1,1.1)
        self.assertEqual(res,2.1)
        res = add(1,-2)
        self.assertEqual(res,-1)

    def test_sub(self):
        res = sub(1,2)
        self.assertEqual(res,-1)
        res = sub(2,1)
        self.assertEqual(res,1)
        res = sub(3,1.1)
        self.assertEqual(res,1.9)

    def test_multiplication(self):
        res = multiplication(1,2)
        self.assertEqual(res,2)
        res = multiplication(2,1)
        self.assertEqual(res,2)
        res = multiplication(3,1.1)
        self.assertEqual(res,3.3)
        res = multiplication(1.1,1.1)
        self.assertEqual(res,1.21)

    def test_division(self):
        res = division(1,2)
        self.assertEqual(res,0.5)
        res = division(2,2)
        self.assertEqual(res,1)
        res = division(2,3)
        self.assertEqual(res,0.67)
        with self.assertRaises(ValueError) as err:
            division(2,0)
        self.assertEqual(str(err.exception),"Error division number")

    def test_count_capital_letters(self):
        res = count_capital_letters("ABCabc")
        self.assertEqual(res,3)
        with self.assertRaises(ValueError) as err:
            count_capital_letters("asd_qwe_ASD_      zxcASDASDQWqweazAAA")
        self.assertEqual(str(err.exception),"Wrong input")
        res = count_capital_letters("asd@!#@#$%$#$%qweQWEQWE")
        self.assertEqual(res,6)

    def test_reverese_sentence(self):
        res = reverse_sentence("test123")
        self.assertEqual(res,"321tset")
        res = reverse_sentence("test 123")
        self.assertEqual(res,"321tset")
        res = reverse_sentence("t   wqeqw    asdest 123")
        self.assertEqual(res,"321tsedsawqeqwt")
    
    def test_check_palindrome(self):
        res=check_palindrome("abcdef")
        self.assertFalse(res)
        res=check_palindrome("asd123321qwe")
        self.assertTrue(res)
        with self.assertRaises(ValueError) as err:
            check_palindrome("12")
        self.assertEqual(str(err.exception),"Wrong Input")