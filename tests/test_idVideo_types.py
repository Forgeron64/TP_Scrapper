from idVideo_types import IDVideo, L_IDVideo

def test_can_init():
    idvid = IDVideo('lTOzdYrXhQU')
    res_bool = idvid.value == 'lTOzdYrXhQU'
    assert res_bool

def test_size():
    idvid = IDVideo('lTOzdYrXhQU')
    size_idvid = idvid.size()
    assert size_idvid == 11



def test_can_init_videotheque():
    l_vidID = L_IDVideo()
    assert l_vidID != []
    
def test_can_size():
    l_vidID = L_IDVideo()
    assert l_vidID.size() >= 0

def test_can_add_videoID():
    l_vidID = L_IDVideo()
    vidID = IDVideo('lTOzdYrXhQU')
    l_vidID.add(vidID)
    assert l_vidID.size() == 1
