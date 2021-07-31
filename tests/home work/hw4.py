import random


def make_number_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        symbol = branch + 1
        # if symbol >= 10:
        #     symbol = symbol - int(symbol/10) * 10
        # print(' ' * (height_of_tree - branch) + str(symbol) * (1 + (branch * 2)))
        # OR
        print(' ' * (height_of_tree - branch) + str((branch + 1)%10) * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')


make_number_tree(12)

number = int(input(f"Please enter your tree height for first task: "))


def task_1_make_tree_1(height: int):
    print("First way (tree trunk DO NOT counted as part of the height):")
    print(f"Printed numerical tree with height: {number + 1} inch")
    for x in range(1, height + 1):
        num = x
        if x > 9:
            num = int(str(x)[-1])
        print(' ' * (height - x) + str(num) * (2 * x - 1))
    print(' ' * (height - 1) + "|" + "\n")


def task_1_make_tree_2(height: int):
    print("Second way (tree trunk IS counted as part of the height):")
    print(f"Printed numerical tree with height: {number} inch")
    for x in range(1, height):
        num = x
        if x > 9:
            num = int(str(x)[-1])
        print(' ' * (height - x) + str(num) * (2 * x - 1))
    print(' ' * (height - 1) + "|" + "\n")


def task_2_bonus_challenge_func_3(number):
    print("Bonus challenge task (tree trunk DO NOT counted as part of the height)")
    print(f"Printed numerical tree with height: {number + 1} inch")
    for x in range(1, number + 1):
        for y in range(number - x):
            print(end=' ')
        print(pow(((10 ** x - 10) // 9) + 1, 2))
    print(' ' * (number - 1) + "|" + "\n")


task_1_make_tree_1(number)
task_1_make_tree_2(number)
task_2_bonus_challenge_func_3(number)

