import unittest
from basic_functions import concatenate_strings, capitalize_string, reverse_string, count_vowels


class TestIntegrationCases(unittest.TestCase):

    def test_concatenate_strings_pass(self):
        result = concatenate_strings("Hello", "World")
        self.assertEqual(result, "HelloWorld")  # pass

    def test_capitalize_string_pass(self):
        result = capitalize_string("hello")
        self.assertEqual(result, "Hello")  # pass

    def test_reverse_string_pass(self):
        result = reverse_string("hello")
        self.assertEqual(result, "olleh")  # pass

    def test_count_vowels_pass(self):
        result = count_vowels("Hello World")
        self.assertEqual(result, 3)  # pass

    def test_concatenate_strings_fail(self):
        result = concatenate_strings("Hello", "World")
        self.assertEqual(result, "Hello World")  # fail

    def test_capitalize_string_fail(self):
        result = capitalize_string("hello")
        self.assertEqual(result, "hello")  # fail

    def test_reverse_string_fail(self):
        result = reverse_string("hello")
        self.assertEqual(result, "hello")  # fail

    def test_count_vowels_fail(self):
        result = count_vowels("Hello World")
        self.assertEqual(result, 10)  # fail


if __name__ == '__main__':
    unittest.main()
