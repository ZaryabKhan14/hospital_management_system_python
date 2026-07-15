import helper
import csv


def view_all_users():

    print("All User Details")

    with open("data/login_credential.csv", mode="r" , newline="") as read_file:
        read_data = csv.DictReader(read_file)


        for row in read_data:
            print(f"ID : {row["User_id"]}")
            print(f"User Name : {row["username"]}")
            print(f"Paassword : {row["password"]}")
            print(f"Role : {row["role"]}")
            print("-" * 50)
