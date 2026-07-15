import csv
import helper
import os

def view_all_doctors():

    print("All Doctor Details")


    file_path = "data/doctors_details.csv"

    file_exist = os.path.exists(file_path)

    found = False

    if not file_exist:
        print("file not found")
        return

    with open(file_path, mode="r", newline="") as csv_file:

        reader = csv.DictReader(csv_file)


        for row in reader:


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
            print(f"Doctor Availability : {row['availability']}")
            print(f"Doctor Duty Timing : {row['duty_timing']}")
            print(f"Doctor Status : {row['status']}")
            print("-" * 30)

        if not found:
            print("Data not found")    

    