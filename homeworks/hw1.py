import unittest


def vowel_counter(word) -> int:
    count = 0
    if type(word) is list:
        for x in word : count += vowel_counter(x)
    elif type(word) is dict:
        for x, y in word.items():
            count += vowel_counter(x)
            count += vowel_counter(y)
    elif type(word) is not str:
        return count

    vowel = set("aeiou")

    for letter in word:
        if letter in vowel:
            count = count + 1

    return count


class Homework(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(8, vowel_counter(["apple", "banana", "cherry", "yellow"]))

    def test_positive_dict(self):
        self.assertEqual(8, vowel_counter({"brand": "Ford", "model": "Mustang", "year": 1964}))

    def test_negative_tuple(self):
        self.assertEqual(0, vowel_counter(("apple", "banana", "cherry")))

    def test_negative_boolean(self):
        self.assertEqual(0, vowel_counter(True))

    def test_negative_zero(self):
        self.assertEqual(0, vowel_counter(0))

    def test_negative_negativeone(self):
        self.assertEqual(0, vowel_counter(-1))

    def test_negative_numbers_in_array(self):
        self.assertEqual(0, vowel_counter(["1", "2", "3", "4"]))

    def test_negative_symbols_in_array(self):
        self.assertEqual(0, vowel_counter(["1", "2", "3", "4"]))

    def test_is_not_none(self):
        value = vowel_counter(None)
        message = "Test value is not none."
        self.assertIsNotNone(value,message)

   


if __name__ == '__main__':
    unittest.main()
