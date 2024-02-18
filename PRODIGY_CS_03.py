from termcolor import colored

def check_password_complexity(password):

    length_requirement = len(password) >= 12
    uppercase_requirement = any(char.isupper() for char in password)
    lowercase_requirement = any(char.islower() for char in password)
    digit_requirement = any(char.isdigit() for char in password)
    special_char_requirement = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password)

    
    print("Password Length: " + colored("OK", "green") if length_requirement else colored("Too short", "red"))
    print("Uppercase Letter: " + colored("OK", "green") if uppercase_requirement else colored("Missing", "red"))
    print("Lowercase Letter: " + colored("OK", "green") if lowercase_requirement else colored("Missing", "red"))
    print("Digit: " + colored("OK", "green") if digit_requirement else colored("Missing", "red"))
    print("Special Character: " + colored("OK", "green") if special_char_requirement else colored("Missing", "red"))

    
    if all([length_requirement, uppercase_requirement, lowercase_requirement, digit_requirement, special_char_requirement]):
        print(colored("Password meets complexity requirements.", "green"))
    else:
        print(colored("Password does not meet complexity requirements.", "red"))


password_to_check = "SecureP@ssw0rd"
check_password_complexity(password_to_check)
