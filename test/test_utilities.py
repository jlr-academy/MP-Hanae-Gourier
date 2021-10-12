import code.utilities
    
# def test_import_file():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.import_file()      
    
#     #assert
#     assert actual == expected
#test_import_file()


#def test_read_txt_files():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.import_file()      
    
#     #assert
#     assert actual == expected
#test_read_txt_files()

#def test_save_lists():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.save_lists()      
    
#     #assert
#     assert actual == expected
#test_save_lists()

#def test_exporting_lists():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.exporting_lists()      
    
#     #assert
#     assert actual == expected
#test_exporting_lists()

def test_check_duplicate(mock_list, mock_item, expected):
    #assemble
    #act
    actual = code.utilities.check_duplicate(mock_list, mock_item)
    #assert     
    assert expected == actual
test_check_duplicate(["skates", "skateboard", "skis"], "skates", True)
test_check_duplicate(["skates", "skateboard", "skis"], "wakeboard", False)

#def test_clear_screen():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.clear_screen()      
    
#     #assert
#     assert actual == expected
#test_clear_screen()


#def test_print_dict():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.print_dict()      
    
#     #assert
#     assert actual == expected
#test_print_dict()


#def test_print_position_list():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.print_position_list()      
    
#     #assert
#     assert actual == expected
#test_print_position_list()