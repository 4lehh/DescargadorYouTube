from customtkinter import *
from frame_mp4 import FrameMP4
from frame_mp3 import FrameMP3

class Aplication(CTk):

    def __init__(self):
        # Creacion de la aplicacion
        super().__init__()
        self.title('Descargador')
        self.geometry('800x600')

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


        # Botones 
        self.button_1 = CTkButton(self.menu_lateral, text="Descargar MP4", command= lambda: self.cambiarFrame(FrameMP4))
        self.button_2 = CTkButton(self.menu_lateral, text="Descargar MP3", command= lambda: self.cambiarFrame(FrameMP3))
        self.button_3 = CTkButton(self.menu_lateral, text="Configuraciones", command=self.cambiarFrame)

        self.button_1.pack(pady=10, padx=10)
        self.button_2.pack(pady=10, padx=10)
        self.button_3.pack(pady=10, padx=10)

        self.cambiarFrame(FrameMP4)

    # Trae un frame al frente
    def cambiarFrame(self, frame_class):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Crear una nueva instancia del frame y agregarla a main_frame
        frame = frame_class(self.main_frame, self)
        frame.pack(fill="both", expand=True)


    def __del__(self) -> None:
        pass


        


app = Aplication()
app.mainloop()

