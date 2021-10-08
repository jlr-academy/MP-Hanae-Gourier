from os import system

def import_file(product_list, courier_list):
    read_txt_files(product_list, "data\products.txt")
    read_txt_files(courier_list, "data\couriers.txt")

def read_txt_files(my_list, file_name): #WIP
    try:
        file_txt=open(file_name) #removed r as is default
        for item in file_txt.readlines():
            my_list.append(item.strip())          
    except FileNotFoundError:
        print("Failed to open txt file") #why is this working? pass empty list if file not found

def save_lists(product_list, courier_list): 
    exporting_list(product_list, "products.txt")
    exporting_list(courier_list, "couriers.txt")
    
def exporting_list(my_list, file_name):
    try:
        with open(file_name, "w") as file:
            for item in my_list:
                file.write(item+"\n")
    except:
        print("Error, could not save list")

def check_duplicate(my_list, item):
    if item.lower() in (x.lower() for x in my_list):
        return True
    return False

def clear_screen():
    system("cls")

def print_dict(dict):
    print("\n")
    num=1
    for key, value in dict.items():
        print(num, key, ":", value)
        num+=1
    print("\n")

def print_position_list(my_list):
    print("\n")
    num=1
    for item in my_list:
        print(num,"-", item)
        num+=1