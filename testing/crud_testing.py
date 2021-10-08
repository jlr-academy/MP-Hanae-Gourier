import code.utilities
import code.crud

def test_delete_item():
    #assemble
    expected = code.utilities.print_position_list(["skateboard", "skis"])
    #act
    actual = code.crud.delete_item("Product", ["skates", "skateboard", "skis"], 0, "y")
    #assert
    assert actual == expected
test_delete_item()
    
def test_update_order_status():
    #assemble
    mock_orders_list = [{
                    "customer_name": "Attenborough",
                    "customer_address": "Serengeti",
                    "customer_phone": "242424",
                    "courier": 3,
                    "status": "PREPARING"
                    },
                    {
                    "customer_name": "Jackson",
                    "customer_address": "Beverly Hills",
                    "customer_phone": "000000",
                    "courier": 1,
                    "status": "PREPARING"
                    }]
    expected = {
                "customer_name": "Jackson",
                "customer_address": "Beverly Hills",
                "customer_phone": "000000",
                "courier": 1,
                "status": "DELIVERED"
                }
    #act
    code.crud.update_order(mock_orders_list,1,"status", "DELIVERED")
    #assert
    if expected not in mock_orders_list:
        raise AssertionError
test_update_order_status()