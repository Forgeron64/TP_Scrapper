from video_types import Video, Videotheque

def test_can_init_video():
    vid = Video('5 recettes de pates','Micode','lTOzdYrXhQU','ceci est un commentaire')
    res_titre = vid.titre != ''
    res_videaste = vid.nomVideaste != ''
    res_videoId = vid.videoId != ''
    res_description = vid.description != ''
    assert res_titre and res_videaste and res_videoId and res_description
    




def test_can_init_videotheque():
    l_vid = Videotheque()
    assert l_vid != []
    
def test_can_size():
    l_vid = Videotheque()
    assert l_vid.size() >= 0

def test_can_add_video():
    l_vid = Videotheque()
    vid = Video('5 recettes de pates','Micode',56,'ceci est un commentaire')
    l_vid.add(vid)
    assert l_vid.size() == 1