# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm . je suis KHITER Mohamed Achraf')

    fact = (lambda x: 1 if (x == 0) else (x * fact(x - 1)))
    print(fact(5))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
