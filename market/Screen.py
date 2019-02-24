import tkinter as tk


class Screen:
    __root = tk.Tk()

    def __init__(self):
        self.__root.title("Mercado")
        tk.Label(self.__root,
                         text="Login",
                         fg="green",
                         font="Helvetica 16 bold italic").pack()
        self.__root.mainloop()