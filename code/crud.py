import utilities

def add_item(sub_menu_item, list1, list2,list3): 
    utilities.clear_screen()
    if sub_menu_item == "Product":
        while True:
            new_item_name=input(f"Please type new {sub_menu_item.lower()} name: \n").title()
            new_item_price=float(input(f"Please type new {sub_menu_item.lower()} price: \n"))
            if utilities.check_duplicate(list1, new_item_name,"name"):
                print(f"Error, {sub_menu_item.lower()} already in list")
                break
            else:
                new_dict={"name": new_item_name, "price": new_item_price}
                list1.append(new_dict)
                utilities.clear_screen()
                utilities.print_position_list(list1)
                break
    elif sub_menu_item == "Courier":
        while True:
            new_item_name=input(f"Please type new {sub_menu_item.lower()} name: \n").title()
            new_item_phone=input(f"Please type new {sub_menu_item.lower()} phone: \n")
            if utilities.check_duplicate(list1, new_item_name,"name"):
                print(f"Error, {sub_menu_item.lower()} already in list")
                break
            else:
                new_dict= {"name": new_item_name, "phone": new_item_phone}
                list1.append(new_dict)
                utilities.clear_screen()
                utilities.print_position_list(list1)
                break
    elif sub_menu_item == "Orders":
        while True:
            new_customer_name=input(f"Please type new {sub_menu_item.lower()} cutomer name: \n").title()
            new_customer_address=input(f"Please type new {sub_menu_item.lower()} customer address: \n").title()
            new_customer_phone=input(f"Please type new {sub_menu_item.lower()} customer phone: \n")
            utilities.print_position_list(list2) 
            new_courier=input("\n Please input index of courier chosen for this order: ")
            utilities.print_position_list(["Placed", "Preparing", "Being delivered", "Delivered", "Cancelled"]) 
            new_status=input(f"\n Please type index of order status: \n").upper()
            utilities.print_position_list(list3) 
            new_items=input(f"Please type new {sub_menu_item.lower()} list of items: \n").title()
            new_dict={"customer_name": new_customer_name, "customer_address": new_customer_address, "customer_phone":new_customer_phone, "courier":new_courier, "status":new_status, "items":new_items}
            list1.append(new_dict)
            utilities.clear_screen()
            utilities.print_position_list(list1)
            break

def update_item(sub_menu_item, list):
    utilities.clear_screen()
    while True:
        utilities.print_position_list(list)
        modified_dict_index=int(input(f"\n Please input index of the item to be modified: "))-1
        if modified_dict_index >=len(list):
            print("\n Error, number not available in list\n")
        else:
            utilities.print_dict(list[modified_dict_index])
            modified_item_index=int(input(f"\n Please input index of the item to be modified: \n"))-1
            if modified_dict_index >=len(list):
                print("\n Error, number not available in list\n")#need to prevent choosing index not in list
            else:
                modified_item_value=input(f"\n Please input new value of the item to be modified: \n").title()
                dictionary = list[modified_dict_index]
                list_of_keys = utilities.get_list_of_dict_keys(dictionary)
                key_being_modified=list_of_keys[modified_item_index]
                dictionary[key_being_modified]=modified_item_value
                utilities.clear_screen()
                utilities.print_position_list(list)
                break                

def delete_item(sub_menu_item, list, position=None, confirmation=None):
    utilities.clear_screen()
    while True:
        utilities.print_position_list(list)
        if position is None:
            position=int(input(f"\n Please type position in the list of {sub_menu_item.lower()} to be deleted: "))-1
        if confirmation is None: 
            confirmation=input(f"Are you sure you want to delete {sub_menu_item.lower()} {position+1, list[position]}? Please select Y to confirm: ")
        utilities.clear_screen()
        if confirmation.upper()=="Y":
            list.pop(position)
            utilities.print_position_list(list)
            break
        else:
            #print(f"Error, {sub_menu_item.lower()} already in list")
            break

def update_order_status(sub_menu_item, list):
    utilities.clear_screen()
    while True:
        utilities.print_position_list(list)
        modified_dict_index=int(input(f"\n Please input index of the {sub_menu_item.lower()} for which status is to be modified: "))-1
        if modified_dict_index >=len(list):
            print("\n Error, number not available in list\n")
        else:
            status_list=["Placed", "Preparing", "Being delivered", "Delivered", "Cancelled"]
            utilities.print_position_list(status_list) 
            modified_item_index=int(input(f"\n Please input index of new status: \n"))-1
            modified_item_value=status_list[modified_item_index]
            dictionary = list[modified_dict_index]
            dictionary["status"]=modified_item_value
            utilities.clear_screen()
            utilities.print_position_list(list)
            break 