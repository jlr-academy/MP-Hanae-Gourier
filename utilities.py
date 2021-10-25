from os import system
import csv
from pyfiglet import Figlet
from printy import printy
import pymysql
import os
from dotenv import load_dotenv
import itertools

def import_file(product_list, courier_list, orders_list, customer_list):
    open_database_product_table(product_list)
    open_database_courier_table(courier_list)
    open_database_order_table(orders_list)
    open_database_customer_table(customer_list)


def read_csv_files(my_list, file_name):
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                my_list.append(row)
        return my_list
    except:
        print("Error, could not open orders file")


def open_database_product_table(my_list):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM product')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        close_db(cursor, connection)
        return (my_list)
    except Exception as e:
        print(f"Failed to open product database table. Error is: {e}")


def open_database_courier_table(my_list):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM courier')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        close_db(cursor, connection)
        return my_list
    except Exception as e:
        print(f"Failed to open courier database table. Error is: {e}")


def open_database_customer_table(my_list):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM customer')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        close_db(cursor, connection)
        return my_list
    except Exception as e:
        print(f"Failed to open customer database table. Error is: {e}")


def open_database_intermediate_order_table(my_list):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM order_items')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        close_db(cursor, connection)
        return my_list
    except Exception as e:
        print(f"Failed to open intermediate order database table. Error is: {e}")


def open_database_order_table(my_list):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT o.order_id, c.customer_name, c.customer_address, c.customer_phone, o.courier_id, d.delivery_status FROM ordeer o LEFT JOIN customer c ON o.customer_id = c.customer_id LEFT JOIN delivery_status d ON o.status_id = d.status_id')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        close_db(cursor, connection)
        return my_list
    except Exception as e:
        print(f"Failed to open order database table. Error is: {e}")


def create_orders_lists_from_db(interm_list, order_list):
    interm_list = group_interm_orders(interm_list) #[{'order_id': 1, 'product_id': [6, 19, 19]}, {'order_id': 3, 'product_id': [5, 19, 5]}, {'order_id': 4, 'product_id': [3]}]
    i=0
    for my_dict in order_list: #[{'order_id': 1, 'customer_name': 'Elizabeth Windsor', 'customer_address': '1 Buckingham Avenue, London', 'customer_phone': '07896534236', 'courier_id': 1, 'delivery_status': 'Placed'}, {'order_id': 3, 'customer_name': 'David Attenborough', 'customer_address': '5 Regency Road, London', 'customer_phone': '07645384956', 'courier_id': 4, 'delivery_status': 'Placed'}, {'order_id': 4, 'customer_name': 'Bear Grylls', 'customer_address': '23 Limestreet, London', 'customer_phone': '07635774626', 'courier_id': 7, 'delivery_status': 'Being Delivered'}]
        [new_list]=interm_list[i]["product_id"]
        my_dict.update({"items":new_list})
        i+=1
    return order_list


