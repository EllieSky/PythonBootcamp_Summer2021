import random


def make_number_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        print(' ' * (height_of_tree - branch) + str(branch + 1) * (1 + (branch * 2)))
        # max = height_of_tree * 2
        # print(' ' * (height_of_tree - branch) + '*' * (max - (max - (branch*2) - 1)))
    print(' ' * height_of_tree + '|')


make_number_tree(9)


def number_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        print(' ' * (height_of_tree - branch) + str((branch + 1) % 10) * (1 + (branch * 2)))
        # max = height_of_tree * 2
        # print(' ' * (height_of_tree - branch) + '*' * (max - (max - (branch*2) - 1)))
    print(' ' * height_of_tree + '|')


number_tree(12)


def number_symbol_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        symbol = branch + 1
        if symbol >= 10:
            symbol = symbol - int(symbol / 10) * 10
        # print(' ' * (height_of_tree - branch) + str((branch + 1)%10) * (1 + (branch * 2)))
        # max = height_of_tree * 2
        # print(' ' * (height_of_tree - branch) + '*' * (max - (max - (branch*2) - 1)))
        print('' * (height_of_tree - branch) + str(symbol) * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')


number_symbol_tree(12)
