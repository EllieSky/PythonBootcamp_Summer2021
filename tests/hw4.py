import random


def make_my_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        symbol = branch + 1
        if symbol > 9:
            symbol = str(symbol)[-1]
        print(' ' * (height_of_tree - branch) + f'{symbol}' * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')


make_my_tree(12)


def make_my_bonus_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        branch_symbols_string = ""

        for item in range(branch + 1):
            if item > 8:
                branch_symbols_string += str(item + 1)[-1]
            else:
                branch_symbols_string += str(item + 1)

        branch_symbols_string += branch_symbols_string[::-1][1:]
        print(' ' * (height_of_tree - branch) + str(branch_symbols_string))
    print(' ' * height_of_tree + '|')


make_my_bonus_tree(12)
