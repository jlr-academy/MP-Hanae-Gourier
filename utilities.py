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

def save_list(orders_list):
    export_to_csv(orders_list, "orders.csv",["customer_name", "customer_address","customer_phone", "courier", "status", "items"])

def export_to_csv(my_list, file_name, field_names):
        try:
            with open(file_name, "w") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(my_list)
        except:
            print(f"Error, could not save {file_name} list")
    
def check_duplicate(my_list, item, category):
    for dictionary in my_list:
        return item.lower() in dictionary[category].lower()

def clear_screen():
    system("cls")

def print_dict(dict):
    print("\n")
    for num, (key, value) in enumerate(dict.items(), start=1):
        print(num, "-", key, ":", value)
    print("\n")

def print_position_list(my_list):
    print("\n")
    for num, dict in enumerate(my_list, start=1):
        print(num, "-", dict)

def print_product_position_list_pretty():
    my_list=open_database_product_table([])
    printy ("\n{:<10} {:<25} {:<20} {:<25}".format('Index', 'Product Name', 'Product Price (GBP)', 'Product Quantity(Units)'), 'y>B')
    for dict in my_list:
        formatted_price=format((float(dict["product_price"])), ".2f")
        print ("{:<10} {:<25} {:<20} {:<25}".format("  "+str(dict["product_id"]), dict["product_name"], "     "+str(formatted_price),"     "+str(dict["product_quantity"])))

def print_courier_position_list_pretty():
    my_list=open_database_courier_table([])
    printy ("\n{:<10} {:<25} {:<10}".format('Index', 'Courier Name', 'Courier Phone Number'), 'y>B')
    for dict in my_list:
        print ("{:<10} {:<25} {:<10}".format("  "+str(dict["courier_id"]), dict["courier_name"], "     "+str(dict["courier_phone"])))

def print_orders_position_list_pretty(my_list):
    printy ("\n{:<8} {:<18} {:<50} {:<17} {:<10} {:<17} {:<9}".format('Index', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items Ordered'), 'y>B')
    for num, dict in enumerate(my_list, start=1):
        print ("{:<8} {:<18} {:<50} {:<17} {:<10} {:<17} {:<9}".format("  "+str(num), dict["customer_name"], dict["customer_address"], dict["customer_phone"],"   "+str(dict["courier"]),dict["status"],dict["items"]))

def print_any_position_list_pretty(sub_menu_item, my_list):
    if sub_menu_item == "Product":
        print_product_position_list_pretty()
    elif sub_menu_item == "Courier":
        print_courier_position_list_pretty()
    elif sub_menu_item == "Orders":
        print_orders_position_list_pretty(my_list)

def get_list_of_dict_keys(dict):
    return [key for key in dict.keys()]

def print_orders_position_list_by_status_pretty(my_list):
    list_of_orders_by_status= sorted(my_list, key = lambda category : category["status"])
    printy ("\n {:<17} {:<8} {:<18} {:<50} {:<17} {:<10} {:<9}".format('Status', 'Index', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Items Ordered'), 'y>B')
    for num, dict in enumerate(list_of_orders_by_status, start=1):
        print ("{:<17} {:<8} {:<18} {:<50} {:<17} {:<10} {:<9}".format(" "+str(dict["status"]), "  "+str(num), " "+str(dict["customer_name"]), " "+str(dict["customer_address"]), " "+str(dict["customer_phone"]),"   "+str(dict["courier"])," "+str(dict["items"])))

def print_orders_position_list_by_courier_pretty(my_list):
    list_of_orders_by_courier= sorted(my_list, key = lambda category : category["courier"])
    printy ("\n {:<10} {:<8} {:<18} {:<50} {:<17} {:<17} {:<9}".format('Courier', 'Index', 'Customer Name', 'Customer Address', 'Customer Phone', 'Status', 'Items Ordered'), 'y>B')
    for num, dict in enumerate(list_of_orders_by_courier, start=1):
        print ("{:<10} {:<8} {:<18} {:<50} {:<17} {:<17} {:<9}".format("   "+str(dict["courier"]), "  "+str(num), " "+str(dict["customer_name"]), " "+str(dict["customer_address"]), " "+str(dict["customer_phone"])," "+str(dict["status"]), " "+str(dict["items"])))

def print_logo(app_name):
    print("\n")
    logo_font = Figlet(font='stampatello', justify="center")
    printy(logo_font.renderText(app_name),"cB")

def transform_inputs_into_list(inputs):
    input_list=inputs.split()
    for i in range(len(input_list)):
        input_list[i]=int(input_list[i])
    return input_list

def select_quantities_from_product_table():
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
        database=database)
        cursor = connection.cursor()
        sql="SELECT product_id, product_quantity FROM product"
        cursor.execute(sql)
        list_of_tuples=cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return list_of_tuples
    except:
        print("Failed to open product database table") 

def select_changing_quantities(my_list):
    my_list_set=set(my_list)
    final_list=[]
    for item in my_list_set:
        changing_quantities=[item, my_list.count(item)]
        final_list.append(changing_quantities)
    return final_list

def define_new_product_quantities(previous_quantities:list, order_quantities:list):
    for item in previous_quantities:
        for x in order_quantities:
            if item[0]==x[0]:
                new_item_quantity=int(item[1])-int(x[1])
                if new_item_quantity>=0:
                    item[1]=new_item_quantity
                else:
                    raise Exception("Error, not enough stock")
    return previous_quantities

def reverse_new_product_quantities(previous_quantities:list, order_quantities:list):
    for item in previous_quantities:
        for x in order_quantities:
            if item[0]==x[0]:
                new_item_quantity=int(item[1])+int(x[1])
                item[1]=new_item_quantity
    return previous_quantities   

def converting_tuples_into_lists(list_of_tuples:list):
    return [list(tuple) for tuple in list_of_tuples]

def upload_new_quantities_to_db(order_quantities:list):
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
        database=database)
        cursor = connection.cursor()
        for item in order_quantities:
            product_id=int(item[0])
            product_quantity=int(item[1])
            sql="UPDATE product set product_quantity=%s WHERE product_id=%s"
            val=(str(product_quantity), str(product_id))
            cursor.execute(sql,val)
        connection.commit()
        cursor.close()
        connection.close()
    except:
        print("Failed to open product database table")

def cancel_previous_order_products(amended_items_list:list):
    previous_quantities_tuples=select_quantities_from_product_table()
    previous_quantities=converting_tuples_into_lists(previous_quantities_tuples)
    order_quantities=select_changing_quantities(amended_items_list)
    new_quantities=reverse_new_product_quantities(previous_quantities, order_quantities)
    upload_new_quantities_to_db(new_quantities)

def update_db_quantities(amended_items_list:list):
    previous_quantities_tuples=select_quantities_from_product_table()
    previous_quantities=converting_tuples_into_lists(previous_quantities_tuples)
    order_quantities=select_changing_quantities(amended_items_list)
    new_quantities= define_new_product_quantities(previous_quantities, order_quantities)
    upload_new_quantities_to_db(new_quantities)