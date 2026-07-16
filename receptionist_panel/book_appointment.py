import csv
import helper
import os

def book_appointment():

    print("Add Appointment Details : ")

    patient_id = helper.get_input_string("Enter Patient ID : ")
    
    doctor_id = helper.get_input_string("Enter Doctor ID : ")

    file_path1 = "data/patient.csv"

    file_path2 = "data/doctors_details.csv"

    file_path3 = "data/appointment_details.csv"

    file_exist1 = os.path.exists(file_path1)

    file_exist2 = os.path.exists(file_path2)

    file_exist3 = os.path.exists(file_path3)

    doctor_found = False

    patient_found = False

    appointment_status = "Booked"

    appointment_id = 1

    headers = ['appointment_id','patient_id','doctor_id','appointment_date','appointment_time','appointment_status','appointment_reason']

    if not file_exist1:
        print(f"file not found : {file_path1}")
        return
    
    if not file_exist2:
        print(f"file not found : {file_path2}")
        return
        
    with open(file_path1, mode="r" , newline="") as file , \
        open(file_path2 , mode="r" , newline="") as file2 :
        
        reader = csv.DictReader(file)
        reader2 = csv.DictReader(file2)

        for row in reader:

            if row['Patient ID'] == patient_id:

                patient_found = True

                print("Patient ID Match")
                break
            
        if not patient_found:

            print("Patient ID not found")
            return
        
        for row in reader2:

            if row['doctor_id'] == doctor_id:

                doctor_found = True      
                
                if row['status'] != "Active":
                    print("Doctor is not available for appointments.")
                    return
                
                doctor_availability = row["availability"]
                doctor_duty_timing = row["duty_timing"]

                
                print("Doctor ID Match")
                break
            
        if not doctor_found:

                print("Doctor ID not found")
                return
        
    appointment_date = helper.get_input_date("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = helper.get_input_time("Enter Appointment Time (HH:MM): ")
    appointment_reason = helper.get_input_string("Enter Appointment reason : ")

    #day check kar rhe hain doctor ka konse din available hai
    # appointment_day = datetime.strptime(
    # appointment_date,
    # "%Y-%m-%d"
    # ).strftime("%A")

    # available_days = [day.strip() for day in doctor_availability.split(",")]

    # if appointment_day not in available_days:
    #     print(f"Doctor is not available on {appointment_day}.")
    #     return
    
#ismai doctor ki timing check kar rhe hain
    # start_time, end_time = doctor_duty_timing.split("-")

    # appointment = datetime.strptime(appointment_time, "%H:%M").time()
    # start = datetime.strptime(start_time.strip(), "%H:%M").time()
    # end = datetime.strptime(end_time.strip(), "%H:%M").time()

    # if appointment < start or appointment > end:
    #     print("Appointment time is outside doctor's duty timing.")
    #     return

    if not file_exist3:
            appointment_id = 1

    else:

        with open(file_path3, mode="r" , newline="") as file3:

            reader3 = csv.DictReader(file3)

            for row in  reader3:

                if row['patient_id'] == patient_id and row['doctor_id'] == doctor_id and row['appointment_time'] == appointment_time and row['appointment_date'] == appointment_date:

                    print("Appointment Already Exists")
                    return   

                if int(row["appointment_id"]) >= appointment_id:
                    appointment_id = int(row["appointment_id"]) + 1

    print(f"Appointment ID : {appointment_id}")

    add_appointment_data = [appointment_id,patient_id,doctor_id,appointment_date,appointment_time,appointment_status,appointment_reason]

    with open(file_path3 , mode="a" , newline="") as write_file:

        writer = csv.writer(write_file)

        if not file_exist3:

            writer.writerow(headers)

        writer.writerow(add_appointment_data)

        print(f"Data has been successfully added to: {file_path3}")
