import helper
import csv
import os

def view_all_patient():
    
    print("All Patient Details")


    with open("data/patient.csv",mode="r", newline="" ) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:

            print(f"Patient ID : {row["Patient ID"]}")
            print(f"Patient Full Name : {row["Patient Full Name"]}")
            print(f"Patient Age : {row["Patient Age"]}")
            print(f"Patient Gender : {row["Patient Gender"]}")
            print(f"Patient Phone Number : {row["Patient Phone Number"]}")
            print(f"Patient CNIC : {row["Patient CNIC"]}")
            print(f"Patient Address : {row["Patient Address"]}")
            print(f"Patient Blood Group : {row["Patient Blood Group"]}")
            print(f"Patient Emergency Contact : {row["Patient Emergency Contact"]}")
            print("-" * 50)
            

      