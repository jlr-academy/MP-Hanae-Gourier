def import_file(product_list, courier_list):
    read_txt_files(product_list, "Products.txt")
    read_txt_files(courier_list, "Couriers.txt")

def read_txt_files(list, file_name):
    try:
        file_txt=open(file_name,"r")
        for item in file_txt.readlines():
            list.append(item.strip())          
    except FileNotFoundError as fnfe:
        print("Failed to open txt file")

def save_lists(product_list, courier_list): 
    exporting_list(product_list, "Products.txt")
    exporting_list(courier_list, "Couriers.txt")

def exporting_list(list, file_name):
    try:
        with open(file_name, "w") as file:
            for item in list:
                file.write(item+"\n")
    except:
        print("Error, could not save list")

def check_duplicate(list, item):
    if item.lower() in (x.lower() for x in list):
        return True

def position_list(list):
    for (num, item) in enumerate(list):
        print(num+1, item)
