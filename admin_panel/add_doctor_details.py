import helper
import csv
import os

def add_doctor_details():

    print("Add Doctor Details")

    user_id = helper.get_input_string("Enter User Id : ")

    file_name = "data/login_credential.csv"

    file_exist = os.path.exists(file_name)

    file_name2 = "data/doctors_details.csv"

    file_exist2 = os.path.exists(file_name2)

    doctor_id = 1
                    
    header = ["doctor_id","user_id","doctor_name","doctor_specilization","doctor_phone_number","doctor_email","doctor__qualification","doctor_experiance"]

    found = False

    if not file_exist:
        print("Login credentials file not found.")
        return
    
    else:
        with open(file_name, mode="r" , newline="") as file:
            
            reader = csv.DictReader(file)

            for row in reader:

                if row['User_id'] == user_id and row["role"] == "Doctor":

                    print("User ID and Role verified successfully.")   
                    print("---------------------------------------")                 
                    found = True

                    doctor_name = helper.get_input_string("Enter Doctor Name : ")
                    doctor_specilization = helper.get_input_string("Enter Doctor Specilization : ")
                    doctor_phone_number = helper.get_input_string("Enter Doctor Phone Number : ")
                    doctor_email = helper.get_input_string("Enter Doctor Email : ")
                    doctor__qualification = helper.get_input_string("Enter Doctor Qualification : ")
                    doctor_experiance = helper.get_input_string("Enter Doctor Experiance : ")

                    break
            
            if not found:
                print("User ID not found or user is not a Doctor.")
                return
            

    if not file_exist2:
        doctor_id = 1
    else:
        with open(file_name2, mode="r" , newline="") as file_doctor:


            read = csv.DictReader(file_doctor)

            for row in read:

                if row["user_id"] == user_id:
                    print("Doctor already exists.")
                    return
                
                if int(row["doctor_id"]) >= doctor_id:
                    doctor_id = int(row["doctor_id"]) + 1

    print(f"Doctor ID: {doctor_id}")

    add_doctor_data = [doctor_id,user_id,doctor_name,doctor_specilization,doctor_phone_number,doctor_email,doctor__qualification,doctor_experiance]


    with open("data/doctors_details.csv", mode="a" , newline="") as csv_file:

        writer = csv.writer(csv_file)

        if not file_exist2:

            writer.writerow(header)

        writer.writerow(add_doctor_data)

        print(f"Data has been successfully added to: {file_name2}")

    
