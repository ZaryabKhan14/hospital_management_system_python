import csv
import helper
import os

def delete_patient():

    print("----------------Delete Patient By ID--------------")


    patient_id = helper.get_input_string("Enter Patient ID : ")

    found = False

    file_path = "data/patient.csv"

    file_exist = os.path.exists(file_path)

    if not file_exist:
        print("file not found")
        return
    
    current_file = file_path

    temporary_file = "data/temp_patient.csv"


    with open(file_path, mode="r" , newline="") as file , \
        open(temporary_file, mode="w", newline="") as temp_file:

        reader = csv.DictReader(file)

        writer = csv.DictWriter(temp_file,fieldnames=reader.fieldnames)

        writer.writeheader()

        for row in reader:

            if row['Patient ID'] == patient_id:

                found = True
                continue

            writer.writerow(row)


        if not found:
            os.remove(temporary_file)
            print("please enter a valid id")

        else:
            os.replace(temporary_file,current_file)
            print("Patient Deleted Successfully")
