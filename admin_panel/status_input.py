import helper


def status_input():

    
    print("Doctor Status")
    print("1. Active")
    print("2. Inactive")
    print("3. On Leave")


    choice = helper.get_input_choice("Select Option " , [1,2,3])

    match choice:
        
        case 1:
            # status = "Active"
            return "Active"
            
        case 2:
            # status = "Inactive"
            return "Inactive"

        case 3:
            # status = "On Leave"
            return "On Leave"


    # return status   