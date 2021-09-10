import unittest

def compare_two_lists( list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
        return result
    return result

list_one = [1, 2, 5, 7, 58]
list_two = [87, 58, 0,3]
compare_two_lists(list_one,list_two)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
