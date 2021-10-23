import utilities
import sys
import crud
from printy import printy

def display_main_menu():
    printy(
        """\n                         [c]<MAIN MENU>@\n
    Please select from the following options:\n 
        0. Exit application
        1. Product menu options
        2. Courier menu options
        3. Orders menu options\n""")

def process_main_menu(product_list, courier_list, orders_list): 
    while True:
        display_main_menu()
        user_choice1=int(input())
        if user_choice1==0:
            utilities.save_list(product_list, courier_list, orders_list)
            break
        elif user_choice1==1:
            sub_menu("Product",product_list)
        elif user_choice1==2:
            sub_menu("Courier",courier_list)
        elif user_choice1==3:
            sub_menu("Orders",orders_list)
        else:
            print("User entry not recognised, program will now exit. Thank you for visiting!")
            break
    sys.exit()

def sub_menu(sub_menu_item, list1):   
    utilities.clear_screen()
    while True:
        printy(f"""
            \n                         [c]<{sub_menu_item.upper()} MENU>@\n
    Please select from the following options:\n 
            0. Return to main menu
            1. View {sub_menu_item.lower()} list
            2. Add {sub_menu_item.lower()}""")
        if sub_menu_item=="Orders":
            print("""            3. Update existing order status
            4. Update existing order
            5. Delete order\n""")
        else:
            print(f"""            3. Update existing {sub_menu_item.lower()}
            4. Delete {sub_menu_item.lower()}\n""")
        user_choice2=int(input())
        if user_choice2==0:
            utilities.clear_screen()
            break
        elif user_choice2==1:
            utilities.clear_screen()
            if sub_menu_item=="Orders":
                display_list_orders(list1)
            elif sub_menu_item=="Product":
                utilities.print_product_position_list_pretty()
            else:
                utilities.print_courier_position_list_pretty()
        elif user_choice2==2:
            crud.add_item(sub_menu_item,list1)
        elif user_choice2==3:
            if sub_menu_item=="Orders":
                crud.update_order_status(sub_menu_item, list1)
            elif sub_menu_item=="Product":
                crud.update_product()
            else:
                crud.update_courier()
        elif user_choice2==4:
            if sub_menu_item=="Orders":
                crud.update_item(sub_menu_item,list1)
            elif sub_menu_item=="Product":
                crud.delete_product()
            else:
                crud.delete_courier()
        elif user_choice2==5 and sub_menu_item=="Orders":
            crud.delete_item(sub_menu_item,list1)
        else:
            print("User entry not recognised, program will now go back to main menu")
            break      

def display_list_orders(my_list):
    print("""Please select how you would like your list of orders to be displayed:
        1. By index number
        2. By status
        3. By courier""")
    user_choice3 = int(input())
    utilities.clear_screen()
    if user_choice3 == 1:
        utilities.print_orders_position_list_pretty(my_list)
    elif user_choice3 == 2:
        utilities.print_orders_position_list_by_status_pretty(my_list)
    elif user_choice3 == 3:
        utilities.print_orders_position_list_by_courier_pretty(my_list)
