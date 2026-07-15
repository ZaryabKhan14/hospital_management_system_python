import helper

def doctor_menu():

    while True:

        print("===== Doctor Menu =====")
        print("1. View My Patients")
        print("2. Search patient")
        print("3. View Patient Details")
        print("4. Add Prescription")
        print("5. View Prescription History")
        print("6. Update Patient Diagnosis")
        print("7. View Today's Appointments")
        print("8. View Medical History")
        print("9. Logout")


        option = helper.get_input_choice("enter your choice : ",[1,2,3])

        match option:
           
            case 1:
                print("_____ View My Patients _____")
                break

            case 2:
                print("L_____ Search patient _______")
                break


            case 3:
                print("_____ View Patient Details _____")
                break

            case 4:
                print("_____ Add Prescription _____")
                break


            case 5:
                print("_____ View Prescription History _____")
                break

            case 6:
                print("_____ Update Patient Diagnosis _____")
                break


            case 7:
                print("_____ View Today's Appointments _____")
                break

            case 8:
                print("_____ View Medical History _____")
                break

            case 9:
                print("Logging out...")
                break

        