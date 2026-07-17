import os
import csv


def view_all_appointments():

    print("------------- All Appointments Records -------------")

    file_path = "data/appointment_details.csv"

    file_exist = os.path.exists(file_path)

    found = False

    if not file_exist:
        print(f"FIle Not found {file_path}")
        return
    

    with open(file_path, mode="r" , newline="") as file:

        reader = csv.DictReader(file)


        for row in reader:

            found = True

            print(f"Appointment ID : {row['appointment_id']}")
            print(f"Patient ID : {row['patient_id']}")
            print(f"Doctor ID : {row['doctor_id']}")
            print(f"Appointment Date : {row['appointment_date']}")
            print(f"Appointment Time : {row['appointment_time']}")
            print(f"Appointment Status : {row['appointment_status']}")
            print(f"Appointment Reason : {row['appointment_reason']}")
            print("-" * 30)


    if not found:
        print("Data Not Found")
