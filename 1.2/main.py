# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

    actual_calorien_elv = 0
    calorien_elv_list = []
    backup_calorien = 0
    f = open("data", "r")
    for x in f:
        if x == '\n':
            calorien_elv_list.append(int(str(actual_calorien_elv)))
            actual_calorien_elv = 0
        else:
            actual_calorien_elv = actual_calorien_elv + int(str(x))

    for i in range(0,3):
        index = calorien_elv_list.index(max(calorien_elv_list))
        backup_calorien = backup_calorien + calorien_elv_list.pop(index)

        print(backup_calorien)

    print(backup_calorien)

    print(max(calorien_elv_list))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
