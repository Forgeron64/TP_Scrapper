from bs4 import BeautifulSoup
from video_types import Video, Videotheque
from soupe_type import Soupe
from typing import List
import requests

class IDVideo:
    def __init__(self, value:str) -> None:
        self.value = value
    
    def size(self) -> int:
        idvid_size = len(self.value)
        return idvid_size
    
    def get_soup_from_video_id(self) -> BeautifulSoup:
        url = "https://www.youtube.com/watch?v=" + self.value
        response = requests.get(url).text
        soup = BeautifulSoup(response,features="html.parser")
        return soup
    
    def to_video(self)-> Video:
        soup = Soupe(self.get_soup_from_video_id())
        title = soup.get_title()
        nom_videaste = soup.get_nom_videaste()
        description = soup.get_description()
        vid = Video(title,nom_videaste,self.value,description)
        return vid
    

class L_IDVideo:
    def __init__(self) -> None:
        self.items: List[IDVideo] = []
        
    def size(self):
        return len(self.items)
    
    def add(self, item:IDVideo):
        self.items.append(item)
        
    def to_videotheque(self):
        l_video = Videotheque()
        for video_id in self.items :
            l_video.add(video_id.to_video())
        return l_video
        