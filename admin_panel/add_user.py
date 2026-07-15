import helper
import csv
import os



def add_user():

    username = helper.get_input_string("Enter username : ")
    password = helper.get_input_string("Enter user password : ")
    role = helper.get_input_string("Enter user role : ")
    role_capitalize_first_letter = role.capitalize()


    file_name = "data/login_credential.csv"

    header = ["User_id","username","password","role"]

    file_exist = os.path.exists(file_name)

    if not file_exist:
        user_id = 1

    else:

        with open("data/login_credential.csv" , mode="r" , newline="") as csv_file:

            rows = list(csv.reader(csv_file))

            if len(rows) <= 1:
                user_id = 1

            else:
                user_id = int(rows[-1][0]) + 1


    print(f"User ID: {user_id}")





    add_data = [[user_id,username,password,role_capitalize_first_letter]]

    with open("data/login_credential.csv", mode="a" , newline="") as file_write:
        write = csv.writer(file_write)


        if not file_exist:

            write.writerow(header)

        write.writerows(add_data)

        print(f"Data has been successfully added to: {file_name}")