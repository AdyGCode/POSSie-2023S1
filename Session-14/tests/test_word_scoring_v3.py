# Unit Testing References
# - https://www.dataquest.io/blog/unit-tests-python/
# - https://www.testim.io/blog/unit-testing-python-tutorial/


# Importing from Siblings
# - https://www.geeksforgeeks.org/python-import-from-sibling-directory/
# - https://realpython.com/absolute-vs-relative-python-imports/
# - https://www.aaronjgrossman.com/2019/08/04/importing-sibling-packages-in-python/

import unittest
from ..src.scoring import Scoring

# Absolute: c:\Users\Documents\source\repos\blah\packagename
# Relative: ./packagename

# from word_scoring_class import Scoring


class TestWordScoring(unittest.TestCase):

    def setUp(self) -> None:
        self.the_ajudicator = Scoring()
        self.the_ajudicator.test_number = 2


    def test_different_words(self):
        # "hello", "spams", [0, 0, 0, 0, 0]
        actual_result = self.the_ajudicator.get_letter_scores("hello", "spams")
        #  Expected result, actual result, custom message
        self.assertEqual([0, 0, 0, 0, 0], actual_result, 'Different words Fails')

    def test_words_identical(self):
        secret_word = "hello"
        guessed_word = "hello"
        expected_result = [2, 2, 2, 2, 2]
        actual_result = self.the_ajudicator.get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result)

    def test_sober_and_robes(self):
        secret_word = "sober"
        guessed_word = "robes"
        expected_result = [1, 2, 2, 2, 1]
        actual_result = self.the_ajudicator.get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result)

    def test_bores_and_robes(self):
        secret_word = "bores"
        guessed_word = "robes"
        expected_result = [1, 2, 1, 2, 2]
        actual_result = self.the_ajudicator.get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result)

    def test_bores_and_sober(self):
        secret_word = "bores"
        guessed_word = "sober"
        expected_result = [1, 2, 1, 2, 1]
        actual_result = self.the_ajudicator.get_letter_scores(secret_word, guessed_word)
        self.assertEqual(expected_result, actual_result, "test_bores_and_sober")


if __name__ == '__main__':
    unittest.main()
