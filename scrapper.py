import sys
from arguments_types import Arguments
from idVideo_types import L_IDVideo
from fichier_type import Fichier



    
    

def main() -> int:
    arguments_from_command_line = Arguments()
    arguments_from_command_line.add(sys.argv)

    if not arguments_from_command_line.verif_is_number_arg_4():
        print("Vous n'avez pas mis le bon nombre d'arguments.")
        print("Veuillez utiliser la typographie suivante : \n\npython scrapper.py --input nom_fichier_input.json --output nom_fichier_output.json")
    elif not arguments_from_command_line.verif_arg_input():
        print("Vous n'avez pas correctement instancier l'argument '--input'")
        print("Veuillez utiliser la typographie suivante : \n\npython scrapper.py --input nom_fichier_input.json --output nom_fichier_output.json")
    elif not arguments_from_command_line.verif_is_arg_2_jsonFile():
        print("Le fichier d'entree n'est pas un fichier .json")
        print("Veuillez utiliser la typographie suivante : \n\npython scrapper.py --input nom_fichier_input.json --output nom_fichier_output.json")
    elif not arguments_from_command_line.verif_arg_output():
        print("Vous n'avez pas correctement instancier l'argument '--output'")
        print("Veuillez utiliser la typographie suivante : \n\npython scrapper.py --input nom_fichier_input.json --output nom_fichier_output.json")
    elif not arguments_from_command_line.verif_is_arg_4_jsonFile():
        print("Le fichier de sortie n'est pas un fichier .json")
        print("Veuillez utiliser la typographie suivante : \n\npython scrapper.py --input nom_fichier_input.json --output nom_fichier_output.json")
    else:
        fic_input = Fichier(arguments_from_command_line.get_input_jsonFile())
        fic_output = Fichier(arguments_from_command_line.get_output_jsonFile())

        l_idvideo = fic_input.get_list_videos_id_from_JsonFile()
        l_video = l_idvideo.to_videotheque()
        
        fic_output.write_Json_data_to_Json_file(l_video.to_json())
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
    






