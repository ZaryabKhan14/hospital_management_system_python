import os 
import csv
import helper


def reschedule_appointment():

    print("_____ Reschedule Appointment By Appointment ID _____")


    appointment_id = helper.get_input_string("Enter Appointment ID : ")

    file_path = "data/appointment_details.csv"

    file_exist = os.path.exists(file_path)

    appointment_found = False
    

    rows = []

    if not file_exist:
        print(f"File Not Found {file_path}")
        return
    

    with open(file_path, mode="r" , newline="") as file:

        reader = csv.DictReader(file)

        header = reader.fieldnames

        rows = list(reader)

        for row in rows:

            if row['appointment_id'] == appointment_id:

                status = row['appointment_status']


                doctor_id = row['doctor_id']
                print(f"doctor id : {doctor_id}")

                appointment_found = True

                if status == "Completed":
                    print("Appointment already Completed")
                    return
                
                elif status == "Cancelled":
                    print("Appointment already Cancelled")
                    return

                appointment_date = helper.get_input_date("Enter Appointment Date (YYYY-MM-DD): ")
                appointment_time = helper.get_input_time("Enter Appointment Time (HH:MM): ")
                break

        if not appointment_found:
                print("Appointment Not Found")
                return

        for row in rows:
            if row['doctor_id'] == doctor_id and row['appointment_time'] == appointment_time and row['appointment_date'] == appointment_date and row['appointment_id'] != appointment_id:

                print("Doctor already has another appointment at this date and time.")
                return        

        for row in rows:
                
            if row['appointment_id'] == appointment_id:

                if row['appointment_date'] == appointment_date and row['appointment_time'] == appointment_time:
                    print("Appointment is already scheduled at this date and time.")
                    return

                row['appointment_date'] = appointment_date
                row['appointment_time'] = appointment_time
                break

        # rows.append(row)

    with open(file_path, mode="w" , newline="") as file:

        writer = csv.DictWriter(file , fieldnames=header)

        writer.writeheader()
        writer.writerows(rows)

    print("Appointment Timing And Date has been updated")



        
    

