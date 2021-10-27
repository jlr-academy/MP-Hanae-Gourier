import utilities
import sql_utilities


def add_product(sub_menu_item):
    utilities.clear_screen()
    while True:
            new_item_name = input(
                f"Please type new {sub_menu_item.lower()} name: \n").title()
            new_item_price_input = input(f"Please type new {sub_menu_item.lower()} price in GBP: \n")
            try:
                new_item_price = float(new_item_price_input)
            except:
                print("Error, input is not a valid price")
                return
            new_item_quantity_input = input(f"Please type new {sub_menu_item.lower()} quantity: \n")
            if new_item_quantity_input.isnumeric() is not True:
                print("Error, input is not a valid quantity")
                return
            new_item_quantity = int(new_item_quantity_input)
            try:
                connection = sql_utilities.connect_to_db()
                cursor = connection.cursor()
                sql = "INSERT INTO product (product_name, product_price, product_quantity) VALUES (%s, %s, %s)"
                val = (str(new_item_name), str(
                    new_item_price), str(new_item_quantity))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor,connection)
            except Exception as e:
                print(f"Failed to open product database table. Error is: {e}")
            break
    utilities.clear_screen()
    utilities.print_product_position_list_pretty()


def add_courier(sub_menu_item):
    while True:
        new_item_name = input(
            f"Please type new {sub_menu_item.lower()} name: \n").title()
        new_item_phone = input(
            f"Please type new {sub_menu_item.lower()} phone: \n")
        if new_item_phone.isnumeric() is not True:
            print("Error, please enter a valid phone number")
            return
        else:
            try:
                connection = sql_utilities.connect_to_db()
                cursor = connection.cursor()
                sql = "INSERT INTO courier (courier_name, courier_phone) VALUES (%s, %s)"
                val = (str(new_item_name), str(new_item_phone))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            except Exception as e:
                print(f"Failed to open courier database table. Error is: {e}")
            break
    utilities.clear_screen()
    utilities.print_courier_position_list_pretty()


def add_customer(sub_menu_item):
    while True:
        new_customer_name = input(
            f"Please type new {sub_menu_item.lower()} name: \n").title()
        new_customer_address = input(
            f"Please type new {sub_menu_item.lower()} address: \n").title()
        new_customer_phone = input(
            f"Please type new {sub_menu_item.lower()} phone: \n")
        if new_customer_phone.isnumeric() is not True:
            print("Error, input is not a valid phone number")
            return
        else:
            try:
                connection = sql_utilities.connect_to_db()
                cursor = connection.cursor()
                sql = "INSERT INTO customer (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)"
                val = (str(new_customer_name), str(new_customer_address), str(new_customer_phone))
                cursor.execute(sql, val)
                connection.commit()
                raw_new_customer_id = cursor.lastrowid
                new_customer_id = int(raw_new_customer_id)
                sql_utilities.close_db(cursor, connection)
            except Exception as e:
                print(f"Failed to open customer database table. Error is: {e}")
            break
    utilities.clear_screen()
    utilities.print_customer_position_list_pretty()
    return new_customer_name, new_customer_address, new_customer_phone, new_customer_id


def add_order():
    while True:
        new_customer_id = utilities.select_customer()
        utilities.print_courier_position_list_pretty()
        new_courier_id = int(input(
            "\n Please input index of courier chosen for this order: "))
        available_couriers=utilities.get_list_of_courier_keys_from_db()
        if utilities.show_error_if_index_not_in_option_list(new_courier_id,available_couriers):
            return
        status_list = ["PLACED", "PREPARING","BEING DELIVERED", "DELIVERED"]
        utilities.print_position_list(status_list)
        new_status_index = int(
            input("\n Please type index of order status: \n"))
        new_delivery_status = status_list[(new_status_index-1)]
        utilities.print_product_position_list_pretty()
        new_items = input(
            "Please type index of products to be added to order. To add more than one item, please separate indices with a space: \n")
        new_items_list = utilities.transform_inputs_into_list(new_items)
        available_products_list=utilities.get_list_of_product_keys_from_db()
        if utilities.show_error_if_indices_not_in_option_list(new_items_list,available_products_list):
            return
        order_id = sql_utilities.add_new_order_to_database(new_customer_id, new_courier_id, new_delivery_status)
        print(order_id)
        sql_utilities.update_db_with_new_products(order_id, new_items_list)
        utilities.update_db_quantities(new_items_list)
        utilities.clear_screen()
        utilities.print_orders_position_list_pretty()
        break


