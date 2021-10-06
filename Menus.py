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
        2. Courier menu options
        3. Order menu options\n""")
        user_choice1=int(input())
        print(f"User has selected option {user_choice1}.\n")
        if user_choice1==0:
            Utilities.save_lists(product_list, courier_list)
            sys.exit()
        elif user_choice1==1:
            sub_menu("Product")
        elif user_choice1==2:
            sub_menu("Courier")
        elif user_choice1==3:
            sub_menu("Orders")
        else:
            print("User entry not recognised, programme will now exit")
            break

def sub_menu(sub_menu_item):
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
            print(f"User has selected option {user_choice2}.\n")
            if user_choice2==0:
                break
            elif user_choice2==1:
                print(list)
            elif user_choice2==2:
                Crud.add_item(list)
            elif user_choice2==3:
                Crud.amend_item(list)
            elif user_choice2==4:
                Crud.delete_item(list)
            else:
                print("User entry not recognised, programme will now go back to main menu")
                break
            