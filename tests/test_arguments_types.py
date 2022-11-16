from arguments_types import Arguments


def test_can_init_Arguments():
    arg = Arguments()
    assert arg.items == []


def test_can_add_Arguments():
    arg = Arguments()   
    arg.add(['toto','tata','titi']) 
    assert arg.items != []


def test_can_get_size():
    arg = Arguments()
    arg.add(['toto','tata','titi'])
    assert arg.size() == 3
    
    
def test_can_verif_is_number_arg_4():
    arg0 = Arguments()
    arg0.add(['toto','tata','titi','tutu','tete'])
    res_bool_0 = arg0.verif_is_number_arg_4()
    
    arg1 = Arguments()
    arg1.add(['toto','tata','titi','tutu'])
    res_bool_1 = arg1.verif_is_number_arg_4()
    assert res_bool_0 and not res_bool_1
    

def test_can_verif_arg_input():
    arg0 = Arguments()
    arg0.add(['--input','input','--input'])
    res_bool0 = arg0.verif_arg_input()
    
    arg1 = Arguments()
    arg1.add(['toto','--input'])
    res_bool1 = arg1.verif_arg_input()
    
    arg2 = Arguments()
    arg2.add(['toto','--input','titi'])
    res_bool2 = arg2.verif_arg_input()
    assert not res_bool0 and res_bool1 and res_bool2
    
    
def test_can_verif_is_arg_2_jsonFile():
    arg0 = Arguments()
    arg0.add(['--input','input','inputjson'])
    res_bool0 = arg0.verif_is_arg_2_jsonFile()
    
    arg1 = Arguments()
    arg1.add(['toto','--input','input.json'])
    res_bool1 = arg1.verif_is_arg_2_jsonFile()
    
    arg2 = Arguments()
    arg2.add(['toto','--input','input.json.json'])
    res_bool2 = arg2.verif_is_arg_2_jsonFile()
    assert not res_bool0 and res_bool1 and res_bool2
    
    
def test_can_verif_arg_output():
    arg0 = Arguments()
    arg0.add(['toto','tata','titi','--output'])
    res_bool0 = arg0.verif_arg_output()
    
    arg1 = Arguments()
    arg1.add(['toto','tata','titi','--output','tutu'])
    res_bool1 = arg1.verif_arg_output()
    
    arg2 = Arguments()
    arg2.add(['toto','tata','titi','--tutu','--output'])
    res_bool2 = arg2.verif_arg_output()
    assert res_bool0 and res_bool1 and not res_bool2
    

def test_can_verif_is_arg_4_jsonFile():
    arg0 = Arguments()
    arg0.add(['--input','input','titi','--tutu','outputjson'])
    res_bool0 = arg0.verif_is_arg_4_jsonFile()
    
    arg1 = Arguments()
    arg1.add(['toto','--input','titi','--tutu','output.json'])
    res_bool1 = arg1.verif_is_arg_4_jsonFile()
    
    arg2 = Arguments()
    arg2.add(['toto','--input','titi','--tutu','output.json.json'])
    res_bool2 = arg2.verif_is_arg_4_jsonFile()
    assert not res_bool0 and res_bool1 and res_bool2
    
    
def test_can_get_input_jsonFile():
    arg = Arguments()
    arg.add(['toto','--input','input.json','--tutu','output.json'])
    assert arg.get_input_jsonFile() == 'input.json'
    
    
def test_can_get_output_jsonFile():
    arg = Arguments()
    arg.add(['toto','--input','input.json','--tutu','output.json'])
    assert arg.get_output_jsonFile() == 'output.json'
    
    