import random



def make_number_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        print(' ' * (height_of_tree - branch) + str(branch + 1) * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')


make_number_tree(9)