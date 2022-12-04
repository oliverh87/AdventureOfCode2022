# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def attack(attack, defend):
    match attack:
        case "A":
            match defend:
                case "X":
                    return 4
                case "Y":
                    return 8
                case "Z":
                    return 3
                case _:
                    return 0

        case "B":
            match defend:
                case "X":
                    return 1
                case "Y":
                    return 5
                case "Z":
                    return 9
                case _:
                    return 0

        case "C":
            match defend:
                case "X":
                    return 7
                case "Y":
                    return 2
                case "Z":
                    return 6
                case _:
                    return 0

        case _:
            return 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    points = 0
    f = open("data", "r")
    for x in f:
        test = x[0]
        test2 = x[1]
        print(x)

        points = points + attack(x[0], x[2])
    print(points)


# a b c 1 2 3     0   3   6


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
