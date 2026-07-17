import csv
import os
import helper


def cancel_appointment():

    print("-------------Cancel Patient Appointment By Appointment ID -------------------")


    appointment_id = helper.get_input_string("Enter Appointment ID : ")


    file_path = "data/appointment_details.csv"

    file_exist = os.path.exists(file_path)

    appointment_found = False

    appointment_status = "Cancelled"

    rows = []

    if not file_exist:
        print("Data Not Found or Invalid ID")
        return
    

    with open(file_path , mode="r", newline="") as file:

        reader = csv.DictReader(file)
        header = reader.fieldnames

        for row in reader:

            if row['appointment_id'] == appointment_id:

                appointment_found = True

                if row['appointment_status'] == "Cancelled":
                
                    print("Appointment is already cancelled.")
                    return
                
                if row['appointment_status'] == "Completed":

                    print("Completed appointments cannot be cancelled.")
                    return
                
                row['appointment_status'] = appointment_status

            rows.append(row)


    if not appointment_found:
        print("Appointment Not Found")
        return
    
    with open(file_path , mode="w" ,  newline="") as file:

        writer = csv.DictWriter(file , fieldnames=header)

        writer.writeheader()
        writer.writerows(rows)

    print("Appointment Status has been updated")