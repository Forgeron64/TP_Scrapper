from typing import List

class Arguments:
    def __init__(self) -> None:
        self.items: List[str] = []
    
    def add(self, items):
        self.items += items
    
    def size(self):
        return len(self.items)
    
    def verif_is_number_arg_4(self):
        return self.size() > 4
        
    def verif_arg_input(self):
        return self.items[1] == '--input'
    
    def verif_is_arg_2_jsonFile(self):
        fichier_json_argument_2 = self.items[2].split(".")
        return fichier_json_argument_2[len(fichier_json_argument_2) - 1] == 'json'
    
    def verif_arg_output(self):
        return self.items[3] == '--output'
    
    def verif_is_arg_4_jsonFile(self):
        fichier_json_argument_4 = self.items[4].split(".")
        return fichier_json_argument_4[len(fichier_json_argument_4) - 1] == 'json'
    
    def get_input_jsonFile(self):
        return self.items[2]
    
    def get_output_jsonFile(self):
        return self.items[4]
    
