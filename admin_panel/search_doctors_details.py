import helper
import os
import csv

def search_doctors_details():

    print("Search Doctor Details By Doctor ID")

    doctor_id = helper.get_input_string("Enter Doctor ID : ")

    found = False

    file_path = "data/doctors_details.csv"

    file_exist = os.path.exists(file_path)


    if not file_exist:
        print(f"file not found {file_path}")
        return
    


    with open(file_path, mode="r" , newline="") as file:

        reader = csv.DictReader(file)


        for row in reader:

            if row['doctor_id'] == doctor_id:

                found = True

                print(f"Doctor ID : {row['doctor_id']}")
                print(f"User ID : {row['user_id']}")
                print(f"Doctor Name : {row['doctor_name']}")
                print(f"Doctor Specilization : {row['doctor_specilization']}")
                print(f"Doctor Phone Number : {row['doctor_phone_number']}")
                print(f"Doctor Email : {row['doctor_email']}")
                print(f"Doctor Qualification : {row['doctor_qualification']}")
                print(f"Doctor Experiance : {row['doctor_experiance']}")
                print(f"Doctor Consultation Fee : {row['consultation_fee']}")
                print(f"Doctor Duty Timing  : {row['duty_timing']}")
                print(f"Doctor status : {row['status']}")
                break

        if not found:
            print("Doctor ID Not found")
