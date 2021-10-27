import pymysql
import os
from dotenv import load_dotenv
import utilities


def import_file(product_list, courier_list, orders_list, customer_list):
    open_database_product_table(product_list)
    open_database_courier_table(courier_list)
    open_database_order_table(orders_list)
    open_database_customer_table(customer_list)


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

# def fetch_customer_id_from_db():
#     connection.insert_id()
#         try:
#         connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
#         cursor = connection.cursor()
#         cursor.execute('SELECT * FROM customer')
#         rows = cursor.fetchall()
#         for row in rows:
#             my_list.append(row)
#         close_db(cursor, connection)
#         return my_list
#     except Exception as e:
#         print(f"Failed to open customer database table. Error is: {e}")

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


def update_order_status_db(new_delivery_status, order_id):
    try:
        load_dotenv()
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "UPDATE ordeer set delivery_status=%s WHERE order_id=%s"
        val = (str(new_delivery_status), str(order_id))
        cursor.execute(sql, val)
        connection.commit()
        close_db(cursor, connection)
    except Exception as e:
        print(f"Failed to open order database table. Error is: {e}")


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


def select_customer_from_list():
    customer_id_input = input("\n Please the index of the customer chosen for this order: ")
    new_customer_id = int(customer_id_input)
    available_customers = utilities.get_list_of_customer_keys_from_db()
    if utilities.show_error_if_index_not_in_option_list(new_customer_id, available_customers):
        return
    return new_customer_id


def select_order_from_list():
    utilities.print_orders_position_list_pretty()
    order_id_input = input("\n Please enter the index of the order to be modified: ")
    order_id = int(order_id_input)
    available_orders = utilities.get_list_of_order_keys_from_db()
    if utilities.show_error_if_index_not_in_option_list(order_id, available_orders):
        return
    return order_id


def open_database_order_table(my_list):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute('SELECT o.order_id, c.customer_name, c.customer_address, c.customer_phone, o.courier_id, o.delivery_status FROM ordeer o LEFT JOIN customer c ON o.customer_id = c.customer_id')
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        close_db(cursor, connection)
        return my_list
    except Exception as e:
        print(f"Failed to open order database table. Error is: {e}")


def open_database_order_table_single_order(order_id):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        sql = "SELECT o.order_id, c.customer_name, c.customer_address, c.customer_phone, o.courier_id, o.delivery_status FROM ordeer o LEFT JOIN customer c ON o.customer_id = c.customer_id WHERE o.order_id=%s"
        val= (str(order_id))
        cursor.execute(sql, val)
        my_list_of_dict = cursor.fetchall()
        close_db(cursor, connection)
        return my_list_of_dict
    except Exception as e:
        print(f"Failed to open order database table. Error is: {e}")


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

def open_database_intermediate_order_table_single_item(my_list, order_id):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        sql = "SELECT * FROM order_items WHERE order_id=%s"
        val = (str(order_id))
        cursor.execute(sql, val)
        rows = cursor.fetchall()
        for row in rows:
            my_list.append(row)
        close_db(cursor, connection)
        return my_list
    except Exception as e:
        print(f"Failed to open intermediate order database table. Error is: {e}")


