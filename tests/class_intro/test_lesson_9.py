#
# def is_there_sum_of_two_numbers(ls: list, total: int):
#     '''
#         function takes 2 params: list & int
#         the list is assumed to be a list of int(s)
#
#         function will check if a pair of numbers within the list can be added to equal the 2nd param
#         If there is it will return True
#         example:
#         [3, 5, 3, 17], 8    ->  True
#         [3, 5, 3, 17], 22    ->  True
#         [3, 5, 3, 17], 17   ->  False
#
#         [3, 5, 3, 17], 11   ->  False
#         [2, 2, 2, 2, 2, 2, 2, 2], 4    ->  True
#         [2, 3, 4, 5], 4    ->  False
#         [1,3,5,7,9,11,13,15,17], 30  -> True
#
#     '''
#     result = False
#     for i in range(len(ls)):
#         # ls[i]
#         for x in range(i+1, len(ls)):
#             if ls[i] + ls[x] == total:
#                 return True
#     return False
#
#
# assert is_there_sum_of_two_numbers([3, 5, 3, 17], 8)  ==  True
# assert is_there_sum_of_two_numbers([3, 5, 3, 17], 22)  ==  True
# assert is_there_sum_of_two_numbers([3, 5, 3, 17], 17)  ==   False
#
# assert is_there_sum_of_two_numbers([3, 5, 3, 17], 11)  ==  False
# assert is_there_sum_of_two_numbers([2, 2, 2, 2, 2, 2, 2, 2], 4)  ==  True
# assert is_there_sum_of_two_numbers([2, 3, 4, 5], 4)  ==   False
#
#
# def count_matching_sum_pairs(ls: list, total: int):
#     result = 0
#     for i in range(len(ls)):
#         # ls[i]
#         for x in range(i+1, len(ls)):
#             if ls[i] + ls[x] == total:
#                 # result = result + 1
#                 result += 1
#     return result

def efficient_matching_pair(ls: list, total: int):
    for number in ls:
        result = total - number
        if number == result and ls.count(result) > 1:
            return True
        elif number != result and ls.count(result):
            return True
    return False

def efficient2_matching_pair(ls: list, total: int):
    pairs: dict = {}
    for number in ls:
        result = total - number
        if pairs.get(result):
            return True
        else:
            pairs.setdefault(number, result)
    return False

assert efficient_matching_pair([3, 5, 3, 17], 8)  ==  True
assert efficient_matching_pair([3, 5, 3, 17], 22)  ==  True
assert efficient_matching_pair([3, 5, 3, 17], 17)  ==   False

assert efficient_matching_pair([3, 5, 3, 17], 11)  ==  False
assert efficient_matching_pair([2, 2, 2, 2, 2, 2, 2, 2], 4)  ==  True
assert efficient_matching_pair([2, 3, 4, 5], 4)  ==   False