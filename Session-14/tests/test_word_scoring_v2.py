# Unit Testing References
# - https://realpython.com/absolute-vs-relative-python-imports/
# -

# Importing from Siblings
# - https://www.geeksforgeeks.org/python-import-from-sibling-directory/
# -

import unittest
from ..src.word_scoring import get_letter_scores
from ..src.word_scoring import display_scores

# Absolute: c:\Users\Documents\source\repos\blah\packagename
# Relative: ./packagename

# from word_scoring_class import Scoring


class TestWordScoring(unittest.TestCase):

    def setUp(self) -> None:
        self.secret = "EMPTY"
        self.guess = "WORDS"
        self.expected = [-1, -1, -1, -1, -1]
        self.actual = [-1, -1, -1, -1, -1]

    def test_does_nothing(self):
        self.assertTrue(True, "It's NOT True!")

    def test_reversed(self):
        self.secret = "hello"
        self.guess = self.guess.upper()
        self.expected = [1, 1, 2, 1, 1]
        self.actual = get_letter_scores(self.secret, self.guess)
        self.assertEqual(self.expected, self.actual, "Reversed Test Fails")

    def test_different_words(self):
        # "hello", "spams", [0, 0, 0, 0, 0]
        actual_result = get_letter_scores("hello", "spams")
        #  Expected result, actual result, custom message
        self.assertEqual([0, 0, 0, 0, 0], actual_result, 'Different words Fails')

    def test_words_identical(self):
        secret_word = "hello"
        guessed_word = "hello"
        expected_result = [2, 2, 2, 2, 2]
        actual_result = get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result)

    def test_sober_and_robes(self):
        secret_word = "sober"
        guessed_word = "robes"
        expected_result = [1, 2, 2, 2, 1]
        actual_result = get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result)

    def test_bores_and_robes(self):
        secret_word = "bores"
        guessed_word = "robes"
        expected_result = [1, 2, 1, 2, 2]
        actual_result = get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result)

    def test_bores_and_sober(self):
        secret_word = "bores"
        guessed_word = "sober"
        expected_result = [1, 2, 1, 2, 1]
        actual_result = get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result, "test_bores_and_sober")


if __name__ == '__main__':
    unittest.main()
