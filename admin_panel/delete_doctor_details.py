import csv
import os
import helper

def delete_doctor_details():

    print("Delete Doctor Details By ID")


    doctor_id = helper.get_input_string("Enter Doctor ID : ")

    found = False

    file_path = "data/doctors_details.csv"

    file_exist = os.path.exists(file_path)

    if not file_exist:
        print("File Not found")
        return
    


    current_file = file_path

    temporary_file = "data/temp_doctor_details.csv"


    with open(file_path, mode="r" , newline="") as file , \
        open(temporary_file, mode="w", newline="") as temp_file:

        reader = csv.DictReader(file)

        writer = csv.DictWriter(temp_file,fieldnames=reader.fieldnames)

        writer.writeheader()

        for row in reader:

            if row['doctor_id'] == doctor_id:

                found = True
                continue

            writer.writerow(row)


        if not found:
            os.remove(temporary_file)
            print("please enter a valid id")

        else:
            os.replace(temporary_file,current_file)
            print("Doctor Detail Deleted Successfully")