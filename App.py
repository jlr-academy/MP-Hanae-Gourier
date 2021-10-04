import Utilities
import Menus

product_list=[]
courier_list=[]

Utilities.import_file(product_list,courier_list)

Menus.main_menu(product_list, courier_list)