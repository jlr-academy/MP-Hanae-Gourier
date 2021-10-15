import utilities
import menus

product_list=[]
courier_list=[]
orders_list=[]

if __name__ =="__main__":
    utilities.import_file(product_list, courier_list, orders_list)
    menus.main_menu(product_list,courier_list,orders_list)