from os import system
import csv
from pyfiglet import Figlet
from printy import printy
import pymysql
import os
from dotenv import load_dotenv

def import_file(product_list, courier_list, orders_list):
    open_database_product_table(product_list)
    open_database_courier_table(courier_list)
    read_csv_files(orders_list, "orders.csv")

def read_csv_files(my_list, file_name): 
    try:
        with open(file_name) as file: 
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                my_list.append(row)
        return my_list
    except:
        print("Failed to open file")
        
def open_database_product_table(my_list):
    try:
        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")
        connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database, 
        cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM product')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        cursor.close()
        connection.close()
        return my_list  
    except:
        print("Failed to open product database table") 

def open_database_courier_table(my_list):
    try:
        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")
        connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database, 
        cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM courier')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        cursor.close()
        connection.close()
        return my_list  
    except:
        print("Failed to open courier database table") 

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

def print_product_position_list_pretty():
    my_list=open_database_product_table([])
    print ("\n{:<10} {:<25} {:<10}".format('Index', 'Product Name', 'Product Price (GBP)'))
    num=1
    for dict in my_list:
        formatted_price=format((float(dict["product_price"])), ".2f")
        print ("{:<10} {:<25} {:<10}".format("  "+str(num), dict["product_name"], "     "+str(formatted_price)))
        num+=1

def print_courier_position_list_pretty():
    my_list=open_database_courier_table([])
    print ("\n{:<10} {:<25} {:<10}".format('Index', 'Courier Name', 'Courier Phone Number'))
    num=1
    for dict in my_list:
        print ("{:<10} {:<25} {:<10}".format("  "+str(num), dict["courier_name"], "     "+str(dict["courier_phone"])))
        num+=1

def print_orders_position_list_pretty(my_list):
    print ("\n{:<8} {:<18} {:<50} {:<17} {:<10} {:<17} {:<9}".format('Index', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items Ordered'))
    num=1
    for dict in my_list:
        print ("{:<8} {:<18} {:<50} {:<17} {:<10} {:<17} {:<9}".format("  "+str(num), dict["customer_name"], dict["customer_address"], dict["customer_phone"],"   "+str(dict["courier"]),dict["status"],dict["items"]))
        num+=1

def print_any_position_list_pretty(sub_menu_item, my_list):
    if sub_menu_item == "Product":
        print_product_position_list_pretty()
    elif sub_menu_item == "Courier":
        print_courier_position_list_pretty()
    elif sub_menu_item == "Orders":
        print_orders_position_list_pretty(my_list)

def get_list_of_dict_keys(dict):
    list_of_keys=[]
    for key in dict.keys():
        list_of_keys.append(key)
    return list_of_keys

def print_orders_position_list_by_status_pretty(my_list):
    list_of_orders_by_status= sorted(my_list, key = lambda category : category["status"])
    print ("\n {:<17} {:<8} {:<18} {:<50} {:<17} {:<10} {:<9}".format('Status', 'Index', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Items Ordered'))
    num=1
    for dict in list_of_orders_by_status:
        print ("{:<17} {:<8} {:<18} {:<50} {:<17} {:<10} {:<9}".format(" "+str(dict["status"]), "  "+str(num), " "+str(dict["customer_name"]), " "+str(dict["customer_address"]), " "+str(dict["customer_phone"]),"   "+str(dict["courier"])," "+str(dict["items"])))
        num+=1

def print_orders_position_list_by_courier_pretty(my_list):
    list_of_orders_by_courier= sorted(my_list, key = lambda category : category["courier"])
    print ("\n {:<10} {:<8} {:<18} {:<50} {:<17} {:<17} {:<9}".format('Courier', 'Index', 'Customer Name', 'Customer Address', 'Customer Phone', 'Status', 'Items Ordered'))
    num=1
    for dict in list_of_orders_by_courier:
        print ("{:<10} {:<8} {:<18} {:<50} {:<17} {:<17} {:<9}".format("   "+str(dict["courier"]), "  "+str(num), " "+str(dict["customer_name"]), " "+str(dict["customer_address"]), " "+str(dict["customer_phone"])," "+str(dict["status"]), " "+str(dict["items"])))
        num+=1

def print_logo(app_name):
    print("\n")
    logo_font = Figlet(font='stampatello', justify="center")
    printy(logo_font.renderText(app_name),"cB")