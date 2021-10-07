import utilities
import sys
import crud

def main_menu(product_list, courier_list, orders_list): 
    while True:
        print(
        """\n                         <MAIN MENU>\n
        Please select from the following options:\n 
        0. Exit application
        1. Product menu options
        2. Courier menu options
        3. Orders menu options\n""")
        user_choice1=int(input())
        if user_choice1==0:
            utilities.save_lists(product_list, courier_list)
            sys.exit()
        elif user_choice1==1:
            sub_menu("Product",product_list, product_list)
        elif user_choice1==2:
            sub_menu("Courier",courier_list, courier_list)
        elif user_choice1==3:
            sub_menu("Orders",orders_list, courier_list)
        else:
            print("User entry not recognised, program will now exit. Thank you for visiting!")
            break

def sub_menu(sub_menu_item, list1, list2):
    utilities.clear_screen()
    while True:
        print(f"""
        \n                         <{sub_menu_item.upper()} MENU>\n
        Please select from the following options:\n 
        0. Return to main menu
        1. View {sub_menu_item.lower()} list
        2. Add {sub_menu_item.lower()}
        3. Update existing {sub_menu_item.lower()}
        4. Delete {sub_menu_item.lower()}\n
    """)
        user_choice2=int(input())
        if user_choice2==0:
            utilities.clear_screen()
            break
        elif user_choice2==1:
            utilities.clear_screen()
            print(list1)
        elif user_choice2==2:
            if sub_menu_item=="Orders":
                crud.add_order(list1,list2)
            else:
                crud.add_item(sub_menu_item,list1)
        elif user_choice2==3:
            if sub_menu_item=="Orders":
                crud.update_order(sub_menu_item,list1)
            else:
                crud.update_item(sub_menu_item,list1)
        elif user_choice2==4:
            crud.delete_item(sub_menu_item,list1)
        else:
            print("User entry not recognised, programme will now go back to main menu")
            break      