import helper
from admin_panel.add_user import add_user
from admin_panel.view_user import view_all_users 
from admin_panel.search_user import search_user
from admin_panel.update_user import update_user
from admin_panel.delete_user import delete_user
from admin_panel.view_patient import view_all_patients
from admin_panel.search_patient import search_patient
from admin_panel.update_patient import update_patient_information
from admin_panel.delete_patient import delete_patient
from admin_panel.view_doctors import view_all_doctors
from admin_panel.add_doctor_details import add_doctor_details

def admin_home(role):



    while True:

        print("\n===== Admin Menu =====")
        print("1. Add User")
        print("2. View All User")
        print("3. Search User")
        print("4. Update User")
        print("5. Delete User")
        print("6. View All Patient")
        print("7. Search Patient")
        print("8. Update Patient Information")
        print("9. Delete Patient")
        print("10. Add Doctors Details")
        print("11. View All Doctors")
        print("12. Assign Doctor to Patient")
        print("13. View All Appointments")
        print("14. Cancel Appointment")
        print("15. Logout")


        choice = helper.get_input_choice(
                    "Enter your choice: ",
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                )
        
        match choice:

            case 1:
                print("_____ Add User _____")
                add_user()

            case 2:
                print("_____ View All Users _____")
                view_all_users()

            case 3:
                print("_____ Search User _____")
                search_user()

            case 4:
                print("_____ Update User _____")
                update_user()

            case 5:
                print("_____ Delete User _____")
                delete_user()

            case 6:
                print("_____ View All Patients _____")
                view_all_patients()

            case 7:
                print("_____ Search Patient _____")
                search_patient()

            case 8:
                print("_____ Update Patient Information _____")
                update_patient_information()

            case 9:
                print("_____ Delete Patient _____")
                delete_patient()


            case 10:
                print("_____ Add Doctors Details _____")
                add_doctor_details()

            case 11:
                print("_____ View All Doctors _____")
                view_all_doctors()

            case 12:
                print("_____ Assign Doctor to Patient _____")
                # assign_doctor_to_patient()

            case 13:
                print("_____ View All Appointments _____")
                # view_all_appointments()

            case 14:
                print("_____ Cancel Appointment _____")
                # cancel_appointment()

            case 15:
                print("Logging out...")
                break


