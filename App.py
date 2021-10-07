import utilities
import menus

product_list=[]
courier_list=[]
orders_list=[{
                "customer_name": "John",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": 2,
                "status": "preparing"
            }] #how do you print orders in a pretty manner?
order={}

utilities.import_file(product_list,courier_list)

menus.main_menu(product_list,courier_list,orders_list)