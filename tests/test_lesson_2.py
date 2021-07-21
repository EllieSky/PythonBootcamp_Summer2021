import unittest


class FunInterviewQuestion(unittest.TestCase):
    def test_reverse_string(self):
        sentense = "I am a happy person"
        expected = "Person happy a am I"

        ls_sentense = sentense.split()
        rv_list = list(reversed(ls_sentense))
        new_sentense = " ".join(rv_list)
        result = new_sentense[0].upper() + new_sentense[1:]

        # result = " ".join(list(reversed(sentense.split())))[0].upper() + \
        #          " ".join(list(reversed(sentense.split())))[1:]

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
