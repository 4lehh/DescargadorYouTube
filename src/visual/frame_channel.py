from customtkinter import *
import os
from src.visual.frames import Frames
import tkinter.messagebox as messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.logic.script import Descargador

class FrameChannel(Frames, CTkFrame):
    def __init__(self, parent, controller=None, ruta: str = None):
        super().__init__(parent)
        self.controller = controller
        self.descargador = Descargador(None)
        self.configurationAplication()
        self.ruta_descarga = ruta
        
    
    def configurationAplication(self) -> None:
        
        # Textos iniciales

        label = CTkLabel(self, text="Descargar videos de un canal de YouTube", font=("Arial", 20))
        label.pack(pady=20)

        descripcion = CTkLabel(self, text="En este apartado tendrá que dejar el link del canal para luego realizar una descarga.")
        descripcion.pack(pady=30)

        # Boton de link

        label_link = CTkLabel(self, text="Ingrese el link del canal", font=("Ariel", 20))
        label_link.pack(pady=10)

        entry = CTkEntry(self, placeholder_text="Link de YouTube")
        entry.pack(pady=10)

        boton_descarga = CTkButton(self, text="Descargar", command= lambda: self.iniciarDescarga(entry.get()))
        boton_descarga.pack(pady=10)

        boton_descarga = CTkButton(self, text="Ir a carpeta", command= self.verExplorador)
        boton_descarga.pack(pady=10)

    def iniciarDescarga(self, url: str) -> None:
        super().iniciarDescarga(url)
    
    def verExplorador(self) -> None: 
        try:
            os.startfile(self.ruta_descarga)
        except Exception as e:
            messagebox.showerror("Error", f"No se ha encontrado la ruta: \n {e}")


    def descargar(self, url: str) -> None:
        try: 
            print(url + f" negro con {self.ruta_descarga}")
            descargador = Descargador(url, self.ruta_descarga)
            descargador.descargarVideoChannel()
            messagebox.showinfo("¡Descarga Completada!", "Se ha realizado correctamente la descarga")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo realizar la descarga por debido a un error: \n {e}")
        
    def getRutaFrame(self) -> str:
        return self.ruta_descarga



        
        



