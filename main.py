#pip install customTkinter

from Manager import Manager

if __name__ == "__main__":
    app = Manager()
    app.geometry("1200x700")
    app.resizable(False,False)
    app.mainloop()