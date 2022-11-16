from fichier_type import Fichier


def test_can_init_Fichier():
    fic = Fichier('test.json')
    assert len(fic.name.split('.')) == 2
    
