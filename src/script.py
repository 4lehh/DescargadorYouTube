# Script funcional

from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

class Descargador:

    # Variables
    url_video: str
    ruta_absoluta: str

    def __init__(self, url: str):
        self.url_video = url
        self.ruta_absoluta = os.path.abspath(__file__)

    def descargarVideo(self) -> None:
        
        # AGREGAR RUTAS

        youtube_video = YouTube(self.url_video)
        youtube_stream = youtube_video.streams.get_highest_resolution()
        youtube_stream.download()