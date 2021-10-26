import utilities
import menus
import sql_utilities

product_list = []
courier_list = []
orders_list = []
customer_list=[]

if __name__ == "__main__":
    sql_utilities.import_file(product_list, courier_list, orders_list, customer_list)
    utilities.print_logo("Cafe App")
    menus.process_main_menu(product_list, courier_list, orders_list, customer_list)
