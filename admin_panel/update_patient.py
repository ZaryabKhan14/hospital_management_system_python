import os
import helper
import csv


def update_patient_information():

    print("Update Patient By ID")

    patient_id = helper.get_input_string("Enter Patient ID  : ")

    file_path = "data/patient.csv"

    file_exist = os.path.exists(file_path)

    if not file_exist:
        print("file not found")
        return
    
    found = False

    rows = []

    with open(file_path, mode="r" , newline="") as csv_file:

        reader = csv.DictReader(csv_file)
        headers = reader.fieldnames

        for row in reader:

            if row['Patient ID'] == patient_id:

                found = True

                patient_full_name = helper.get_input_string("Patient Full Name: ")
                patient_age = helper.get_input_integer("Patient Age: ")
                patient_gender = helper.get_input_string("Patient Gender: ")
                patient_phone_number = helper.get_input_string("Patient Phone Number: ")
                patient_cnic = helper.get_input_string("Patient CNIC (Optional): ")
                patient_address = helper.get_input_string("Patient Address: ")
                patient_blood_group = helper.get_input_string("Patient Blood Group: ")
                patient_emergency_contact = helper.get_input_string("Emergency Contact Number: ")


                row['Patient Full Name'] = patient_full_name
                row['Patient Age'] = patient_age
                row['Patient Gender']  = patient_gender
                row['Patient Phone Number']  = patient_phone_number
                row['Patient CNIC']  = patient_cnic
                row['Patient Address']  = patient_address
                row['Patient Blood Group']  = patient_blood_group
                row['Patient Emergency Contact']  = patient_emergency_contact

            rows.append(row)


        if not found:
            print("Enter Valid ID")
            return
        

        with open(file_path,mode="w",newline="") as file:

            writer = csv.DictWriter(file,fieldnames=headers)

            writer.writeheader()
            writer.writerows(rows)

        print("Patient Data Has been Updated")
