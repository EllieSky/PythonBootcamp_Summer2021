import unittest


# Create python function that performs the following action:
# 1) takes a numeric input
# 2) converts it into a list on integers
# 3) returns a list of integers
# 4) is able to handle bad input
# Example:
# 7153  ->   [7,1,5,3]
# 0.0056  ->  [0,0,0,5,6]
# Part 2:
# Test your function using a unittest.TestCase class
# Create at least 2 negative test cases, and at least 6 total test cases.
# Hint:
#         <str>.replace()
def convert_integer_list(element):
    res = []
    for i in str(element):
        if i.isnumeric():
            res.append(int(i))
        elif not i.isnumeric():
            pass

        elif not element.isnumeric():
            raise TypeError(f"The element '{element}' is not numeric")
    return res


class MyTestCase(unittest.TestCase):
    # 7153  ->   [7,1,5,3]
    def test_convert_int_list(self):
        integer = 7153
        print(convert_integer_list(integer))
        expected_result = [7, 1, 5, 3]
        self.assertEqual(expected_result, convert_integer_list(integer))

    # 0.0056  ->  [0,0,0,5,6]
    def test_convert_float_list(self):
        number = 0.0056
        print(convert_integer_list(number))
        expected_result = [0, 0, 0, 5, 6]
        self.assertEqual(expected_result, convert_integer_list(number))

    def test_convert_negative_number(self):
        number = -56
        print(convert_integer_list(number))
        expected_result = [5, 6]
        self.assertEqual(expected_result, convert_integer_list(number))

    def test_convert_negative_float(self):
        number = -0.75656
        print(convert_integer_list(number))
        expected_result = [0, 7, 5, 6, 5, 6]
        self.assertEqual(expected_result, convert_integer_list(number))

    def test_char(self):
        word = 'word'
        self.assertRaises(TypeError, convert_integer_list(word))

    def test_special_char(self):
        char = '/+='
        self.assertRaises(TypeError, convert_integer_list(char))

    def test_list(self):
        list1 = [1, 2, 3]
        self.assertRaises(TypeError, convert_integer_list(list1))

    def test_dict(self):
        dictionary = {1: False, "Ivan": 2, 3: 'Different type'}
        self.assertRaises(TypeError, convert_integer_list(dictionary))

    def test_mix(self):
        mix = "OK", 25, True
        self.assertRaises(TypeError, convert_integer_list(mix))

    # here we receive the list values as text. only for my education.
    def test_other_way_to_handle_float_more_than_0(self):
        value = 0.0056
        result = ['0', '0', '0', '5', '6']
        if type(value) is float:
            # using command pop to delete "."
            res = sorted(str(value))
            res.pop(0)
            print(type(res))
            print(f"The list from number is {res}")


        self.assertEqual(result, res)

if __name__ == '__main__':
    unittest.main()
