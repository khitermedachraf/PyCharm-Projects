# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as x
import tkinter.ttk as z
from tkinter import filedialog


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    w = x.Tk()
    w.title("Fenêtre principale")
    w.geometry("600x600")
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

    #Les échelles - « Scale »
    ech1 = x.Scale(w, from_=0, to=10, label="Volume (dB)", tickinterval=2, length=350,
                   resolution=0.1, orient="horizontal")
    ech2 = x.Scale(w, from_=0, to=100, label="Volume (dB)", resolution=10,
                   orient="vertical")
    ech1.pack(padx=25, pady=25)
    ech2.pack()

    #Second frame
    w2 = x.Toplevel()
    w2.title("Deuxieme Fenêtre")
    w2.geometry("600x600")
    # Les boîtes de liste - « Listbox »
    liste = x.Listbox(w2)
    liste.insert("end", "ACAD")
    liste.insert("end", "GTR")
    liste.insert("end", "ISIL")
    liste.pack()

    #Les boîtes de liste déroulante - « Combobox »
    liste_deroulante = z.Combobox(w2, values=["ACAD", "GTR",
                                             "ISIL","KHITER Med Achraf"])
    liste_deroulante.current(3)
    liste_deroulante.pack(padx=25, pady=25)

    # Les menus - « Menu »
    m = x.Menu(w2)
    sous_menu = x.Menu(m, tearoff=0)
    sous_menu.add_command(label="Sous-menu 1")
    sous_menu.add_command(label="Sous-menu 2")
    sous_menu.add_command(label="Sous-menu 3")
    m.add_cascade(label="Menu", menu=sous_menu)
    w2.config(menu=m)

    # Open Files Dialog Box - Python Tkinter GUI Tutorial



    quitter = x.Button(w, text="Quitter", command=w.quit)
    quitter2 = x.Button(w2, text="Quitter", command=w.quit)
    quitter.pack()
    quitter2.pack()
    w.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
