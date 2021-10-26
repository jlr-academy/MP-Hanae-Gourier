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
            new_item_quantity = float(new_item_quantity_input)
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
                sql_utilities.close_db(cursor, connection)
            except Exception as e:
                print(f"Failed to open customer database table. Error is: {e}")
            break
    utilities.clear_screen()
    utilities.print_customer_position_list_pretty()
    return new_customer_name, new_customer_address, new_customer_phone


def add_order(list1):
    while True:
        new_customer_name = None
        new_customer_address = None
        new_customer_phone = None
        utilities.select_customer()
        utilities.print_courier_position_list_pretty()
        new_courier = int(input(
            "\n Please input index of courier chosen for this order: "))
        available_couriers=utilities.get_list_of_courier_keys_from_db()
        if utilities.show_error_if_index_not_in_option_list(new_courier,available_couriers):
            return
        status_list = ["PLACED", "PREPARING","BEING DELIVERED", "DELIVERED"]
        utilities.print_position_list(status_list)
        new_status_index = int(
            input("\n Please type index of order status: \n").upper())
        new_status_value = status_list[new_status_index]
        utilities.print_product_position_list_pretty()
        new_items = input(
            "Please type index of products to be added to order. To add more than one item, please separate indices with a space: \n")
        new_items_list = utilities.transform_inputs_into_list(new_items)
        available_products_list=utilities.get_list_of_product_keys_from_db()
        #if utilities.show_error_if_indices_not_in_option_list(new_items_list,available_products_list)==True:
        utilities.update_db_quantities(new_items_list)
        new_dict = {"customer_name": new_customer_name, "customer_address": new_customer_address,
                    "customer_phone": new_customer_phone, "courier": new_courier, "status": new_status_value, "items": new_items}
        list1.append(new_dict)
        utilities.clear_screen()
        utilities.print_orders_position_list_pretty(list1)
        break


