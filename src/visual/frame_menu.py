from customtkinter import *


class Menu(CTkFrame):

    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.configurationAplication()
    
    def configurationAplication(self) -> None:
        label = CTkLabel(self, text="Configuraciones del sistema", font=("Arial", 20))
        label.pack(pady=20)

        descripcion = CTkLabel(self, text="En este apartado se gestionará donde se .")
        descripcion.pack(pady=30)