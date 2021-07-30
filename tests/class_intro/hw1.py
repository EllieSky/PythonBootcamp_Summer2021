import unittest


def vowel_counter(word) -> int:
    count = 0
    if type(word) is list:
        for x in word: count += vowel_counter(x)
    elif type(word) is dict:
        for x,y in word.items():
            count += vowel_counter(x)
            count += vowel_counter(y)
    elif type(word) is not str: return count
    elif not word.isascii():
        raise ValueError("Sorry, non english words are not supported at this time")

    vowel = set("aeiou")

    for letter in word:
        if letter.lower() in vowel:
            count = count + 1

    return count


class TestVowelCount(unittest.TestCase):
    # positive smoke test
    def test_small_word(self):
        input = "dog"
        self.assertEqual(1, vowel_counter(input))

    def test_sentence(self):
        sentence = "It's a great Tuesday evening!"

        expected_count = 10
        actual_count = vowel_counter(sentence)

        self.assertTrue(expected_count == actual_count,
                        f"The actual count of {actual_count} vowels in the input '{sentence}' "
                        f"did not match expected count {expected_count}.")

    # negative
    def test_int_input(self):
        input = 266
        expected = 0
        actual = vowel_counter(input)
        self.assertEqual(expected, actual)

    def test_russian_word(self):
        word = "корова"
        # self.assertEqual(3, vowel_counter(word))
        self.assertRaises(ValueError, lambda: vowel_counter(word))

    def test_no_vowel_input(self):
        word = 'hfHDGSfjs'
        self.assertEqual(0, vowel_counter(word))

    def test_empty_input(self):
        word = ""
        self.assertEqual(0, vowel_counter(word))

    # negative
    def test_object_input(self):
        obj = object()
        self.assertEqual(0, vowel_counter(obj))

