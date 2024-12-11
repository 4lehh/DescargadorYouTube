from customtkinter import *
import os
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.logic.script import Descargador


class FrameMP3(CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.descargador = Descargador(None)
        self.configurationAplication()

    def configurationAplication(self):

        # Textos iniciales

        label = CTkLabel(self, text="Descargar audios de YouTube", font=("Arial", 20))
        label.pack(pady=20)

        descripcion = CTkLabel(self, text="En este apartado tendrá que dejar el link del video para luego realizar una descarga.")
        descripcion.pack(pady=30)

        # Descarga

        label_link = CTkLabel(self, text="Ingrese el link del video", font=("Ariel", 20))
        label_link.pack(pady=10)

        entry = CTkEntry(self, placeholder_text="Link de YouTube")
        entry.pack(pady=10)

        boton_descarga = CTkButton(self, text="Descargar", command= lambda: self.iniciarDescarga(entry.get()))
        boton_descarga.pack(pady=10)

    def iniciarDescarga(self, url: str) -> None:
        threading.Thread(target=self.descargar, args=(url,), daemon=True).start()    
    
    def descargarVideo(self, url: str):
        descargador = Descargador(url)
        descargador.descargarAudio()
        print("GG")

