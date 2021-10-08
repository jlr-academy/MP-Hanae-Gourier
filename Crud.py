import utilities

def add_item(sub_menu_item, list): 
    utilities.clear_screen() 
    while True:
        new_item=input(f"Please type new {sub_menu_item.lower()} name: \n").title()
        if utilities.check_duplicate(list, new_item):
            print(f"Error, {sub_menu_item.lower()} already in list")
            break
        else:
            list.append(new_item)
            utilities.clear_screen()
            print(list)
            break

def add_order(list1,list2):
    utilities.clear_screen()
    new_item=get_new_order(list2)
    list1.append(new_item)
    print(list1)

def get_new_order(list):
    customer_name= input("Please input customer name: \n")
    customer_address= input("Please input customer address: \n")
    customer_phone= input("Please input customer phone: \n")
    print(utilities.position_list(list)) 
    chosen_courier=input("Please input index of courier chosen for this order: \n")
    order_status="PREPARING"
    order={
            "customer_name": customer_name,
            "customer_address": customer_address,
            "customer_phone": customer_phone,
            "courier": chosen_courier,
            "status": order_status
            }  
    return order

def update_item(sub_menu_item, list):
    utilities.clear_screen()
    while True:
        utilities.position_list(list)
        position=int(input(f"\n Please type position in the list of {sub_menu_item.lower()} to be modified: "))-1
        if position >=len(list):
            print("\n Error, number not available in list\n")
        else:
            modified_item=input(f"\n Please type new {sub_menu_item.lower()} name for the chosen position: \n")
            print("\n")
            if utilities.check_duplicate(list, modified_item):
                print(f"Error, {sub_menu_item.lower()} already in list")
                break
            else:
                utilities.clear_screen()
                list[position]=modified_item
                utilities.position_list(list)
                break

def delete_item(sub_menu_item, list, position=None, confirmation=None):   #default arguments - if not called will be this value
    utilities.clear_screen()
    while True:
        utilities.position_list(list)
        if position is None:
            position=int(input(f"\n Please type position in the list of {sub_menu_item.lower()} to be deleted: "))-1
        if confirmation is None: 
            confirmation=input(f"Are you sure you want to delete {sub_menu_item.lower()} {position+1, list[position]}? Please select Y to confirm: ")
        utilities.clear_screen()
        if confirmation.upper()=="Y":
    
            list.pop(position)
            utilities.position_list(list)
            break
        else:
            print(f"Error, {sub_menu_item.lower()} already in list")
            break

def update_order(sub_menu_item, list, position=None, category=None, new_category_input=None):
    utilities.clear_screen()
    utilities.position_list(list)
    if position is None:
        position=int(input(f"\n Please type position in the list of {sub_menu_item.lower()} to be modified: "))-1
        if position >=len(list):
            print("\n Error, number not available in list\n")
        else:
            utilities.print_dict(list[position])
            if category is None:
                category=(input("Please type position in the list of the item you would like to modify: \n"))
            if new_category_input is None:
                new_category_input=(input("Please type in the new value for this category: \n"))
    list[position][category]=new_category_input
    utilities.clear_screen()