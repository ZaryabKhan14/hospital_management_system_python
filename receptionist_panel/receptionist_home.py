import helper
from receptionist_panel.add_patient import add_patient
from receptionist_panel.view_all_patient import view_all_patient
from receptionist_panel.search_patient import search_patient
from receptionist_panel.update_patient_information import update_patient_information

def receptionist_menu(role):

    while True:

        print("\n===== Receptionist Menu =====")
        print("1. Register New Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Update Patient Information")
        print("5. Book Appointment")
        print("6. View Appointments")
        print("7. Cancel Appointment")
        print("8. Assign Doctor")
        print("9. Admit Patient")
        print("10. Discharge Patient")
        print("11. Logout")

        option = helper.get_input_choice(
            "Enter your choice: ",
            [1,2,3,4,5,6,7,8,9,10,11]
        )

        match option:

            case 1:
                add_patient()

            case 2:
                view_all_patient()

            case 3:
                search_patient()

            case 4:
                update_patient_information()


            case 5:
                print("_____ Book Appointment _____")

            case 6:
                print("_____ View Appointments _____")

            case 7:
                print("_____ Cancel Appointment _____")

            case 8:
                print("_____ Assign Doctor _____")

            case 9:
                print("_____ Admit Patient _____")

            case 10:
                print("_____ Discharge Patient _____")

            case 11:
                print("Logging out...")
                break