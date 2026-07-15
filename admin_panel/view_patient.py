import csv
import os
import helper

def view_all_patients():

    print("_____________All Patient Details____________")

    file_path = "data/patient.csv"

    file_exist = os.path.exists(file_path)

    if not file_exist:
        print("file not found")
        return


    found = False

    with open(file_path, mode="r" , newline="") as csv_file:

        reader = csv.DictReader(csv_file)

        

        for row in reader:
            
            found = True

            print(f"Paitent id : {row['Patient ID']}")
            print(f"Patient Full Name : {row['Patient Full Name']}")
            print(f"Patient Age : {row['Patient Age']}")
            print(f"Patient Gender : {row['Patient Gender']}")
            print(f"Patient Phone Number : {row['Patient Phone Number']}")
            print(f"Patient CNIC : {row['Patient CNIC']}")
            print(f"Patient Address : {row['Patient Address']}")
            print(f"Patient Blood Group : {row['Patient Blood Group']}")
            print(f"Patient Emergency Contact : {row['Patient Emergency Contact']}")
            print("-" * 50)

            

    if not found:
        print("No patient records found.")