#     *
#    ***
#   *****
#
import random


def make_tree_with_numbers(height_of_tree: int = random.randint(1, 50)):
    for branch in range(1, height_of_tree+1):
        print(' ' * (height_of_tree-branch) + (str(branch)) * (branch*2-1)) if branch <= 9 else\
            print(' ' * (height_of_tree - branch) + (str(branch % 10)) * (branch * 2 - 1))
    print(' ' * (height_of_tree-1)+'|')


make_tree_with_numbers()