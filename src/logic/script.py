# Script funcional

from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix import Channel
import os
import time

class Descargador:

    # Variables
    url_video: str
    ruta_absoluta: str

    def __init__(self, url: str, ruta_descarga: str = None):
        self.name_video = "None"
        self.url_video = url
        self.ruta_absoluta = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/').replace('/logic', '').replace('/src', '') + '/download' if ruta_descarga == None else ruta_descarga          # Quitar el src y remplazar los \\ por / y redirigir a download

    def descargarVideo(self) -> None:
        youtube_video = YouTube(self.url_video)
        youtube_stream = youtube_video.streams.get_highest_resolution()
        youtube_stream.download(output_path=self.ruta_absoluta)
        self.name_video = youtube_video.title
        time.sleep(1)
    
    def descargarAudio(self) -> None:
        youtube_audio = YouTube(self.url_video)
        youtube_stream = youtube_audio.streams.get_audio_only()
        youtube_stream.download(output_path=self.ruta_absoluta)
        self.name_video = youtube_audio.title
        time.sleep(1)
    
    def descargarPlayList(self) -> None:
        playlist = Playlist(self.url_video)
        for video in playlist.videos:
            youtube_stream = video.streams.get_audio_only()
            youtube_stream.download(output_path=self.ruta_absoluta)
        self.name_video = playlist.title
        time.sleep(1)
    
    def descargarVideoChannel(self) -> None:
        channel = Channel(self.url_video)
        for video in channel.videos:
            video.streams.get_highest_resolution().download(output_path=self.ruta_absoluta)
        self.name_video = channel.channel_name

    def cambiarRuta(self, nueva_ruta: str) -> None:
        self.ruta_absoluta = nueva_ruta
    
    def getRutaDescarga(self) -> str:
        return self.ruta_absoluta
    
    def getNameVideo(self) -> str:
        return self.name_video

    def __del__(self) -> None:                                                                                                        # Destructor 
        pass
    