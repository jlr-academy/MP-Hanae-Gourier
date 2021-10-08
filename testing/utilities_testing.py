import code.utilities
    
def test_check_duplicate(mock_list, mock_item, expected):
    #assemble
    #act
    actual = code.utilities.check_duplicate(mock_list, mock_item)
    #assert     
    assert expected == actual
test_check_duplicate(["skates", "skateboard", "skis"], "skates", True)
test_check_duplicate(["skates", "skateboard", "skis"], "wakeboard", False)