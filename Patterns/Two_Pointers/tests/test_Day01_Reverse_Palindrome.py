import unittest
from Patterns.Two_Pointers.Solution.Day01_reverse_palindrome_string import reverse_string, palindrome_ornot


class TestReversePalindromestring(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string(list("hello")), list("olleh"))  # add assertion here
        self.assertNotEqual(reverse_string(list("python")), list("python"))

    def test_Palindrome(self):
        self.assertEqual(palindrome_ornot("madam"), "a palindrome")
        self.assertNotEqual(palindrome_ornot("madman"), "a palindrome")


if __name__ == '__main__':
    unittest.main()