def update_product():
    utilities.clear_screen()
    while True:
        utilities.print_product_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index = int(input(f"\n Please input index of the product to be modified: "))
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
            modified_item_index = input(f"\n Please input index of the category to be modified: \n")
            if modified_item_index == 1:
                modified_product_name = input(
                    f"\n Please type in new product name: \n").title()
                sql = "UPDATE product SET product_name=%s WHERE product_id=%s"
                val = (str(modified_product_name), str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            elif modified_item_index == 2:
                modified_product_price = float(
                    input(f"\n Please type in new product price: \n"))
                sql = "UPDATE product set product_price=%s WHERE product_id=%s"
                val = (modified_product_price, str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
                sql_utilities.close_db(cursor, connection)
            elif modified_item_index == 3:
                modified_product_quantity = int(
                    input(f"\n Please type in new product quantity: \n"))
                sql = "UPDATE product set product_quantity=%s WHERE product_id=%s"
                val = (modified_product_quantity, str(modified_dict_index))
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
            modified_dict_index = int(
                input(f"\n Please input index of the courier to be modified: "))
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
            elif modified_item_index == 2:
                modified_courier_phone = float(
                    input(f"\n Please type in new courier phone number: \n"))
                sql = "UPDATE courier set courier_phone=%s WHERE courier_id=%s"
                val = (modified_courier_phone, str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
            sql_utilities.close_db(cursor, connection)
        except Exception as e:
            print(f"Failed to open courier database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_courier_position_list_pretty()


def update_customer():
    utilities.clear_screen()
    while True:
        utilities.print_customer_position_list_pretty()
        try:
            connection = sql_utilities.connect_to_db()
            cursor = connection.cursor()
            modified_dict_index = int(
                input(f"\n Please input index of the customer to be modified: "))
            sql = ('SELECT * FROM customer WHERE customer_id = %s')
            val = (str(modified_dict_index))
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
                val = (str(modified_customer_name), str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
            elif modified_item_index == 2:
                modified_customer_address = input(
                    f"\n Please type in new customer address: \n")
                sql = "UPDATE customer set customer_address=%s WHERE customer_id=%s"
                val = (str(modified_customer_address), str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
            elif modified_item_index == 3:
                modified_customer_phone = float(
                    input(f"\n Please type in new customer phone number: \n"))
                sql = "UPDATE customer set customer_phone=%s WHERE customer_id=%s"
                val = (modified_customer_phone, str(modified_dict_index))
                cursor.execute(sql, val)
                connection.commit()
            sql_utilities.close_db(cursor, connection)
        except Exception as e:
            print(f"Failed to open customer database table. Error is: {e}")
        break
    utilities.clear_screen()
    utilities.print_customer_position_list_pretty()


def update_order_status(sub_menu_item, my_list):
    utilities.clear_screen()
    while True:
        utilities.print_orders_position_list_pretty(my_list)
        modified_dict_index = int(input(
            f"\n Please input index of the {sub_menu_item.lower()} for which status is to be modified: "))-1
        if modified_dict_index >= len(my_list):
            print("\n Error, index not available in list\n")
        else:
            status_list = ["PLACED", "PREPARING","BEING DELIVERED", "DELIVERED"]
            utilities.print_position_list(status_list)
            modified_item_index = int(
                input('\n Please input index of new status: \n')) - 1
            modified_item_value = status_list[modified_item_index]
            dictionary = my_list[modified_dict_index]
            dictionary["status"] = modified_item_value
            utilities.clear_screen()
            utilities.print_orders_position_list_pretty(my_list)
            break


def update_order(sub_menu_item, list):
    utilities.clear_screen()
    utilities.print_any_position_list_pretty(sub_menu_item, list)
    modified_dict_index = int(
        input(f"\n Please input index of the order to be modified: "))-1
    if modified_dict_index >= len(list):
        print("\n Error, number not available in list\n")
    else:
        utilities.print_dict(list[modified_dict_index])
        modified_item_index = int(
            input(f"Please input index of the category to be modified: \n"))-1
        if modified_item_index == 5:
            dictionary = list[modified_dict_index]
            list_of_keys = utilities.get_list_of_dict_keys(dictionary)
            key_being_modified = list_of_keys[modified_item_index]
            previous_inp = dictionary[key_being_modified]
            previous_list = utilities.transform_inputs_into_list(previous_inp)
            utilities.cancel_previous_order_products(previous_list)
            utilities.print_product_position_list_pretty()
            modified_item_value = input(
                f"\n Please type in new indices of products ordered. Use a space to separate indices if ordering more than one product: \n").title()
            modified_item_value_list = utilities.transform_inputs_into_list(
                modified_item_value)
            utilities.update_db_quantities(modified_item_value_list)
            dictionary = list[modified_dict_index]
            list_of_keys = utilities.get_list_of_dict_keys(dictionary)
            key_being_modified = list_of_keys[modified_item_index]
            dictionary[key_being_modified] = modified_item_value
            utilities.clear_screen()
            utilities.print_any_position_list_pretty(sub_menu_item, list)
        elif modified_item_index == 3:
            utilities.print_courier_position_list_pretty()
            new_courier = input(
                f"\n Please type in new value: \n").title()
            available_couriers=utilities.get_list_of_courier_keys_from_db()
            if utilities.show_error_if_index_not_in_option_list(new_courier,available_couriers):
                return
            dictionary = list[modified_dict_index]
            list_of_keys = utilities.get_list_of_dict_keys(dictionary)
            key_being_modified = list_of_keys[modified_item_index]
            dictionary[key_being_modified] = new_courier
            utilities.clear_screen()
            utilities.print_any_position_list_pretty(sub_menu_item, list)
        else:
            modified_item_value = input(
                f"\n Please type in new value: \n").title()
            dictionary = list[modified_dict_index]
            list_of_keys = utilities.get_list_of_dict_keys(dictionary)
            key_being_modified = list_of_keys[modified_item_index]
            dictionary[key_being_modified] = modified_item_value
            utilities.clear_screen()
            utilities.print_any_position_list_pretty(sub_menu_item, list)


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
                f"Are you sure you want to delete this product? Please select Y to confirm: ")
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
            confirmation = input(
                f"Are you sure you want to delete this courier? Please select Y to confirm: ")
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
            confirmation = input(
                f"Are you sure you want to delete this customer? Please select Y to confirm: ")
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
                sql = "DELETE FROM ordeer WHERE order_id=%s"
                val = (str(modified_dict_index))
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