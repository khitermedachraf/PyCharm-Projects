# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
import sys,re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm . je suis KHITER Mohamed Achraf')

    fact = (lambda x: 1 if (x == 0) else (x * fact(x - 1)))
    [print(fact(i)) for i in [6,7]]

    #try to compile a simple regex for Zellal USTHB exam

    var = open("secour.txt", 'w')
    a = 1
    for i in open(sys.argv[0], 'r'):
        x = re.search("[.!]??(.$)", i, re.S)
        var.write("Ligne " + str(a) + " résultat : " + x.group(1))
        a += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
