import helper
import os
import csv


def update_user():
    print("---------Update User Through ID-----------")

    user_id = helper.get_input_string("Enter User ID : ")

    found = False

    file_name = "data/login_credential.csv"

    file_exist = os.path.exists(file_name)

    if not file_exist:
        print("file not exist ")
        return

    rows = []

    with open("data/login_credential.csv", mode="r" , newline="") as csv_file:
        read_csv = csv.DictReader(csv_file)
        headers = read_csv.fieldnames


        for row in read_csv:

            if row["User_id"] == user_id:

                found = True

                user_name = helper.get_input_string("Enter User Name : ")
                user_password = helper.get_input_string("Enter User Passwrod : ")
                user_role = helper.get_input_string("Enter User Role : ")
                capitalize_user_role = user_role.capitalize()

                row["username"] = user_name
                row["password"] = user_password
                row["role"] = capitalize_user_role

            rows.append(row)

            if not found:
                print("User Not Found")
                return
            

            with open("data/login_credential.csv" , mode="w" , newline="") as write_file:
                wrtie = csv.DictWriter(write_file,fieldnames=headers)

                wrtie.writeheader()
                wrtie.writerows(rows)

        print("User Information Has Been Updated")




