import utilities
import crud
    
def test_check_duplicate(mock_list, mock_item, expected):
    #assemble
    #act
    actual = utilities.check_duplicate(mock_list, mock_item)
    #assert     
    assert expected == actual
test_check_duplicate(["skates", "skateboard", "skis"], "skates", True)
test_check_duplicate(["skates", "skateboard", "skis"], "wakeboard", False)

def test_delete_item(mock_sub_menu_item, mock_list, mock_position, mock_confirmation):
    #assemble
    expected = utilities.position_list(["skateboard", "skis"])
    #act
    actual = crud.delete_item(mock_sub_menu_item, mock_list, mock_position, mock_confirmation)
    #assert
    assert actual == expected
#test_delete_item("Product", ["skates", "skateboard", "skis"], 0, "y")