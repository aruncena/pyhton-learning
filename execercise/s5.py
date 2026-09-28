import os
dir_name = input("Enter the lit of dir:")

list_dir = dir_name.split(" ")

for dir in list_dir:
    if os.path.exists(dir):
        print(f"{dir} exists.")
    else:
        os.mkdir(dir)
        print(f"{dir} created.")