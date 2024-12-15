from abc import ABC, abstractmethod
from customtkinter import *
import threading
import tkinter.messagebox as messagebox

class Frames(ABC, CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
    @abstractmethod
    def configurationAplication(self) -> None:
        pass

    @abstractmethod
    def iniciarDescarga(self, url: str) -> None:
        threading.Thread(target=self.descargar, args=(url,), daemon=True).start()

    @abstractmethod
    def verExplorador(self) -> None:
        try:
            os.startfile(self.ruta_descarga)
        except Exception as e:
            messagebox.showerror("Error", f"No se ha encontrado la ruta: \n {e}")

    @abstractmethod
    def descargar(self, url: str) -> None:
        pass

    @abstractmethod
    def getRutaFrame(self) -> str:
        return self.ruta_descarga

    @abstractmethod
    def agregarDescargaHistorial(self, name_video: str) -> None:
        pass