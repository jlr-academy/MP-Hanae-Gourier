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
    customer_id_input = input("\n Please input index of customer chosen for this order: ")
    new_customer_id = int(customer_id_input)
    available_customers = utilities.get_list_of_customer_keys_from_db()
    if utilities.show_error_if_index_not_in_option_list(new_customer_id, available_customers):
        return
    return new_customer_id


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


def add_new_order_to_database(new_customer_id, new_courier_id, new_delivery_status):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "INSERT INTO ordeer (customer_id, courier_id, delivery_status) VALUES (%s, %s, %s)"
        val = (str(new_customer_id), str(new_courier_id), str(new_delivery_status))
        cursor.execute(sql, val)
        connection.commit()
        close_db(cursor, connection)
    except Exception as e:
        print(f"Failed to open customer database table. Error is: {e}")


def update_db_with_products(order_id, new_items_list):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        sql = "INSERT INTO order_items (order_id, product_id) VALUES (%s, %s)"
        for product_id in new_items_list:
            val = (str(order_id), str(product_id))
            cursor.execute(sql, val)
        connection.commit()
        close_db(cursor,connection)
    except Exception as e:
        print(f"Failed to open product database table. Error is: {e}")