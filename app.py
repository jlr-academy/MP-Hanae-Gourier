import utilities
import menus

product_list = []
courier_list = []
orders_list = []
customer_list=[]
intermediate_order_list=[]

if __name__ == "__main__":
    utilities.import_file(product_list, courier_list, orders_list, customer_list)
    utilities.print_logo("Tasty's Cafe")
    menus.process_main_menu(product_list, courier_list, orders_list, customer_list)
