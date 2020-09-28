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

    #try to compile a simple regex for Zellal USTHB exam exo 4 :
    d = {}
    for j in zip(*[re.split("\W+", open(sys.argv[1], 'r',).read().lower())[i:] for i in range(int(sys.argv[2]))]):
        d[j] = d.get(j, 0) + 1
    [print(" ".join(k) + " " + str(d.get(k)) + "\n") for k in sorted(d) if d.get(k) == int(sys.argv[3]) and re.search("^\w{" + sys.argv[4] + "} (.+ )?\w{" + sys.argv[5] + "}$", " ".join(k))]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
