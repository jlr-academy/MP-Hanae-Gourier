import utilities
import pytest
from unittest import mock
import csv

@mock.patch("utilities.read_txt_files", return_value=["oops", "atchoo"]) #not a good test because this is not a good function! Need to refactor!
def test_import_file(mock_read_txt_files):
    #assemble
    #act
    utilities.import_file([],[],[])    
    #assert
    mock_read_txt_files.assert_called()

# def test_read_txt_files():
#     #assemble
#     test_list = []
#     test_file_name = "test_courier.csv"
#     #act
#     actual=utilities.read_txt_files(test_list, test_file_name)      
#     #assert
#     assert len(test_list)==2

def test_read_txt_files_that_doesnt_exist():
    #assemble
    test_list = []
    test_file_name = "doesnt_exist.txt"
    #act
    actual=utilities.read_txt_files(test_list, test_file_name)      
    #assert
    assert pytest.raises(Exception)
    
def test_read_txt_files_wrong_type():
    #assemble
    test_list = []
    test_file_name = "test_courier.txt"
    #act
    actual=utilities.read_txt_files(test_list, test_file_name)      
    #assert
    assert pytest.raises(Exception)    

@mock.patch("utilities.export_to_csv", return_value=["oops", "atchoo"])
def test_save_list(mock_export_to_csv): #not a good test because this is not a good function! Need to refactor!
    #assemble
    #act
    utilities.save_list([],[],[])      
    #assert
    mock_export_to_csv.assert_called()

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

#def test_print_dict():   #How can I check this if the original function doesn't return anything?
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.print_dict()      
    
#     #assert
#     assert actual == expected


#def test_print_position_list(): #How can I check this if the original function doesn't return anything?
#     #assemble
    
#     expected = 
#     #act
#     actual=code.utilities.print_position_list()      
    
#     #assert
#     assert actual == expected

# def test_list_orders_by_status(): #How can I check this if the original function doesn't return anything?
#     #assemble
#     test_list=[{"name":"sushi", "status":"preparing"},{"name":"sashimi", "status":"delivered"},{"name":"oyakodon", "status":"preparing"}]
#     #act
#     actual=utilities.list_orders_by_status(test_list)     
#     #assert
#     assert #???Function not returning anything so nothing to assert - what should function return????

# def test_list_orders_by_courier(): #How can I check this if the original function doesn't return anything?
#     #assemble
#     test_list=[{"name":"sushi", "courier":"2"},{"name":"sashimi", "courier":"2"},{"name":"oyakodon", "courier":"1"]
#     #act
#     actual=utilities.list_orders_by_courier(test_list)     
#     #assert
#     assert #???Function not returning anything so nothing to assert - what should function return????

def test_check_valid_phone_number_happy_path():
    #assemble
    phone="123456"
    expected=123456
    #act
    actual=utilities.check_valid_phone_number(phone)
    #assert
    assert actual == expected

def test_check_valid_phone_number_unhappy_path():
    #assemble
    phone="lalala"
    expected=ValueError
    #act
    actual=utilities.check_valid_phone_number(phone)
    #assert
    assert actual == expected