import utilities
import crud

def test_delete_item():
    #assemble
    expected = utilities.print_position_list(["skateboard", "skis"])
    #act
    actual = crud.delete_item("Product", ["skates", "skateboard", "skis"], 0, "y")
    #assert
    assert actual == expected
