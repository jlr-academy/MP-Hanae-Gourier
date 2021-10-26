import utilities
from unittest.mock import patch
import csv

def test_import_file():
    pass

def test_read_csv_file():
    pass

def test_open_database_product_table():
    pass

def test_open_database_courier_table():
    pass

def test_save_list():
    pass

def test_export_to_csv():
    #assemble
    test_list = [{"name":"skates", "price": 65}, {"name":"skateboard", "price": 50}, {"name":"skis", "price": 140}]
    test_file_name = "test_products.csv"
    expected = [{"name":"skates", "price": "65"}, {"name":"skateboard", "price": "50"}, {"name":"skis", "price": "140"}]
    actual_list=[]
    #act
    actual=utilities.export_to_csv(test_list, test_file_name, ["name", "price"])      
    #assert
    with open(test_file_name) as file: 
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            actual_list.append(row)
        print(actual_list)
        print(expected)
        assert actual_list == expected

def test_check_there_is_duplicate():
    #assemble
    test_list = [{"name":"skates", "price": 65}, {"name":"skateboard", "price": 50}, {"name":"skis", "price": 140}]
    test_item = "skates"
    expected = True
    #act
    actual = utilities.check_duplicate(test_list, test_item, "name")
    #assert     
    assert expected == actual

def test_check_there_is_no_duplicate():
    #assemble
    test_list = [{"name":"skates", "price": 65}, {"name":"skateboard", "price": 50}, {"name":"skis", "price": 140}]
    test_item ="wakeboard"
    expected = False
    #act
    actual = utilities.check_duplicate(test_list, test_item, "name")
    #assert     
    assert expected == actual

def test_clear_screen():
    pass

@patch('builtins.print')
def test_print_dict(mock_print): #happy path
    #assemble
    test_dict={"la":"ba", "ra":"ta", "wa":"na"}
    expected = 5
    #act
    utilities.print_dict(test_dict)
    #assert
    mock_print.call_count == expected

@patch('builtins.print')
def test_print_position_list(mock_print): #happy path
    #assemble
    test_list=["la","ba","ra"]
    expected =4
    #act
    utilities.print_position_list(test_list)
    #assert
    assert mock_print.call_count == expected


def test_print_product_position_list_pretty():
    pass

def test_print_courier_position_list_pretty():
    pass

@patch('builtins.print')
def test_print_orders_position_list_pretty(mock_print): #happy path - FAILS!!!!! TO BE FIXED!!!
    #assemble
    test_list=[{
                "customer_name": "John",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": 2,
                "status": "preparing",
                "items": [1, 3, 4]
                },
                {
                "customer_name": "John",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": 2,
                "status": "preparing",
                "items": [1, 3, 4]
                }]
    expected=2
    #act
    utilities.print_orders_position_list_pretty(test_list)
    #assert
    assert mock_print.call_count == expected

def test_print_any_position_list_pretty():
    pass
    #need to assert that if picked product, would mock-call print_product_position_list_pretty

def test_get_list_of_dict_keys():
    #assemble
    test_dict={"ra":2, "fa":1, "na":3}
    expected=["ra", "fa", "na"]
    #act
    actual = utilities.get_list_of_dict_keys(test_dict)
    #assert
    actual == expected

def test_print_orders_position_list_by_status_pretty():
    pass

def test_print_orders_position_list_by_status_pretty():
    pass
        
def test_transform_inputs_into_lists(): #happy path
    #assemble
    inputs="1 5 24"
    expected = [1,5,24]
    #act
    actual= utilities.transform_inputs_into_list(inputs)
    #assert
    assert actual == expected

def test_changing_quantities(): #happy path
    #assemble
    my_list=[1,1,1,2,2]
    expected=[[1,3],[2,2]]
    #act
    actual=utilities.select_changing_quantities(my_list)
    #assert
    assert actual == expected

def test_define_new_product_quantities(): #happy path
    #assemble
    my_list=[[1,3],[2,2]]
    my_second_list=[[1,10],[2,10]]
    expected=[[1,7],[2,8]]
    #act
    actual=utilities.define_new_product_quantities(my_second_list, my_list)
    #assert
    assert actual == expected

def test_reverse_new_product_quantities(): #happy path
    #assemble
    my_list=[[1,3],[2,2]]
    my_second_list=[[1,10],[2,10]]
    expected=[[1,13],[2,12]]
    #act
    actual=utilities.reverse_new_product_quantities(my_second_list, my_list)
    #assert
    assert actual == expected

