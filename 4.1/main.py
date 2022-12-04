# This is a sample Python script.
import string


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_character(first, second):
    for i in range(len(first)):
        for j in range(len(first)):
            if first[i] == second[j]:
                return first[i]


def calculate_poitns(letter_value):
    values = dict()
    print(letter_value)
    if letter_value.isupper():
        for index, letter in enumerate(string.ascii_uppercase):
            values[letter] = index + 1
        print(26 + values[letter_value])
        return 26 + values[letter_value]
    else:
        for index, letter in enumerate(string.ascii_lowercase):
            values[letter] = index + 1
        print(values[letter_value])
        return values[letter_value]


def get_value_of_backpack(item_list):
    first_compartment = item_list[0:int((len(item_list) - 1) / 2)]
    second_compartment = item_list[int((len(item_list) - 1) / 2):int(len(item_list) - 1)]
    doubble_letter = get_character(first_compartment, second_compartment)
    return calculate_poitns(doubble_letter)


def find_same_letter(list_of_group):
    for i in range(len(list_of_group[0])-1):
        for j in range(len(list_of_group[1])-1):
            for k in range(len(list_of_group[2])-1):
                if list_of_group[0][i] == list_of_group[1][j] == list_of_group[2][k]:
                    return calculate_poitns(list_of_group[2][k])


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    test = 0
    points = 0
    iterator = 0
    group_list = []
    f = open("data", "r")
    testi = 0
    for x in f:
        testi = testi + 1
        if iterator > 1:
            iterator = 0
            group_list.append(x)
            points = points + find_same_letter(group_list)
            group_list = []
            print("yes")
            print(x)
        else:
            iterator = iterator + 1
            group_list.append(x)
            print("no")
            print(x)
        if testi > 297:
            print("jhdhjd")


    print(points)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