def update_product():
    utilities.clear_screen()
    while True:
        utilities.print_product_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index_input = input(f"\n Please input index of the product to be modified: ")
            modified_dict_index=int(modified_dict_index_input)
            available_products = utilities.get_list_of_product_keys_from_db()
            if utilities.show_error_if_index_not_in_option_list(modified_dict_index, available_products):
                return
            sql = ('SELECT * FROM product WHERE product_id = %s')
            val = (str(modified_dict_index))
            cursor.execute(sql, val)
            rows = cursor.fetchall()
            for row in rows:
                print(
                    f'1 - Product Name: {row[1]}\n2 - Product Price: {row[2]}\n3 - Product Quantity: {row[3]}')
            modified_item_index = int(input(f"\n Please input index of the category to be modified: \n"))
            if modified_item_index == 1:
                modified_product_name = input(
                    f"\n Please type in new product name: \n").title()
                sql = "UPDATE product SET product_name=%s WHERE product_id=%s"
                val = (str(modified_product_name), str(modified_dict_index_input))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            elif modified_item_index == 2:
                modified_product_price = float(
                    input(f"\n Please type in new product price: \n"))
                sql = "UPDATE product set product_price=%s WHERE product_id=%s"
                val = (modified_product_price, str(modified_dict_index_input))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            elif modified_item_index == 3:
                modified_product_quantity = int(
                    input(f"\n Please type in new product quantity: \n"))
                sql = "UPDATE product set product_quantity=%s WHERE product_id=%s"
                val = (modified_product_quantity, str(modified_dict_index_input))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            else:
                print("Error, index not within list, program will now return to product menu.")
                return
        except Exception as e:
            print(f"Failed to open product database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_product_position_list_pretty()


def update_courier():
    utilities.clear_screen()
    while True:
        utilities.print_courier_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index = int(input(f"\n Please input index of the courier to be modified: "))
            available_couriers = utilities.get_list_of_courier_keys_from_db()
            if utilities.show_error_if_index_not_in_option_list(modified_dict_index, available_couriers):
                return
            sql = ('SELECT * FROM courier WHERE courier_id = %s')
            val = (str(modified_dict_index))
            cursor.execute(sql, val)
            rows = cursor.fetchall()
            for row in rows:
                print(
                    f'1 - Courier Name: {row[1]}\n2 - Courier Phone Number: {row[2]}')
            modified_item_index = int(
                input(f"\n Please input index of the category to be modified: \n"))
            if modified_item_index == 1:
                modified_courier_name = input(
                    f"\n Please type in new courier name: \n").title()
                sql = "UPDATE courier SET courier_name=%s WHERE courier_id=%s"
                val = (str(modified_courier_name), str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            elif modified_item_index == 2:
                modified_courier_phone = float(
                    input(f"\n Please type in new courier phone number: \n"))
                sql = "UPDATE courier set courier_phone=%s WHERE courier_id=%s"
                val = (modified_courier_phone, str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            else:
                print("Error, index not within list, program will now return to courier menu.")
                return
        except Exception as e:
            print(f"Failed to open courier database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_courier_position_list_pretty()


def update_customer(customer_id=None):
    utilities.clear_screen()
    if customer_id == None:
        utilities.print_customer_position_list_pretty()
        customer_id = int(
            input(f"\n Please input index of the customer to be modified: "))
        available_products = utilities.get_list_of_customer_keys_from_db()
        if utilities.show_error_if_index_not_in_option_list(customer_id, available_products):
            return
        sql_utilities.update_customer_in_db(customer_id)
    elif customer_id is not None:
        sql_utilities.update_customer_in_db(customer_id)
    utilities.clear_screen()
    utilities.print_customer_position_list_pretty()


def update_order_status(my_list):
    utilities.clear_screen()
    while True:
        utilities.print_orders_position_list_pretty()
        order_id = sql_utilities.select_order_from_list()
        status_list = ["PLACED", "PREPARING","BEING DELIVERED", "DELIVERED"]
        utilities.print_position_list(status_list)
        modified_item_index = int(
            input('\n Please input index of new status: \n')) - 1
        new_delivery_status = status_list[modified_item_index]
        sql_utilities.update_order_status_db(new_delivery_status, order_id)
        utilities.clear_screen()
        utilities.print_orders_position_list_pretty()
        break


def update_order():
    utilities.clear_screen()
    order_id = sql_utilities.select_order_from_list()
    my_list = utilities.create_db_order_list_ready_to_use()
    my_list_of_dict = utilities.create_db_order_list_ready_to_use_single_item(order_id)
    utilities.print_dict(my_list_of_dict[0])
    modified_item_index = int(
        input(f"Please enter the index of the category to be modified: \n"))
    if modified_item_index == 1:
        print("Try again, changing the order_id is not recommended!")
    elif modified_item_index == 2 or modified_item_index == 3 or modified_item_index == 4:
        utilities.amend_customer_in_order(order_id)
        utilities.clear_screen()
        utilities.print_orders_position_list_pretty()
    elif modified_item_index == 5:
        utilities.print_courier_position_list_pretty()
        new_courier_id = int(input(
            f"\n Please enter index of modified courier: \n"))
        available_couriers=utilities.get_list_of_courier_keys_from_db()
        if utilities.show_error_if_index_not_in_option_list(new_courier_id,available_couriers):
            return
        sql_utilities.modify_courier_in_db(new_courier_id, order_id)
        utilities.clear_screen()
        utilities.print_orders_position_list_pretty()
    elif modified_item_index == 6:
        status_list = ["PLACED", "PREPARING","BEING DELIVERED", "DELIVERED"]
        utilities.print_position_list(status_list)
        modified_item_index = int(input('\n Please input index of new status: \n')) - 1
        new_delivery_status = status_list[modified_item_index]
        sql_utilities.update_order_status_db(new_delivery_status, order_id)
        utilities.clear_screen()
        utilities.print_orders_position_list_pretty()
    elif modified_item_index == 7:
        sql_utilities.modify_order_item_quantities_db(my_list, order_id)
        utilities.clear_screen()
        utilities.print_orders_position_list_pretty()
    else:
        print("Error, please select an index from the list above")


def delete_product():
    utilities.clear_screen()
    while True:
        utilities.print_product_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index = int(
                input(f"\n Please input index of the product to be deleted: "))
            available_products = utilities.get_list_of_product_keys_from_db()
            if utilities.show_error_if_index_not_in_option_list(modified_dict_index, available_products):
                return
            confirmation = input(
                f"Are you sure you want to delete this product? Please note products that are currently active in orders cannot be deleted. Please select Y to confirm: ")
            if confirmation == "y":
                sql = "DELETE FROM product WHERE product_id=%s"
                val = (str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            else:
                connection.commit()
                sql_utilities.close_db(cursor, connection)
                break
        except Exception as e:
            print(f"Failed to open product database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_product_position_list_pretty()


def delete_courier():
    utilities.clear_screen()
    while True:
        utilities.print_courier_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index = int(
                input(f"\n Please input index of the courier to be deleted: "))
            available_products = utilities.get_list_of_courier_keys_from_db()
            if utilities.show_error_if_index_not_in_option_list(modified_dict_index, available_products):
                return
            confirmation = input(
                f"Are you sure you want to delete this courier? Please note couriers that are currently active in orders cannot be deleted. Please select Y to confirm: ")
            if confirmation == "y":
                sql = "DELETE FROM courier WHERE courier_id=%s"
                val = (str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            else:
                connection.commit()
                sql_utilities.close_db(cursor, connection)
                break
        except Exception as e:
            print(f"Failed to open courier database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_courier_position_list_pretty()


def delete_customer():
    utilities.clear_screen()
    while True:
        utilities.print_customer_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index = int(
                input(f"\n Please input index of the customer to be deleted: "))
            available_products = utilities.get_list_of_customer_keys_from_db()
            if utilities.show_error_if_index_not_in_option_list(modified_dict_index, available_products):
                return
            confirmation = input(
                f"Are you sure you want to delete this customer? Please note customers that are currently active in orders cannot be deleted. Please select Y to confirm: ")
            if confirmation == "y":
                sql = "DELETE FROM customer WHERE customer_id=%s"
                val = (str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            else:
                connection.commit()
                sql_utilities.close_db(cursor, connection)
                break
        except Exception as e:
            print(f"Failed to open customer database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_customer_position_list_pretty()


def delete_order():
    utilities.clear_screen()
    while True:
        utilities.print_orders_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index = int(
                input(f"\n Please input index of the order to be deleted: "))
            confirmation = input(
                f"Are you sure you want to delete this order? Please select Y to confirm: ")
            if confirmation == "y":
                sql2 = "DELETE FROM order_items WHERE order_id=%s"
                val = (str(modified_dict_index))
                cursor.execute(sql2, val)
                sql = "DELETE FROM ordeer WHERE order_id=%s"
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            else:
                connection.commit()
                sql_utilities.close_db(cursor, connection)
                break
        except Exception as e:
            print(f"Failed to open order database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_customer_position_list_pretty()