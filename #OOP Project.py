import re
import maskpass

print("----------Registration----------")
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
mobile_regex = re.compile(r"^020?[10,11,12]\d{8}")
pass_regex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
class Register:
    def signup(self):
        while True:
            first_name = input("First Name: ")
            if first_name.isalpha():
                break
            else:
                print("Invalid First Name")
        while True:
            last_name = input("Last Name: ")
            if last_name.isalpha():
                break
            else:
                print("Invalid last Name")
        while True:
            email = input("E-mail: ")
            if re.fullmatch(email_regex, email):
                break
            else:
                print("Invalid Email")
        while True:
            print("Your Password Must have: ")
            print("1- at least one number.")
            print("2- at least one uppercase and one lowercase character.")
            print("3- at least one special symbol.")
            print("4- be between 6 to 20 characters long.")
            print("------------------------------------------------------")
            password = maskpass.askpass()
            if pass_regex.match(password):
                break
            else:
                print("Invalid Password..!\nPlease Enter a Valid Password")
        while True:
            confirm_pass = maskpass.askpass(prompt= "Confirrm Password: ")
            if confirm_pass == password:
                break
            else:
                print("Doesn't Match with Password..!\nPlease, Reconfirm Your Password: ")
        while True:
            mobile_phone = input("Enter your phone number: ")
            if mobile_regex.match(mobile_phone):
                break
            else:
                print("Invalid Phone Number..!\nRe-Enter a valid number: ")
        print("Welcome", first_name, last_name, "..!")

registration = Register()
registration.signup()