from datetime import datetime

def get_input_date(message):

    while True:

        date = input(message).strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

def get_input_time(message):

    while True:

        time = input(message).strip()

        try:
            datetime.strptime(time, "%H:%M")
            return time

        except ValueError:
            print("Invalid time. Please use HH:MM (24-hour format).")

            

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