import utilities

def add_to_db(sub_menu_item): #products and courier in db
    utilities.clear_screen()
    if sub_menu_item == "Product":
        while True:
            new_item_name=input(f"Please type new {sub_menu_item.lower()} name: \n").title()
            new_item_price=float(input(f"Please type new {sub_menu_item.lower()} price in GBP: \n"))
            new_item_quantity=int(input(f"Please type new {sub_menu_item.lower()} quantity: \n"))
            try:
                connection = utilities.connect_to_sql()
                cursor=connection.cursor()
                cursor.execute("INSERT INTO product (product_name, product_price, product_quantity) VALUES (%s, %s, %s)",
                    (str(new_item_name), str(new_item_price), str(new_item_quantity)))
                connection.commit()
                utilities.close_db(connection, cursor)
            except:
                print("Failed to open product database table") 
            break
        utilities.clear_screen()
        utilities.print_product_position_list_pretty()     
    elif sub_menu_item == "Courier":
        while True:
            new_item_name=input(f"Please type new {sub_menu_item.lower()} name: \n").title()
            new_item_phone=input(f"Please type new {sub_menu_item.lower()} phone: \n")
            try:
                connection = utilities.connect_to_sql()
                cursor=connection.cursor()
                cursor.execute("INSERT INTO courier (courier_name, courier_phone) VALUES (%s, %s)",
                    (str(new_item_name), str(new_item_phone)))
                connection.commit()
                utilities.close_db(connection, cursor)
            except:
                print("Failed to open courier database table") 
            break
        utilities.clear_screen()
        utilities.print_courier_position_list_pretty()

def add_item(sub_menu_item, list1):    # for orders in csv
        while True:
            new_customer_name=input(f"Please type new {sub_menu_item.lower()} cutomer name: \n").title()
            new_customer_address=input(f"Please type new {sub_menu_item.lower()} customer address: \n").title()
            new_customer_phone=input(f"Please type new {sub_menu_item.lower()} customer phone: \n")
            utilities.print_courier_position_list_pretty() 
            new_courier=input("\n Please input index of courier chosen for this order: ")
            status_list=["PLACED", "PREPARING", "BEING DELIVERED", "DELIVERED", "CANCELLED"]
            utilities.print_position_list(status_list) 
            new_status_index=int(input(f"\n Please type index of order status: \n").upper())
            new_status_value=status_list[new_status_index]
            utilities.print_product_position_list_pretty() 
            new_items=input(f"Please type index of products to be added to order. To add more than one item, please separate indices with a space: \n")
            new_items_list=utilities.transform_inputs_into_list(new_items)
            utilities.update_db_quantities(new_items_list)
            new_dict={"customer_name": new_customer_name, "customer_address": new_customer_address, "customer_phone":new_customer_phone, "courier":new_courier, "status":new_status_value, "items":new_items}
            list1.append(new_dict)
            utilities.clear_screen()
            utilities.print_orders_position_list_pretty(list1)
            break

def update_product():
    utilities.clear_screen()
    while True:
        utilities.print_product_position_list_pretty() 
        try:
            connection = utilities.connect_to_sql()
            cursor=connection.cursor()
            modified_dict_index=int(input(f"\n Please input index of the product to be modified: "))
            sql=('SELECT * FROM product WHERE product_id = %s')
            val=(str(modified_dict_index))
            cursor.execute(sql,val)
            rows = cursor.fetchall()
            for row in rows:
                print(f'1 - Product Name: {row[1]}\n2 - Product Price: {row[2]}\n3 - Product Quantity: {row[3]}')
            modified_item_index=int(input(f"\n Please input index of the category to be modified: \n"))
            if modified_item_index==1:
                modified_product_name=input(f"\n Please type in new product name: \n").title()
                sql="UPDATE product SET product_name=%s WHERE product_id=%s"
                val=(str(modified_product_name), str(modified_dict_index))
                cursor.execute(sql,val)
                connection.commit()
            elif modified_item_index ==2:
                modified_product_price=float(input(f"\n Please type in new product price: \n"))
                sql="UPDATE product set product_price=%s WHERE product_id=%s"
                val=(modified_product_price, str(modified_dict_index))
                cursor.execute(sql,val)
                connection.commit()
            elif modified_item_index ==3:
                modified_product_quantity=int(input(f"\n Please type in new product quantity: \n"))
                sql="UPDATE product set product_quantity=%s WHERE product_id=%s"
                val=(modified_product_quantity, str(modified_dict_index))
                cursor.execute(sql,val)
                connection.commit()
            utilities.close_db(connection, cursor)
        except:
            print("Failed to open product database table")
        break
    utilities.clear_screen()
    utilities.print_product_position_list_pretty() 

def update_courier():
    utilities.clear_screen()
    while True:
        utilities.print_courier_position_list_pretty() 
        try:
            connection = utilities.connect_to_sql()
            cursor=connection.cursor()
            modified_dict_index=int(input(f"\n Please input index of the courier to be modified: "))
            sql=('SELECT * FROM courier WHERE courier_id = %s')
            val=(str(modified_dict_index))
            cursor.execute(sql,val)
            rows = cursor.fetchall()
            for row in rows:
                print(f'1 - Courier Name: {row[1]}\n2 - Courier Phone Number: {row[2]}')
            modified_item_index=int(input(f"\n Please input index of the category to be modified: \n"))
            if modified_item_index==1:
                modified_courier_name=input(f"\n Please type in new courier name: \n").title()
                sql="UPDATE courier SET courier_name=%s WHERE courier_id=%s"
                val=(str(modified_courier_name), str(modified_dict_index))
                cursor.execute(sql,val)
                connection.commit()
            elif modified_item_index ==2:
                modified_courier_phone=float(input(f"\n Please type in new courier phone number: \n"))
                sql="UPDATE courier set courier_phone=%s WHERE courier_id=%s"
                val=(modified_courier_phone, str(modified_dict_index))
                cursor.execute(sql,val)
                connection.commit()
            utilities.close_db(connection, cursor)
        except:
            print("Failed to open courier database table")
        break
    utilities.clear_screen()
    utilities.print_courier_position_list_pretty()

