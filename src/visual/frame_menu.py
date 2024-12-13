from customtkinter import *


class Menu(CTkFrame):

    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.configurationAplication()
    
    def configurationAplication(self) -> None:
        label = CTkLabel(self, text="Configuraciones del sistema", font=("Arial", 20))
        label.pack(pady=20)

        descripcion = CTkLabel(self, text="En este apartado se gestionará donde se podrá configurar algunos campos de las descargas \n Ahora te dejamos las opciones:")
        descripcion.pack(pady=30)
    
    def cambiarRuta(self) -> None:
        filedialog.askdirectory(initialdir=self.descargador.getRutaDescarga, title="Explorar la carpeta")