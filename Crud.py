import utilities

courier_list=["Speedy","Nifty","Express","Bolt"]
orders_list=[{
                "customer_name": "John",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": 2,
                "status": "preparing"
            }]
order={}

def add_item(list): 
    utilities.clear_screen() 
    while True:
        new_item=input("Please type new item name: \n").title()
        if utilities.check_duplicate(list, new_item):
            print("Error, item already in list")
            break
        else:
            list.append(new_item)
            utilities.clear_screen()
            print(list)
            break

def add_order():
    utilities.clear_screen()
    new_item=get_new_order(courier_list)
    orders_list.append(new_item)
    print(orders_list)

def get_new_order(courier_list):
    customer_name= input("Please input customer name: \n")
    customer_address= input("Please input customer address: \n")
    customer_phone= input("Please input customer phone: \n")
    print(utilities.position_list(courier_list)) ##Why am I getting None added to the list? 
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

def amend_item(list):
    utilities.clear_screen()
    while True:
        utilities.position_list(list)
        position=int(input("\n Please type position in the list of item to be modified: "))-1
        if position >=len(list):
            print("\n Error, number not available in list\n")
        else:
            modified_item=input("\n Please type new item name for the chosen position: \n")
            print("\n")
            if utilities.check_duplicate(list, modified_item):
                print("Error, item already in list")
                break
            else:
                utilities.clear_screen()
                list[position]=modified_item
                utilities.position_list(list)
                break

def delete_item(list):
    utilities.clear_screen()
    while True:
        utilities.position_list(list)
        position=int(input("\n Please type position in the list of item to be deleted: "))-1
        confirmation=input(f"Are you sure you want to delete item {position+1, list[position]}? Please select Y to confirm: ")
        utilities.clear_screen()
        if confirmation.upper()=="Y":
            list.pop(position)
            utilities.position_list(list)
            break
        else:
            print("Error, item already in list")
            break