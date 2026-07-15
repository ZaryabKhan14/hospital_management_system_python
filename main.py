import csv
import helper
from doctor_menu.doctor_home import  doctor_menu
from receptionist_panel.receptionist_home import  receptionist_menu
from admin_panel.admin_home import admin_home

print("-----------------Hosptal Management System----------------------")

attempt = 0

while attempt < 3:
    username = helper.get_input_string("enter username : ")
    password = helper.get_input_string("enter password : ")

    session = False


    with open('data/login_credential.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)


        for row in reader:
            if(row['username'] == username and row['password'] == password):

                role = row['role']
                # print(f"{username} login successfull")
                # print("welcome",row['role'])
                session = True  

                if row['role'] == "Doctor":
                    print(f"{username} login successfull")
                    print("welcome",row['role'])
                    print("Doctor menu")
                    doctor_menu()

                elif row['role'] == "Patient":
                    print(f"{username} login successfull")
                    print("welcome",row['role'])
                    print("patient menu")


                elif row['role'] == "Admin":
                    print(f"{username} login successfull")
                    print("welcome",row['role'])
                    print("Admin menu")
                    admin_home(role)
                    


                elif row['role'] == "Receptionist":
                    print(f"{username} login successfull")
                    print("welcome",row['role'])
                    print("Receptionist menu")
                    receptionist_menu(role)
                    print(role)

                else:
                    print("invalid error")

                break

            
        if session:
            break
        else:
            attempt += 1
            print(f"Invalid Username or Password!")
            print(f"Attempts Left: {3 - attempt}")

        if attempt == 3:
            print("Maximum login attempts reached. Access denied.")
                

