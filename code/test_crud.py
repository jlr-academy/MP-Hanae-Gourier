import utilities
import crud
from unittest.mock import patch, Mock

#def test_add_item():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.crud.add_item()      
    
#     #assert
#     assert actual == expected
#test_add_item()


#def test_add_order():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.crud.add_order()      
    
#     #assert
#     assert actual == expected
#test_add_order()


#def test_get_new_order():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.crud.get_new_order()      
    
#     #assert
#     assert actual == expected
#test_get_new_order()

#def test_update_item():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.crud.update_item()      
    
#     #assert
#     assert actual == expected
#test_update_item()


def test_delete_item():
    #assemble
    expected = utilities.print_position_list(["skateboard", "skis"])
    #act
    actual = crud.delete_item("Product", ["skates", "skateboard", "skis"], 0, "y")
    #assert
    assert actual == expected

#def test_update_order():
#     #assemble
    
#     expected = 
#     #act
#     actual=code.crud.update_order()      
    
#     #assert
#     assert actual == expected
#test_update_order()

# @patch("builtins.input")    
# def test_update_order_status(mock_input: Mock):
#     #assemble
#     mock_orders_list = [{
#                     "customer_name": "Attenborough",
#                     "customer_address": "Serengeti",
#                     "customer_phone": "242424",
#                     "courier": 3,
#                     "status": "PREPARING"
#                     },
#                     {
#                     "customer_name": "Jackson",
#                     "customer_address": "Beverly Hills",
#                     "customer_phone": "000000",
#                     "courier": 1,
#                     "status": "PREPARING"
#                     }]
#     expected = [{
#                     "customer_name": "Attenborough",
#                     "customer_address": "Serengeti",
#                     "customer_phone": "242424",
#                     "courier": 3,
#                     "status": "PREPARING"
#                     },
#                     {
#                     "customer_name": "Jackson",
#                     "customer_address": "Beverly Hills",
#                     "customer_phone": "000000",
#                     "courier": 1,
#                     "status": "DELIVERED"
#                     }]
#     mock_input.side_effect=["1","3"]
#     #act
#     actual = crud.update_order_status(mock_orders_list,1)
#     #assert
#     assert expected == actual
