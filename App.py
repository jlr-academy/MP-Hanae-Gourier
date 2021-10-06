import utilities
import menus

product_list=[]
courier_list=[]
orders_list=[{}]
order_status_list=[]

utilities.import_file(product_list,courier_list)

menus.main_menu(product_list,courier_list,orders_list)