import json
from typing import List

class Video:
    def __init__(self, titre :str, nomVideaste:str, videoId:str, description:str) -> None:
        self.titre = titre
        self.nomVideaste = nomVideaste
        self.videoId = videoId
        self.description = description
    
    def video_to_json(self):
        res_json = {"TitreVideo" : self.titre, "NomVideaste" : self.nomVideaste, "VideoId" : self.videoId, "description" : self.description}
        return json.dumps(res_json)
        
class Videotheque:
    def __init__(self) -> None:
        self.items: List[Video] = []
        
    def size(self):
        return len(self.items)
    
    def add(self, item:Video):
        self.items.append(item)
        
    def to_json(self):
        liste = []
        for vid in self.items:
            liste.append(vid.video_to_json())
        liste_json = {"videos" : liste}
        return liste_json
    
        