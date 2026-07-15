import helper
import csv
import os

def add_patient():



    patient_full_name = helper.get_input_string("Patient Full Name: ")
    patient_age = helper.get_input_integer("Patient Age: ")
    patient_gender = helper.get_input_string("Patient Gender: ")
    patient_phone_number = helper.get_input_string("Patient Phone Number: ")
    patient_cnic = helper.get_input_string("Patient CNIC (Optional): ")
    patient_address = helper.get_input_string("Patient Address: ")
    patient_blood_group = helper.get_input_string("Patient Blood Group: ")
    patient_emergency_contact = helper.get_input_string("Emergency Contact Number: ")

    headers = [
        "Patient ID",
        "Patient Full Name",
        "Patient Age",
        "Patient Gender",
        "Patient Phone Number",
        "Patient CNIC",
        "Patient Address",
        "Patient Blood Group",
        "Patient Emergency Contact"
    ]



    file_name = "data/patient.csv"
    file_exist = os.path.exists(file_name)

    if not file_exist:
        patient_id = 1
    else:
        with open(file_name, mode="r", newline="", encoding="utf-8") as file:
            rows = list(csv.reader(file))

            if len(rows) <= 1: 
                patient_id = 1
            else:
                patient_id = int(rows[-1][0]) + 1

    print(f"Patient ID: {patient_id}")
   
    add_data = [
        [patient_id,patient_full_name,patient_age,patient_gender,patient_phone_number,patient_cnic,patient_address,patient_blood_group,patient_emergency_contact]
    ]

    with open(file_name, mode="a", newline="", encoding="utf-8") as file:
        file_writer = csv.writer(file)

        if not file_exist:
            file_writer.writerow(headers)

        file_writer.writerows(add_data)

    print(f"Data has been successfully added to: {file_name}")