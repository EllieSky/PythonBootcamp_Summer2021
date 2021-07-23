#   *
#  ***
# *****
#   |


# height_of_tree = 3
# print(' '*3 + '*')
# print(' '*2 + '*'*3)
# print(' ' + '*'*5)

def make_tree(height_of_tree):
    decor = 0
    for branch in range(height_of_tree):
        decor += 1
        if decor == 10:
            decor = 0
        print(' ' * (height_of_tree - branch) + str(decor) * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')

make_tree(21)


def make_symmetrical_tree(height_of_tree):
    decor = 0
    branch_sequence = []
    reversed_branch_sequence = []
    for branch in range(height_of_tree):
        decor += 1
        # if decor > 9:
        #     new_decor = 0
        #     branch_sequence = list(range(0, new_decor + 10))
        #     reversed_branch_sequence = reversed(range(0, new_decor + 10))
        #     print(' ' * (height_of_tree - branch) +
        #           "".join([str(x) for x in branch_sequence]) +
        #           "".join([str(x) for x in reversed_branch_sequence]))
        branch_sequence = list(range(0, decor - 1))
        reversed_branch_sequence = reversed(range(0, decor))
        print(' ' * (height_of_tree - branch) +
              "".join([str(x) for x in branch_sequence]) +
              "".join([str(x) for x in reversed_branch_sequence]))


    print(' ' * height_of_tree + '|')

make_symmetrical_tree(20)