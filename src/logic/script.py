# Script funcional

from pytubefix import YouTube
import os

class Descargador:

    # Variables
    url_video: str
    ruta_absoluta: str

    def __init__(self, url: str):
        self.url_video = url
        self.ruta_absoluta = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/').replace('/src', '') + '/download'          # Quitar el src y remplazar los \\ por / y redirigir a download


    def descargarVideo(self) -> None:
        youtube_video = YouTube(self.url_video)
        youtube_stream = youtube_video.streams.get_highest_resolution()
        youtube_stream.download(output_path=self.ruta_absoluta)
    
    def cambiarRuta(self, nueva_ruta: str) -> None:
        self.ruta_absoluta = nueva_ruta

    def __del__(self) -> None:                                                                                                        # Destructor 
        pass
    