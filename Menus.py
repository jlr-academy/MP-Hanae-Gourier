import Utilities
import sys
import Crud

def main_menu(product_list, courier_list): 
    while True:
        print(
        """\n                         <MAIN MENU>\n
        Please select from the following options:\n 
        0. Exit application
        1. Product menu options
        2. Courier menu options\n""")
        user_choice1=int(input())
        print(f"User has selected option {user_choice1}.\n")
        if user_choice1==0:
            Utilities.save_lists(product_list, courier_list)
            sys.exit()
        elif user_choice1==1:
            product_menu(product_list)
        elif user_choice1==2:
            couriers_menu(courier_list)
        else:
            print("User entry not recognised, programme will now exit")
            break

def product_menu(product_list):
    while True:
        print("""
            \n                         <PRODUCT MENU>\n
            Please select from the following options:\n 
            0. Return to main menu
            1. View product list
            2. Add product
            3. Update existing product
            4. Delete product\n
        """)
        user_choice2=int(input())
        print(f"User has selected option {user_choice2}.\n")
        if user_choice2==0:
            break
        elif user_choice2==1:
            print(product_list)
        elif user_choice2==2:
            Crud.add_item(product_list)
        elif user_choice2==3:
            Crud.amend_item(product_list)
        elif user_choice2==4:
            Crud.delete_item(product_list)
        else:
            print("User entry not recognised, programme will now go back to main menu")
            break

def couriers_menu(courier_list):
    while True:
        print("""
        \n                         <Courier MENU>\n
        Please select from the following options:\n 
        0. Return to main menu
        1. View courier list
        2. Add courier
        3. Update existing courier
        4. Delete courier\n
        """)
        user_choice2=int(input())
        print(f"User has selected option {user_choice2}.\n")
        if user_choice2==0:
            break
        elif user_choice2==1:
            print(courier_list)
        elif user_choice2==2:
            Crud.add_item(courier_list)
        elif user_choice2==3:
            Crud.amend_item(courier_list)
        elif user_choice2==4:
            Crud.delete_item(courier_list)
        else:
            print("User entry not recognised, programme will now go back to main menu")
            break