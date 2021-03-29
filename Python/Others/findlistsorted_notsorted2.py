# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def findsortedlist(lst, lst_size):
    templst = lst[:]
    templst.sort()
    if templst == lst:
        return 'Yes'
    else:
        return 'No'




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for x in range(int(input().strip())):
        lst_size = int(input().strip())
        lst = list(map(int, input().strip().split()))
        print(findsortedlist(lst, lst_size))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
