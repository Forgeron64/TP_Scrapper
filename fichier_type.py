import json
from idVideo_types import IDVideo,L_IDVideo

class Fichier:
    def __init__(self, name :str) -> None:
        self.name = name 
        
    def get_list_videos_id_from_JsonFile(self):
        with open(self.name, 'r') as f:
            data = json.load(f) 
        l_idvideo = L_IDVideo()
        for video_id in data['videos_id']:
            vid_id = IDVideo(video_id)
            l_idvideo.add(vid_id)
        return l_idvideo
    
    def write_Json_data_to_Json_file(self,data_json):
        with open(self.name, 'w') as json_file:
            json.dump(data_json, json_file)