def update_item(sub_menu_item, list):
    utilities.clear_screen()
    utilities.print_any_position_list_pretty(sub_menu_item, list)
    modified_dict_index=int(input(f"\n Please input index of the order to be modified: "))-1
    if modified_dict_index >=len(list):
        print("\n Error, number not available in list\n")
    else:
        utilities.print_dict(list[modified_dict_index])
        modified_item_index=int(input(f"Please input index of the category to be modified: \n"))-1
        if modified_item_index==5:
            dictionary = list[modified_dict_index]
            list_of_keys = utilities.get_list_of_dict_keys(dictionary)
            key_being_modified=list_of_keys[modified_item_index]
            previous_inp=dictionary[key_being_modified]
            previous_list=utilities.transform_inputs_into_list(previous_inp)
            utilities.cancel_previous_order_products(previous_list)
            modified_item_value=input(f"\n Please type in new list of products: \n").title()
            modified_item_value_list=utilities.transform_inputs_into_list(modified_item_value)
            utilities.update_db_quantities(modified_item_value_list)
            dictionary = list[modified_dict_index]
            list_of_keys = utilities.get_list_of_dict_keys(dictionary)
            key_being_modified=list_of_keys[modified_item_index]
            dictionary[key_being_modified]=modified_item_value
            utilities.clear_screen()
            utilities.print_any_position_list_pretty(sub_menu_item, list)
        else:
            modified_item_value=input(f"\n Please type in new value: \n").title()
            dictionary = list[modified_dict_index]
            list_of_keys = utilities.get_list_of_dict_keys(dictionary)
            key_being_modified=list_of_keys[modified_item_index]
            dictionary[key_being_modified]=modified_item_value
            utilities.clear_screen()
            utilities.print_any_position_list_pretty(sub_menu_item, list)              

def delete_item(sub_menu_item, list, position=None, confirmation=None):
    utilities.clear_screen()
    while True:
        utilities.print_any_position_list_pretty(sub_menu_item, list)
        if position is None:
            position=int(input(f"\n Please type position in the list of {sub_menu_item.lower()} to be deleted: "))-1
        if confirmation is None: 
            confirmation=input(f"Are you sure you want to delete {sub_menu_item.lower()} {position+1, list[position]}? Please select Y to confirm: ")
        utilities.clear_screen()
        if confirmation.upper()=="Y":
            list.pop(position)
            utilities.print_any_position_list_pretty(sub_menu_item, list)
            break
        else:
            #print(f"Error, {sub_menu_item.lower()} already in list")
            break

def delete_product():
    utilities.clear_screen()
    while True:
        utilities.print_product_position_list_pretty() 
        try:
            connection = utilities.connect_to_sql()
            cursor=connection.cursor()
            modified_dict_index=int(input(f"\n Please input index of the product to be deleted: "))
            confirmation=input(f"Are you sure you want to delete this product? Please select Y to confirm: ")
            if confirmation =="y":
                sql="DELETE FROM product WHERE product_id=%s"
                val=(str(modified_dict_index))
                cursor.execute(sql,val)
                connection.commit()
                utilities.close_db(connection, cursor)
            else:
                connection.commit()
                utilities.close_db(connection, cursor)
                break
        except:
            print("Failed to open product database table")
        break
    utilities.clear_screen()
    utilities.print_product_position_list_pretty()

def delete_courier():
    utilities.clear_screen()
    while True:
        utilities.print_courier_position_list_pretty() 
        try:
            connection = utilities.connect_to_sql()
            cursor=connection.cursor()
            modified_dict_index=int(input(f"\n Please input index of the courier to be deleted: "))
            confirmation=input(f"Are you sure you want to delete this product? Please select Y to confirm: ")
            if confirmation =="y":
                sql="DELETE FROM courier WHERE courier_id=%s"
                val=(str(modified_dict_index))
                cursor.execute(sql,val)
                connection.commit()
                utilities.close_db(connection, cursor)
            else:
                connection.commit()
                utilities.close_db(connection, cursor)
                break
        except:
            print("Failed to open courier database table")
        break
    utilities.clear_screen()
    utilities.print_courier_position_list_pretty()

def update_order_status(sub_menu_item, my_list):
    utilities.clear_screen()
    while True:
        utilities.print_orders_position_list_pretty(my_list)
        modified_dict_index=int(input(f"\n Please input index of the {sub_menu_item.lower()} for which status is to be modified: "))-1
        if modified_dict_index >=len(my_list):
            print("\n Error, number not available in list\n")
        else:
            status_list=["PLACED", "PREPARING", "BEING DELIVERED", "DELIVERED", "CANCELLED"]
            utilities.print_position_list(status_list) 
            modified_item_index=int(input(f"\n Please input index of new status: \n"))-1
            modified_item_value=status_list[modified_item_index]
            dictionary = my_list[modified_dict_index]
            dictionary["status"]=modified_item_value
            utilities.clear_screen()
            utilities.print_orders_position_list_pretty(my_list)
            break 

