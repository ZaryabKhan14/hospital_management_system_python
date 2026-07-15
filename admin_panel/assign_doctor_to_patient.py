import csv
import helper
import os

def assign_doctor_to_patient():

    print("Assign Doctor To Patient")

    file_path = "data/login_credential.csv"
    file_path2 = "data/patient.csv"

    file_exist = os.path.exists(file_path)
    file_exist2 = os.path.exists(file_path2)

    if not file_exist:
        print("login credential not found")
        return
    
    if not file_exist2:
        print("patient.csv not found")
        return
    
    