import utilities
import crud
from unittest.mock import patch, Mock

def test_delete_item(): #happy path
    #assemble
    expected = utilities.print_position_list(["skateboard", "skis"])
    #act
    actual = crud.delete_item("Product", ["skates", "skateboard", "skis"], 0, "y")
    #assert
    assert actual == expected