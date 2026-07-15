import helper
import csv


def search_user():

    print("Search User by ID ")


    user_id = helper.get_input_string("Enter User ID : ")
    
    found = False


    with open("data/login_credential.csv", mode="r", newline="") as file:
        read_file = csv.DictReader(file)


        for row in read_file:

            if (row['User_id'] == user_id):

                found = True
                print(f"User ID : {row['User_id']}")
                print(f"User Name : {row["username"]}")
                print(f"User Password : {row["password"]}")
                print(f"User Role : {row["role"]}")
                print("-" * 50)

    if not found:
        print("Please enter a valid Patient ID.")