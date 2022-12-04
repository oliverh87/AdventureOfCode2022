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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    points = 0
    f = open("data", "r")
    for x in f:
        points = points + get_value_of_backpack(x)
        print("acctusl points: " + str(points))
    print(points)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
