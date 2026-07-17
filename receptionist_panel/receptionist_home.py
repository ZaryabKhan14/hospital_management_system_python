import helper
from receptionist_panel.add_patient import add_patient
from receptionist_panel.view_all_patient import view_all_patient
from receptionist_panel.search_patient import search_patient
from receptionist_panel.update_patient_information import update_patient_information

from receptionist_panel.book_appointment import book_appointment
from receptionist_panel.view_appointment import view_all_appointments
from receptionist_panel.cancel_appointment import cancel_appointment
from receptionist_panel.reschedule_appointment import reschedule_appointment

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
        print("8. Reschedule Appointment")
        print("9. Search Appointment")
        print("10. Logout")

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

                book_appointment()

            case 6:
                print("_____ View Appointments _____")

                view_all_appointments()

            case 7:
                print("_____ Cancel Appointment _____")

                cancel_appointment()

            case 8:
                print("_____ Reschedule Appointment _____")

                reschedule_appointment()

            case 9:
                print("_____ Search Appointment _____")

            case 10:
                print("Logging out...")
                break