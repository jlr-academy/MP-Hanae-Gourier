import Utilities

def add_item(list):  
    while True:
        new_item=input("Please type new item name").title()
        if Utilities.check_duplicate(list, new_item):
            print("Error, item already in list")
            break
        else:
            list.append(new_item)
            print(list)
            break

def amend_item(list):
    while True:
        Utilities.position_list(list)
        position=int(input("\n Please type position in the list of item to be modified"))-1
        if position >=len(list):
            print("\n Error, number not available in list\n")
        else:
            modified_item=input("\n Please type new item name for the chosen position")
            print("\n")
            if Utilities.check_duplicate(list, modified_item):
                print("Error, item already in list")
                break
            else:
                list[position]=modified_item
                Utilities.position_list(list)
                break

def delete_item(list):
    while True:
        Utilities.position_list(list)
        position=int(input("\n Please type position in the list of item to be deleted"))-1
        confirmation=input(f"Are you sure you want to delete item {position+1, list[position]}? Please select Y to confirm")
        print("\n")
        if confirmation.upper()=="Y":
            list.pop(position)
            Utilities.position_list(list)
            break
        else:
            print("Error, item already in list")
            break