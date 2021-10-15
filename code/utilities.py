from os import system
import csv

def import_file(product_list, courier_list, orders_list):
    read_txt_files(product_list, "products.csv")
    read_txt_files(courier_list, "courier.csv")
    read_txt_files(orders_list, "orders.csv")

def read_txt_files(my_list, file_name): 
    try:
        with open(file_name) as file: 
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                my_list.append(row)
        return my_list
    except:
        print("Failed to open file")

def save_list(product_list, courier_list, orders_list):
    export_to_csv(product_list, "products.csv",["name", "price"])
    export_to_csv(courier_list, "courier.csv",["name", "phone"])
    export_to_csv(orders_list, "orders.csv",["customer_name", "customer_address","customer_phone", "courier", "status", "items"])

def export_to_csv(list, file_name, field_names):
        try:
            with open(file_name, "w") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(list)
        except:
            print(f"Error, could not save {file_name} list")
    
def check_duplicate(my_list, item, category):
    for dictionary in my_list:
        if item.lower() in dictionary[category].lower(): 
            return True
        return False

def clear_screen():
    system("cls")

def print_dict(dict):
    print("\n")
    num = 1
    for key, value in dict.items():
        print(num, "-", key, ":", value)
        num += 1
    print("\n")

def print_position_list_enum(my_list):
    print("\n")
    for index, item in enumerate(my_list, start=1):
            print({index},"-",{item})

def print_position_list(my_list):
    print("\n")
    num = 1
    for dict in my_list:
        print(num, "-", dict)
        num +=1

def print_product_position_list_pretty(my_list):
    print ("\n{:<10} {:<25} {:<10}".format('Index', 'Product Name', 'Product Price (GBP)'))
    num=1
    for dict in my_list:
        print ("{:<10} {:<25} {:<10}".format("  "+str(num), dict["name"], "     "+str(dict["price"])))
        num+=1

def print_courier_position_list_pretty(my_list):
    print ("\n{:<10} {:<25} {:<10}".format('Index', 'Courier Name', 'Courier Phone Number'))
    num=1
    for dict in my_list:
        print ("{:<10} {:<25} {:<10}".format("  "+str(num), dict["name"], "     "+str(dict["phone"])))
        num+=1

def print_orders_position_list_pretty(my_list):
    print ("\n{:<8} {:<18} {:<50} {:<17} {:<10} {:<14} {:<9}".format('Index', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items Ordered'))
    num=1
    for dict in my_list:
        print ("{:<8} {:<18} {:<50} {:<17} {:<10} {:<14} {:<9}".format("  "+str(num), dict["customer_name"], dict["customer_address"], dict["customer_phone"],"   "+str(dict["courier"]),dict["status"],dict["items"]))
        num+=1

def print_any_position_list_pretty(sub_menu_item, my_list):
    if sub_menu_item == "Product":
        print_product_position_list_pretty(list)
    elif sub_menu_item == "Courier":
        print_courier_position_list_pretty(list)
    elif sub_menu_item == "Orders":
        print_orders_position_list_pretty(list)

def get_list_of_dict_keys(dict):
    list_of_keys=[]
    for key in dict.keys():
        list_of_keys.append(key)
    return list_of_keys

def list_orders_by_status(my_list):
    list_of_orders_by_status= sorted(my_list, key = lambda category : category["status"])
    num = 1
    for dict in list_of_orders_by_status:
        print(dict["status"], "-", dict)
        num +=1

def list_orders_by_courier(my_list):
    list_of_orders_by_courier= sorted(my_list, key = lambda category : category["courier"])
    num = 1
    for dict in list_of_orders_by_courier:
        print(dict["courier"], "-", dict)
        num +=1

def check_valid_phone_number(phone): #need to add to menu!!!
    try:
        int(phone)
        return int(phone)
    except:
        print("Error, this is not a valid phone number")
        return ValueError

def print_logo(file_name):
    logo= open (file_name,"r")
    print(" ".join([line for line in logo]))