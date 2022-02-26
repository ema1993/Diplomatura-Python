from tkinter import Tk
from vista import *

class Controller():
    """
    Esta es la clase Controller la cual permite
    el flujo de información a lo largo de
    toda la aplicación
    """

    def __init__(self, windows1):
        """
        Este es el constructor de la clase Controlador
        en donde se realiza la instancia de la clase Ventanita
        """
        self.root_controler = windows1
        obj = Ventanita(self.root_controler)



if __name__ == "__main__":
    root = Tk()
    objeto = Controller(root)
    root.mainloop()