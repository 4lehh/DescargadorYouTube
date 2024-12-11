from customtkinter import *

class FrameMP3(CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller

        label = CTkLabel(self, text="Descargar audios de YouTube", font=("Arial", 20))
        label.pack(pady=20)

        descripcion = CTkLabel(self, text="En este apartado tendrá que dejar el link del video para luego realizar una descarga.")
        descripcion.pack(pady=10)

