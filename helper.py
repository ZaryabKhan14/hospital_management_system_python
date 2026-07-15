def get_input_integer(message):
    while True:
        try:
            return int(input(message))
        
        except ValueError:
            print("Please enter a valid integer.")


def get_input_float(message):
    while True:
        
        try:
            return float(input(message))
    
        except ValueError:
            print("Please enter a valid float.")


def get_input_string(message):
    while True:
        
        string_value = input(message.strip())
        if string_value != "":
            return string_value
        
        else:
            print("Strint cant be empty.")



def get_input_choice(message,choice):
    while True:
        value = int(input(message))

        if value in choice:
            return value
        

        else:
            print("invalid choice")