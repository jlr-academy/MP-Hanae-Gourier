import menus
import pytest
from unittest.mock import patch
from unittest.mock import Mock


@patch("builtins.input", side_effect=["0", "1"])
def test_main_menu_option_0(mock_input):
    # assemble
    product_list = ["Coke", "Fanta", "Water"]
    courier_list = ["Dana", "Ilias", "Georgio"]
    orders_list = [{
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "courier": 2,
        "status": "PREPARING"
    }]
    # act and assert
    with pytest.raises(SystemExit):
        menus.main_menu(product_list, courier_list, orders_list)

# @patch("menus.sub_menu")
# @patch("builtins.input", return_value=1)
# def test_main_menu_option_1(mock_input: Mock, mock_sub_menu: Mock):
#     assemble
#     product_list = ["Coke", "Fanta", "Water"]
#     courier_list = ["Dana", "Ilias", "Georgio"]
#     orders_list = [{
#         "customer_name": "John",
#         "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
#         "customer_phone": "0789887334",
#         "courier": 2,
#         "status": "PREPARING"
#     }]
#     act
#     actual = menus.main_menu(product_list, courier_list, orders_list)
#     assert
#     assert mock_sub_menu.call_count == 1    

# def test_sub_menu():
#     #assemble

#     expected =
#     #act
#     actual=code.menus.sub_menu()

#     #assert
#     assert actual == expected
# test_sub_menu
