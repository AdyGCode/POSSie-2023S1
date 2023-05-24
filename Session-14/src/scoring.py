
class Scoring:
    def display_scores(scores):
        pass


    def get_letter_scores(word, guess):
        '''
        Accepts two strings, and compares them to provide a score for the word.

        Design and code by Adrian Gould, May 2023

        The scores are based on the letters of the guess being compared to the
        letters of the secret word.

        A letter may not be scored twice.

        letter 1 is correct and in correct spot, score = 2
        letter 1 is correct but in wrong spot, score = 1
        letter 1 is incorrect, score = 0

        Two pass algorithm
        - compare for letters the same and in correct spot ONLY
        - compare for correct letters in the wrong spot

        Presume:
        - words are the same length
        - words are both given in same case (eg lower case).

        :param word:
        :param guess:
        :return:
        '''

        # create a list with 5 zeros (all incorrect)
        result = [0] * len(word)  # [0, 0, 0, 0, 0]

        # create lists from word and the guess
        word_list = list(word)  # hello --> ['h', 'e', 'l', 'l', 'o']
        guess_list = list(guess)
        # store the word length
        word_length = len(word)  # hello --> 5

        if word == guess:
            return [2, 2, 2, 2, 2]

        # first pass - check for same letters
        for pos in range(word_length):  # 0, 1, 2, 3, 4, ...
            if word_list[pos] == guess_list[pos]:
                # set result at pos to 2 (same letter same position)
                result[pos] = 2
                # remove letter at pos from both guess list and word list
                word_list[pos] = " "
                guess_list[pos] = " "

        for word_position in range(word_length):
            # is the letter in the word not blank (a space)?
            if word_list[word_position] != " ":
                for guess_position in range(word_length):
                    if guess_list[guess_position] == word_list[word_position]:
                        result[guess_position] = 1
                        word_list[word_position] = " "
                        guess_list[guess_position] = " "
                        break

        return result



