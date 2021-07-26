import unittest

def convert_int_to_list(number):
    if type(number) != int and type(number) != float:
        return [int(i) for i in str(number).replace('.' '').replace(',', '').replace('-', '')]

class IntConvertTest(unittest.TestCase):
    def test_positive_int(self):
        expected = [7,4,2,1]
        actual = convert_int_to_list(7421)
        self.assertEqual((expected, actual))

if __name__ == '__main__':
    unittest.main()