def save_list(orders_list, product_list, courier_list, customer_list):
    export_to_csv(orders_list, "orders.csv", ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"])
    export_to_csv(product_list, "product.csv", ["product_id", "product_name", "product_price", "product_quantity"])
    export_to_csv(courier_list, "courier.csv", ["courier_id", "courier_name", "courier_phone"])
    export_to_csv(customer_list, "customer.csv", ["customer_id", "customer_name", "customer_address", "customer_phone"])


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
    my_list = open_database_product_table([])
    printy("\n{:<10} {:<25} {:<20} {:<25}".format('Index', 'Product Name','Product Price (GBP)', 'Product Quantity(Units)'), 'y>B')
    for dict in my_list:
        formatted_price = format((float(dict["product_price"])), ".2f")
        print("{:<10} {:<25} {:<20} {:<25}".format(
            "  "+str(dict["product_id"]), dict["product_name"], "     "+str(formatted_price), "     "+str(dict["product_quantity"])))


def print_courier_position_list_pretty():
    my_list = open_database_courier_table([])
    printy("\n{:<10} {:<25} {:<10}".format(
        'Index', 'Courier Name', 'Courier Phone Number'), 'y>B')
    for dict in my_list:
        print("{:<10} {:<25} {:<10}".format(
            "  "+str(dict["courier_id"]), dict["courier_name"], "     "+str(dict["courier_phone"])))


def print_customer_position_list_pretty():
    my_list = open_database_customer_table([])
    printy("\n{:<10} {:<25} {:<50} {:<10}".format(
        'Index', 'Customer Name', 'Customer Address', 'Customer Phone Number'), 'y>B')
    for dict in my_list:
        print("{:<10} {:<25} {:<50} {:<10}".format(
            "  "+str(dict["customer_id"]), dict["customer_name"], dict["customer_address"], "     "+str(dict["customer_phone"])))


def print_orders_position_list_pretty(order_list, intermediate_order_list):
    my_list = create_db_order_list_ready_to_use(order_list, intermediate_order_list)
    printy("\n{:<8} {:<18} {:<50} {:<17} {:<10} {:<17} {:<9}".format('Index', 'Customer Name','Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items Ordered'), 'y>B')
    for num, dict in enumerate(my_list, start=1):
        print("{:<8} {:<18} {:<50} {:<17} {:<10} {:<17} {:<9}".format("  "+str(dict["order_id"]),dict["customer_name"], dict["customer_address"], dict["customer_phone"], "   "+str(dict["courier"]), dict["status"], dict["items"]))


def print_any_position_list_pretty(sub_menu_item):
    if sub_menu_item == "Product":
        print_product_position_list_pretty()
    elif sub_menu_item == "Courier":
        print_courier_position_list_pretty()
    elif sub_menu_item == "Orders":
        print_orders_position_list_pretty()
    elif sub_menu_item == "Customer":
        print_customer_position_list_pretty()


def get_list_of_dict_keys(dict):
    return [key for key in dict.keys()]


def get_list_of_product_keys_from_db():
    my_list = open_database_product_table([])
    return [my_dict['product_id'] for my_dict in my_list]


def get_list_of_courier_keys_from_db():
    my_list = open_database_courier_table([])
    return [my_dict['courier_id'] for my_dict in my_list]


def print_orders_position_list_by_status_pretty(order_list, intermediate_order_list):
    my_list = create_db_order_list_ready_to_use(order_list, intermediate_order_list)
    list_of_orders_by_status = sorted(
        my_list, key=lambda category: category["status"])
    printy("\n {:<17} {:<8} {:<18} {:<50} {:<17} {:<10} {:<9}".format('Status', 'Index','Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Items Ordered'), 'y>B')
    for num, dict in enumerate(list_of_orders_by_status, start=1):
        print("{:<17} {:<8} {:<18} {:<50} {:<17} {:<10} {:<9}".format(" "+str(dict["status"]), "  "+str(dict["order_id"]), " "+str(dict["customer_name"]), " "+str(
            dict["customer_address"]), " "+str(dict["customer_phone"]), "   "+str(dict["courier"]), " "+str(dict["items"])))


def print_orders_position_list_by_courier_pretty(order_list, intermediate_order_list):
    my_list = create_db_order_list_ready_to_use(order_list, intermediate_order_list)
    list_of_orders_by_courier = sorted(
        my_list, key=lambda category: category["courier"])
    printy("\n {:<10} {:<8} {:<18} {:<50} {:<17} {:<17} {:<9}".format('Courier', 'Index','Customer Name', 'Customer Address', 'Customer Phone', 'Status', 'Items Ordered'), 'y>B')
    for num, dict in enumerate(list_of_orders_by_courier, start=1):
        print("{:<10} {:<8} {:<18} {:<50} {:<17} {:<17} {:<9}".format("   "+str(dict["courier"]), "  "+str(dict["order_id"]), " "+str(
            dict["customer_name"]), " "+str(dict["customer_address"]), " "+str(dict["customer_phone"]), " "+str(dict["status"]), " "+str(dict["items"])))


def print_logo(app_name):
    print("\n")
    logo_font = Figlet(font='stampatello', justify="center")
    printy(logo_font.renderText(app_name), "cB")


def transform_inputs_into_list(inputs):
    input_list = inputs.split()
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    return input_list


def select_quantities_from_product_table():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "SELECT product_id, product_quantity FROM product"
        cursor.execute(sql)
        list_of_tuples = cursor.fetchall()
        connection.commit()
        close_db(cursor, connection)
        return list_of_tuples
    except Exception as e:
        print(f"Failed to open product database table. Error is: {e}")


def select_changing_quantities(my_list):
    my_list_set = set(my_list)
    final_list = []
    for item in my_list_set:
        changing_quantities = [item, my_list.count(item)]
        final_list.append(changing_quantities)
    print(final_list)


def group_interm_orders(my_list):
    sorted_list=[list(y) for x,y in itertools.groupby(sorted(my_list,key=lambda x: (x['order_id'])),lambda x: (x['order_id']))]
    return [{key:(value if key!='product_id' else list([x['product_id'] for x in my_dict])) for key,value in my_dict[0].items()} for my_dict in sorted_list]


def define_new_product_quantities(previous_quantities: list, order_quantities: list):
    for item in previous_quantities:
        for x in order_quantities:
            if item[0] == x[0]:
                new_item_quantity = int(item[1])-int(x[1])
                if new_item_quantity >= 0:
                    item[1] = new_item_quantity
                else:
                    raise Exception("Error, not enough stock")
    return previous_quantities


def reverse_new_product_quantities(previous_quantities: list, order_quantities: list):
    for item in previous_quantities:
        for x in order_quantities:
            if item[0] == x[0]:
                new_item_quantity = int(item[1])+int(x[1])
                item[1] = new_item_quantity
    return previous_quantities


def converting_tuples_into_lists(list_of_tuples: list):
    return [list(tuple) for tuple in list_of_tuples]


def upload_new_quantities_to_db(order_quantities: list):
    try:
        load_dotenv()
        connection = connect_to_db()
        cursor = connection.cursor()
        for item in order_quantities:
            product_id = int(item[0])
            product_quantity = int(item[1])
            sql = "UPDATE product set product_quantity=%s WHERE product_id=%s"
            val = (str(product_quantity), str(product_id))
            cursor.execute(sql, val)
        connection.commit()
        close_db(cursor, connection)
    except Exception as e:
        print(f"Failed to open product database table. Error is: {e}")


def cancel_previous_order_products(amended_items_list: list):
    previous_quantities_tuples = select_quantities_from_product_table()
    previous_quantities = converting_tuples_into_lists(
        previous_quantities_tuples)
    order_quantities = select_changing_quantities(amended_items_list)
    new_quantities = reverse_new_product_quantities(
        previous_quantities, order_quantities)
    upload_new_quantities_to_db(new_quantities)


def update_db_quantities(amended_items_list: list):
    previous_quantities_tuples = select_quantities_from_product_table()
    previous_quantities = converting_tuples_into_lists(
        previous_quantities_tuples)
    order_quantities = select_changing_quantities(amended_items_list)
    new_quantities = define_new_product_quantities(
        previous_quantities, order_quantities)
    upload_new_quantities_to_db(new_quantities)


def connect_to_db(cursorclass = pymysql.cursors.Cursor):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        cursorclass = cursorclass)


def close_db(cursor, connection):
    cursor.close()
    connection.close()


def show_error_if_index_not_in_option_list(my_index, my_list):
    if my_index not in my_list:
        print("Error, this courier does not exist, please try again.")
        return True


def show_error_if_indices_not_in_option_list(list_of_indices, my_list):
    for my_index in list_of_indices:
        if my_index not in my_list:
            print("Error, you have selected one or more products that do not exist, please try again")
            return True


def create_db_order_list_ready_to_use(order_list, intermediate_order_list):
    order_list = open_database_order_table(order_list)
    interm_list = open_database_intermediate_order_table(intermediate_order_list)
    create_orders_lists_from_db(interm_list, order_list)