def test_converting_tuples_into_lists(): #happy path
    #assemble
    my_list_of_tuples=[(1,3),(2,2)]
    expected=[[1,3],[2,2]]
    #act
    actual=utilities.converting_tuples_into_lists(my_list_of_tuples)
    #assert
    assert actual == expected

def test_converting_tuples_into_lists(): #happy path
    #assemble
    my_list_of_tuples=[(1,3),(2,2)]
    expected=[[1,3],[2,2]]
    #act
    actual=utilities.converting_tuples_into_lists(my_list_of_tuples)
    #assert
    assert actual == expected


@patch('builtins.print')
def test_show_error_if_index_not_in_option_list1(mock_print): #unhappy path
    #assemble
    my_list=[3, 4, 29]
    my_index=29
    expected = 0
    #act
    utilities.show_error_if_index_not_in_option_list(my_index, my_list)
    #assert
    assert mock_print.call_count == expected

@patch('builtins.print')
def test_show_error_if_index_not_in_option_list2(mock_print): #happy path
    #assemble
    my_list=[3, 4, 29]
    my_index=28
    #act
    utilities.show_error_if_index_not_in_option_list(my_index, my_list)
    #assert
    assert mock_print.call_count == 1

@patch('builtins.print')
def test_show_error_if_indices_not_in_option_list1(mock_print): #unhappy path
    #assemble
    my_list=[3, 4, 29]
    my_indices=[3, 29]
    #act
    utilities.show_error_if_indices_not_in_option_list(my_indices, my_list)
    #assert
    assert mock_print.call_count == 0

@patch('builtins.print')
def test_show_error_if_indices_not_in_option_list2(mock_print): #happy path
    #assemble
    my_list=[3, 4, 29]
    list_of_my_indices=[3, 4, 28]
    #act
    utilities.show_error_if_indices_not_in_option_list(list_of_my_indices, my_list)
    #assert
    assert mock_print.call_count == 1

@patch('builtins.print')
def test_show_error_if_indices_not_in_option_list3(mock_print): #happy path
    #assemble
    my_list=[3, 4, 29]
    list_of_indices=[2, 4, 28]
    #act
    utilities.show_error_if_indices_not_in_option_list(list_of_indices, my_list)
    #assert
    assert mock_print.call_count == 1

@patch('builtins.print')
def test_show_error_if_indices_not_in_option_list4(mock_print): #unhappy path
    #assemble
    my_list=[3, 4, 29]
    list_of_indices=[3, 4]
    #act
    utilities.show_error_if_indices_not_in_option_list(list_of_indices, my_list)
    #assert
    assert mock_print.call_count == 0

def test_create_orders_lists_from_db():
    #assemble
    test_interm_list = [{'order_id': 1, 'product_id': [6, 19, 19]}, {'order_id': 3, 'product_id': [5, 19, 5]}, {'order_id': 4, 'product_id': [3]}]
    test_order_list = [{'order_id': 1, 'customer_name': 'Elizabeth Windsor', 'customer_address': '1 Buckingham Avenue, London', 'customer_phone': '07896534236', 'courier_id': 1, 'delivery_status': 'Placed'}, {'order_id': 3, 'customer_name': 'David Attenborough', 'customer_address': '5 Regency Road, London', 'customer_phone': '07645384956', 'courier_id': 4, 'delivery_status': 'Placed'}, {'order_id': 4, 'customer_name': 'Bear Grylls', 'customer_address': '23 Limestreet, London', 'customer_phone': '07635774626', 'courier_id': 7, 'delivery_status': 'Being Delivered'}]
    expected = [{'order_id': 1, 'customer_name': 'Elizabeth Windsor', 'customer_address': '1 Buckingham Avenue, London', 'customer_phone': '07896534236', 'courier_id': 1, 'delivery_status': 'Placed', 'items':[6, 19, 19]}, {'order_id': 3, 'customer_name': 'David Attenborough', 'customer_address': '5 Regency Road, London', 'customer_phone': '07645384956', 'courier_id': 4, 'delivery_status': 'Placed', 'items':[5, 19, 5]}, {'order_id': 4, 'customer_name': 'Bear Grylls', 'customer_address': '23 Limestreet, London', 'customer_phone': '07635774626', 'courier_id': 7, 'delivery_status': 'Being Delivered', 'items':[3]}]
    #act
    actual = utilities.create_orders_lists_from_db(test_interm_list, test_order_list)
    #assert
    actual == expected