import csv
import os 
import helper
from admin_panel.status_input import status_input



def update_doctor_Details():


    print("Update Docotr Details By ID")


    user_id = helper.get_input_string("Enter User ID : ")

    file_path = "data/login_credential.csv"

    file_path2 = "data/doctors_details.csv"

    file_exist = os.path.exists(file_path)
    file_exist2 = os.path.exists(file_path2)

    user_id_found = False
    doctor_found = False

    rows = []

    if not file_exist:
        print(f"file not exist : {file_exist}")
        return
    
    else:

        with open(file_path , mode="r" , newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            

            for row in reader:

                if row['User_id'] == user_id and row['role'] == "Doctor":

                    print("User ID and User Role match")
                    user_id_found = True

                    doctor_name = helper.get_input_string("Enter Doctor Name : ")
                    doctor_specilization = helper.get_input_string("Enter Doctor Specilization : ")
                    doctor_phone_number = helper.get_input_string("Enter Doctor Phone Number : ")
                    doctor_email = helper.get_input_string("Enter Doctor Email : ")
                    doctor_qualification = helper.get_input_string("Enter Doctor Qualification : ")
                    doctor_experiance = helper.get_input_string("Enter Doctor Experiance : ")
                    consultation_fee = helper.get_input_string("Enter Doctor Consultation Fee : ")
                    availability = helper.get_input_string("Enter Doctor Availability : ")
                    duty_timing = helper.get_input_string("Enter Doctor Duty Timing : ")
                    status = status_input()

                    break


            if not user_id_found:
                print("User ID not found or user is not a Doctor.")
                return


    if not file_exist2:
        print(f"file not found {file_path2}")
        return
    
    else:
        
        with open(file_path2, mode= "r", newline="") as read_file:

            read = csv.DictReader(read_file)
            header = read.fieldnames

            for row in read:

                if row['user_id'] == user_id:

                    doctor_found = True

                    row['doctor_name'] = doctor_name
                    row['doctor_specilization'] = doctor_specilization
                    row['doctor_phone_number'] = doctor_phone_number
                    row['doctor_email'] = doctor_email
                    row['doctor_qualification'] = doctor_qualification
                    row['doctor_experiance'] = doctor_experiance
                    row['consultation_fee'] = consultation_fee
                    row['availability'] = availability
                    row['duty_timing'] = duty_timing
                    row['status'] = status

                rows.append(row)

            if not doctor_found:
                print("Doctor not found.")
                return

    

        with open(file_path2 , mode="w" , newline="") as update_file:
            write = csv.DictWriter(update_file,fieldnames=header)

            write.writeheader()
            write.writerows(rows)

    print("Doctor Information Has Been Updated")


 



    
