from customtkinter import *
from src.visual.frame_mp4 import FrameMP4
from src.visual.frame_mp3 import FrameMP3
from src.visual.frame_menu import Menu
from PIL import Image

class Aplication(CTk):

    def __init__(self):
        # Creacion de la aplicacion
        super().__init__()
        self.title('Descargador')
        self.geometry('800x600')
        self.ruta_descarga = None

        # Configuracion de los frames
        self.configurationAplication()
    
    def configurationAplication(self):
        # Configurar el layout principal
        self.grid_columnconfigure(1, weight=1)  # Columna derecha se expande
        self.grid_rowconfigure(0, weight=1)  # Fila principal se expande

        # Menú lateral (1/3 de la ventana)
        self.menu_lateral = CTkFrame(self, width=200, corner_radius=0)
        self.menu_lateral.grid(row=0, column=0, sticky="ns")

        # Frames para las pantallas dinamicas
        self.main_frame = CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.imagenApp()


        # Botones 
        self.button_1 = CTkButton(self.menu_lateral, text="Descargar MP4", command= lambda: self.cambiarFrame(FrameMP4))
        self.button_2 = CTkButton(self.menu_lateral, text="Descargar MP3", command= lambda: self.cambiarFrame(FrameMP3))
        self.button_3 = CTkButton(self.menu_lateral, text="Configuraciones", command= lambda: self.cambiarFrame(Menu))

        self.button_1.pack(pady=10, padx=10)
        self.button_2.pack(pady=10, padx=10)
        self.button_3.pack(pady=10, padx=10)

        self.cambiarFrame(FrameMP4)

    # Trae un frame al frente
    def cambiarFrame(self, frame_class):
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, Menu):
                self.ruta_descarga = widget.getRutaFrame()
            widget.destroy()

        # Crear una nueva instancia del frame y agregarla a main_frame
        frame = frame_class(self.main_frame, self, self.ruta_descarga)
        frame.pack(fill="both", expand=True)

    def imagenApp(self) -> None:
        image_path = "assets/youtube_logo.png"
        imagen = Image.open(image_path)
        imagen_escalada = CTkImage(imagen, size=(150, 150))
        imagen_label = CTkLabel(self.menu_lateral, image=imagen_escalada, text="")
        imagen_label.pack(pady=5)
        text_label = CTkLabel(self.menu_lateral, text="DescargadorTube")
        text_label.pack(pady=10)

    def __del__(self) -> None:
        pass