import unittest


def compare_lists(list1, list2):
    if type(list1) != list and type(list2) != list:
        raise TypeError("The data type of one or both of the inputs is not a list.")

    # ls1 = []
    # for item in list1:
    #     ls1.append(str(item))
    # ls2 = []
    # for item in list2:
    #     ls2.append(str(item))

    ls2 = list(list2[::])
    for item in list1:
        try:
            idx = ls2.index(item)
        except ValueError:
            return False
        ls2.pop(idx)

    return len(ls2) == 0

    # return sorted(ls1) == sorted(ls2)


class ListCompareTests(unittest.TestCase):
    def test_same_lists(self):
        ls1 = [1, 3, 6, 2]
        ls2 = [1, 3, 6, 2]
        self.assertTrue(compare_lists(ls1, ls2))

    def test_different_lists(self):
        ls1 = [1, 3, 6, 2]
        ls2 = [9, 8, 2, 4]
        self.assertFalse(compare_lists(ls1, ls2))

    def test_different_lengths(self):
        ls1 = [1, 3, 6, 2]
        ls2 = [1, 3, 6, 2, 4]
        self.assertFalse(compare_lists(ls1, ls2))

    def test_duplicate_values(self):
        ls1 = [1, 3, 6, 2, 1]
        ls2 = [1, 3, 6, 2, 3]
        self.assertFalse(compare_lists(ls1, ls2))

    def test_different_order(self):
        ls1 = [1, 3, 5, 7]
        ls2 = [7, 1, 5, 3]
        self.assertTrue(compare_lists(ls1, ls2))

    def test_char_list(self):
        ls1 = ['a', 'b', 'c']
        ls2 = ['a', 'b', 'd']
        self.assertFalse(compare_lists(ls1, ls2))

    # @unittest.expectedFailure
    def test_mixed_lists(self):
        ls1 = [False, 33, 'word']
        ls2 = [33, 'word', False]
        self.assertTrue(compare_lists(ls1, ls2))

    def test_mixed_types(self):
        ls1 = [4, 5, 6]
        ls2 = ['4', '5', '6']
        self.assertFalse(compare_lists(ls1, ls2))

    def test_unexpected_data_types(self):
        word1 = "abcde"
        word2 = "decba"
        self.assertRaises(TypeError, lambda :compare_lists(word1, word2))

    def test_other_collection(self):
        ls1 = [1, 3, 5, 7]
        ls2 = (1, 3, 5, 7)
        self.assertTrue(compare_lists(ls1, ls2))

    def test_with_dups(self):
        ls1 = [1, 2, 3, 2]
        ls2 = [1, 2, 3]

if __name__ == '__main__':
    unittest.main()


