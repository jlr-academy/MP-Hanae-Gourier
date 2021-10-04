import sys

product_list=[]
courier_list=[]

try:
    product_txt=open("Products.txt","r")
    for item in product_txt.readlines():
        product_list.append(item.strip())           
except FileNotFoundError as fnfe:
    print("Failed to open Products.txt")

try:
    couriers_txt=open("Couriers.txt","r")
    for item in couriers_txt.readlines():
        courier_list.append(item.strip())          
except FileNotFoundError as fnfe:
    print("Failed to open Couriers.txt")


def main_menu(): 
    while True:
        print(
        """\n                         <MAIN MENU>\n
        Please select from the following options:\n 
        0. Exit application
        1. Product menu options
        2. Courier menu options\n""")
        user_choice1=int(input())
        print(f"User has selected option {user_choice1}.\n")
        if user_choice1==0:
            save_and_exit()
        elif user_choice1==1:
            product_menu(product_list)
        elif user_choice1==2:
            couriers_menu(courier_list)
        else:
            print("User entry not recognised, programme will now exit")
            break

 
def product_menu(product_list):
    while True:
        print("""
            \n                         <PRODUCT MENU>\n
            Please select from the following options:\n 
            0. Return to main menu
            1. View product list
            2. Add product
            3. Update existing product
            4. Delete product\n
        """)
        user_choice2=int(input())
        print(f"User has selected option {user_choice2}.\n")
        if user_choice2==0:
            break
        elif user_choice2==1:
            print(product_list)
        elif user_choice2==2:
            add_product(product_list)
        elif user_choice2==3:
            amend_product(product_list)
        elif user_choice2==4:
            delete_product(product_list)
        else:
            print("User entry not recognised, programme will now go back to main menu")
            break


def couriers_menu(courier_list):
    while True:
        print("""
        \n                         <Courier MENU>\n
        Please select from the following options:\n 
        0. Return to main menu
        1. View courier list
        2. Add courier
        3. Update existing courier
        4. Delete courier\n
        """)
        user_choice2=int(input())
        print(f"User has selected option {user_choice2}.\n")
        if user_choice2==0:
            break
        elif user_choice2==1:
            print(courier_list)
        elif user_choice2==2:
            add_courier(courier_list)
        elif user_choice2==3:
            amend_courier(courier_list)
        elif user_choice2==4:
            delete_courier(courier_list)
        else:
            print("User entry not recognised, programme will now go back to main menu")
            break


def save_and_exit(): #split into two functions as at the moment does two things - put reading and saving functions in a separate module
    try:
        with open("Products.txt", "w") as products_file:
            for product in product_list:
                products_file.write(product+"\n")
    except:
        print("Error, could not save product list")
    try:
        with open("Couriers.txt", "w") as couriers_file:
            for courier in courier_list:
                couriers_file.write(courier+"\n")
    except:
        print("Error, could not save courier list")
    sys.exit() #split out

    
def add_product(product_list):  
    while True:
        print("Please type new product name")
        new_product=input().title()
        if check_duplicate(product_list, new_product):
            print("Error, product already in list")
            break
        else:
            product_list.append(new_product)
            print(product_list)
            break


def add_courier(courier_list):
    while True:
        print("Please type new courier name")
        new_courier=input().title()
        if check_duplicate(courier_list, new_courier):
            print("Error, courier already in list")
            break
        else:
            courier_list.append(new_courier)
            print(courier_list)
            break

        
def check_duplicate(list, item):
    if item.lower() in (x.lower() for x in list):
        return True


def position_list(list):
    for (num, item) in enumerate(list):
        print(num+1, item)
        

def amend_product(product_list):
    while True:
        position_list(product_list)
        print("\n Please type position in the product list of product to be modified")
        position=int(input())-1
        if position >=len(product_list):
            print("\n Error, number not available in list\n")
        else:
            print("\n Please type new product name for the chosen position")
            modified_product=input()
            print("\n")
            if check_duplicate(product_list, modified_product):
                print("Error, product already in list")
                break
            else:
                product_list[position]=modified_product
                position_list(product_list)
                break


def amend_courier(courier_list):
    while True:
        position_list(courier_list)
        print("\n Please type position in the courier list of courier to be modified")
        position=int(input())-1
        if position >=len(courier_list):
            print("\n Error, number not available in list\n")
        else:
            print("\n Please type new courier name for the chosen position")
            modified_courier=input()
            print("\n")
            if check_duplicate(courier_list,modified_courier):
                print("Error, product already in list")
                break
            else:
                courier_list[position]=modified_courier
                position_list(courier_list)
                break


def delete_product(product_list):
    while True:
        position_list(product_list)
        print("\n Please type position in the product list of item to be deleted")
        position=int(input())-1
        print(f"Are you sure you want to delete item {position+1, product_list[position]}? Please select Y to confirm") 
        confirmation=input()
        print("\n")
        if confirmation.upper()=="Y":
            product_list.pop(position)
            position_list(product_list)
            break
        else:
            print("Error, product already in list")
            break


def delete_courier(courier_list):
    while True:
        position_list(courier_list)
        print("\n Please type position in the courier list of item to be deleted")
        position=int(input())-1
        print(f"Are you sure you want to delete item {position+1, courier_list[position]}? Please select Y to confirm") 
        confirmation=input()
        print("\n")
        if confirmation.upper()=="Y":
            courier_list.pop(position)
            position_list(courier_list)
            break
        else:
            print("Error, courier already in list")
            break


main_menu()    

#amended product needs to be given capitals