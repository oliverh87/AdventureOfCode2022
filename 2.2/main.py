# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def get_attack(attack, defend):
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

def chosestatus(attack, status):
    match status:
        # lose
        case "X":
            match attack:
                case "A":
                    return get_attack(attack, "Z")
                case "B":
                    return get_attack(attack, "X")
                case "C":
                    return get_attack(attack, "Y")
                case _:
                    return 0
        # draw
        case "Y":
            match attack:
                case "A":
                    return get_attack(attack, "X")
                case "B":
                    return get_attack(attack, "Y")
                case "C":
                    return get_attack(attack, "Z")
                case _:
                    return 0
        # win
        case "Z":
            match attack:
                case "A":
                    return get_attack(attack, "Y")
                case "B":
                    return get_attack(attack, "Z")
                case "C":
                    return get_attack(attack, "X")
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
        print(chosestatus(x[0], x[2]))
        points = points + chosestatus(x[0], x[2])
    print(points)


# a b c 1 2 3     0   3   6


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