def find_customer_id_based_on_order_id(order_id):
    try:
        connection = connect_to_db(cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        sql = "SELECT o.order_id, c.customer_id FROM ordeer o LEFT JOIN customer c ON o.customer_id = c.customer_id WHERE o.order_id=%s"
        val= (str(order_id))
        cursor.execute(sql, val)
        my_list_of_dict = cursor.fetchall()
        close_db(cursor, connection)
        return my_list_of_dict
    except Exception as e:
        print(f"Failed to open order database table. Error is: {e}")


def add_new_order_to_database(new_customer_id, new_courier_id, new_delivery_status):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "INSERT INTO ordeer (customer_id, courier_id, delivery_status) VALUES (%s, %s, %s)"
        val = (str(new_customer_id), str(new_courier_id), str(new_delivery_status))
        cursor.execute(sql, val)
        connection.commit()
        raw_order_id = cursor.lastrowid
        order_id=int(raw_order_id)
        close_db(cursor, connection)
        return order_id
    except Exception as e:
        print(f"Failed to open customer database table. Error is: {e}")


def update_db_with_new_products(order_id, new_items_list):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        for product_id in new_items_list:
            sql = "INSERT INTO order_items (order_id, product_id) VALUES (%s, %s)"
            val = (str(order_id), str(product_id))
            cursor.execute(sql, val)
        connection.commit()
        close_db(cursor,connection)
    except Exception as e:
        print(f"Failed to open product database table. Error is: {e}")

def update_db_to_remove_old_products(order_id, previous_items_list):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        for item in previous_items_list:
            sql = "DELETE FROM order_items WHERE order_id=%s"
            val = (str(order_id))
            cursor.execute(sql, val)
        connection.commit()
        close_db(cursor,connection)
    except Exception as e:
        print(f"Failed to open product database table. Error is: {e}")


def modify_order_item_quantities_db(my_list, order_id):
    my_dictionary = utilities.return_correct_dict_from_list(my_list, order_id)
    previous_list = my_dictionary["items"]
    utilities.cancel_previous_order_products(previous_list)
    utilities.print_product_position_list_pretty()
    modified_item_value = input(f"\n Please enter the new indices of products ordered. Use a space to separate indices if ordering more than one product: \n").title()
    modified_item_value_list = utilities.transform_inputs_into_list(modified_item_value)
    utilities.update_db_quantities(modified_item_value_list)
    update_db_to_remove_old_products(order_id, previous_list)
    update_db_with_new_products(order_id, modified_item_value_list)

def modify_courier_in_db(new_courier_id, order_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "UPDATE ordeer set courier_id=%s WHERE order_id=%s"
        val = (str(new_courier_id), str(order_id))
        cursor.execute(sql, val)
        connection.commit()
        close_db(cursor, connection)
    except Exception as e:
        print(f"Failed to open customer database table. Error is: {e}")

def update_customer_in_db(customer_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = ('SELECT * FROM customer WHERE customer_id = %s')
        val = (str(customer_id))
        cursor.execute(sql, val)
        rows = cursor.fetchall()
        for row in rows:
            print(
                f'1 - Customer Name: {row[1]}\n2 - Customer Address: {row[2]}\n3 - Customer Phone Number: {row[3]}')
        modified_item_index = int(
            input(f"\n Please input index of the category to be modified: \n"))
        if modified_item_index == 1:
            modified_customer_name = input(
                f"\n Please type in new customer name: \n").title()
            sql = "UPDATE customer SET customer_name=%s WHERE customer_id=%s"
            val = (str(modified_customer_name), str(customer_id))
            cursor.execute(sql, val)
            connection.commit()
        elif modified_item_index == 2:
            modified_customer_address = input(
                f"\n Please type in new customer address: \n")
            sql = "UPDATE customer set customer_address=%s WHERE customer_id=%s"
            val = (str(modified_customer_address), str(customer_id))
            cursor.execute(sql, val)
            connection.commit()
        elif modified_item_index == 3:
            modified_customer_phone_input = input(f"\n Please type in new customer phone number: \n")
            if modified_customer_phone_input.isnumeric() is not True:
                print("Error, input is not a valid phone number")
                return
            modified_customer_phone = modified_customer_phone_input
            sql = "UPDATE customer set customer_phone=%s WHERE customer_id=%s"
            val = (modified_customer_phone, str(customer_id))
            cursor.execute(sql, val)
            connection.commit()
        close_db(cursor, connection)
    except Exception as e:
        print(f"Failed to open customer database table. Error is: {e}")

def update_order_with_customer_id(new_customer_id, order_id):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "UPDATE ordeer set customer_id=%s WHERE order_id=%s"
        val = (str(new_customer_id), str(order_id))
        cursor.execute(sql, val)
        connection.commit()
        close_db(cursor, connection)
    except Exception as e:
        print(f"Failed to open customer database table. Error is: {e}")