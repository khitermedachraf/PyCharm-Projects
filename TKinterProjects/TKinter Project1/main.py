# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as x

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    w = x.Tk()
    w.title("Fenêtre principale")
    w.geometry("300x300")
    cadre = x.Frame(w, width=150, height=150, bg="red")
    cadre.pack()

    etiquette = x.Label(cadre, text="Ceci est un cadre")
    etiquette.pack(padx=25, pady=25)

    champ = x.Entry(w, width=15)
    champ.pack()

    case1 = x.Checkbutton(w, text="Case à cocher 1")
    case2 = x.Checkbutton(w, text="Case à cocher 2")
    case1.pack()
    case2.pack()

    champ = x.Entry(w, width=15)
    champ.pack()
    #Les boutons radio - « Radiobutton »
    y = x.IntVar()
    bouton_radio1 = x.Radiobutton(w, text="Bouton radio1", variable=y, value=1)
    bouton_radio2 = x.Radiobutton(w, text="Bouton radio2", variable=y, value=2)
    bouton_radio3 = x.Radiobutton(w, text="Bouton radio3", variable=y, value=3)
    bouton_radio1.pack()
    bouton_radio2.pack()
    bouton_radio3.pack()
    quitter = x.Button(w, text="Quitter", command=w.quit)
    quitter.pack()
    w.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
