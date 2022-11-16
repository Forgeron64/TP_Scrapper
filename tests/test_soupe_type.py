from soupe_type import Soupe
from idVideo_types import IDVideo

def test_init() -> None:
    idvid = IDVideo('lTOzdYrXhQU')
    soup = Soupe(idvid.get_soup_from_video_id())
    assert soup != None
    
def test_get_nom_videaste():
    idvid = IDVideo('lTOzdYrXhQU')
    soup = Soupe(idvid.get_soup_from_video_id())
    res = soup.value.find("span", itemprop="author").next.next['content']  
    assert res == 'GOTAGA'
    
def test_get_title():
    idvid = IDVideo('lTOzdYrXhQU')
    soup = Soupe(idvid.get_soup_from_video_id())
    title = soup.value.find("meta", itemprop="name")['content']
    assert title == 'ON JOUE UN TOURNOI FIFA SPÉCIAL COUPE DU MONDE (ft. plein de monde)'
    
def test_get_description():
    idvid = IDVideo('lTOzdYrXhQU')
    soup = Soupe(idvid.get_soup_from_video_id())
    description = soup.value.find("meta",itemprop="description")['content']  
    assert description == 'Pour le lancement du mode Coupe du Monde sur FIFA, on a organisé un tournoi entre nous pour savoir qui sera le meilleur !Merci à Soprano, Hakim Jemili, Roman...'