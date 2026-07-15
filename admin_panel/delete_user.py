import csv
import os
import helper


def delete_user():
    print("-------------Delete User By ID-----------------")



    user_id = helper.get_input_string("Enter User ID : ")

    found = False

    file_path = "data/login_credential.csv"

    file_exist = os.path.exists(file_path)

    if  not file_exist:
        print("file not exist")
        return



    current_file = file_path
    temporary_file = "data/temp_login_credential.csv"

    with open(current_file, mode="r", newline="") as csv_file, \
         open(temporary_file, mode="w", newline="") as temp_file:
        
        reader = csv.DictReader(csv_file)
        writer = csv.DictWriter(temp_file,fieldnames=reader.fieldnames)

        writer.writeheader()

        for row in reader:

            if row["User_id"] == user_id:
                found = True
                continue

            writer.writerow(row)
       
    if not found:
        os.remove(temporary_file)
        print("please enter a valid id")

    else:
        os.replace(temporary_file,current_file)
        print("User Deleted Successfully")

        
        
