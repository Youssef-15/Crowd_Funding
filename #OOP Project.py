import re
import maskpass

print("----------Registration----------")
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
mobile_regexEg = re.compile(r"^[010,011,012]\d{8}")
mobile_regexEn = re.compile(r"^[01]\d{15}")
mobile_regexUS = re.compile(r"^\d{10}")
mobile_regexSp = re.compile(r"^[6,7]\d{8}")
mobile_regexIt = re.compile(r"^[3]\d{9}")
pass_regex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
class Register:
    def signup(self):
        #First and last name
        while True:
            first_name = input("First Name: ")
            if first_name.isalpha():
                file1 = open("Data.txt", "a")
                file1.write(first_name+"\n")
                file1.close()
                break
            else:
                print("Invalid First Name")
        while True:
            last_name = input("Last Name: ")
            if last_name.isalpha():
                file1 = open("Data.txt", "w")
                file1.write(last_name+"\n")
                file1.close()
                break
            else:
                print("Invalid last Name")
        #E-mail input
        while True:
            email = input("E-mail: ")
            if re.fullmatch(email_regex, email):
                file1 = open("Data.txt", "a")
                file1.write(email+"\n")
                file1.close()
                break
            else:
                print("Invalid Email")
        #Password and password confirmation
        while True:
            print("Your Password Must have: ")
            print("1- at least one number.")
            print("2- at least one uppercase and one lowercase character.")
            print("3- at least one special symbol.")
            print("4- be between 6 to 20 characters long.")
            print("------------------------------------------------------")
            password = maskpass.askpass()
            if pass_regex.match(password):
                file1 = open("Data.txt", "a")
                file1.write(password+"\n")
                file1.close()
                break
            else:
                if len(password) < 6:
                    print("Too short Password..!")
                elif len(password) > 20:
                    print("Too long Password..!")
                elif not re.search(r'\d', password):
                    print("Password doesn't contain any number.")
                elif not re.search(r'[A-Z]', password):
                    print("Password doesn't contain any capital letter")
                elif not re.search(r'[a-z]', password):
                    print("Password doesn't contain any small letter")
                elif not re.search(r'[@$!%*#?&]', password):
                    print("Password doesn't contain any special character")
        while True:
            confirm_pass = maskpass.askpass(prompt= "Confirrm Password: ")
            if confirm_pass == password:
                break
            else:
                print("Doesn't Match with Password..!\nPlease, Reconfirm Your Password: ")
        #Mobile Phone
        while True:
            countries = ["Egypt", "England", "USA", "Spain", "Italy"]
            country = input("Choose a number to select Your Country: \n1-Egypt\n2-England\n3-USA\n4-Spain\n5-Ita1ly\n")
            if country not in countries:
                print("Invalid Input..!\n Please Choose your country from the list: ")
            else:
                #Egypt
                if country == "Egypt":
                    file1 = open("Data.txt", "a")
                    file1.write(country+"\n")
                    file1.close()
                    mobile_phone = input("Enter your phone number: +20")
                    if mobile_regexEg.match(mobile_phone):
                        break
                    else:
                        print("Invalid Phone Number..!\nRe-Enter a valid number: ")
                #England
                elif country == "England":
                    file1 = open("Data.txt", "a")
                    file1.write(country+"\n")
                    file1.close()
                    mobile_phone = input("Enter your phone number: +44")
                    if mobile_regexEn.match(mobile_phone):
                        break
                    else:
                        print("Invalid Phone Number..!\nRe-Enter a valid number: ")
                #USA
                elif country == "USA":
                    file1 = open("Data.txt", "a")
                    file1.write(country+"\n")
                    file1.close()
                    mobile_phone = input("Enter your phone number: +1")
                    if mobile_regexUS.match(mobile_phone):
                        break
                    else:
                        print("Invalid Phone Number..!\nRe-Enter a valid number: ")
                #Spain
                elif country == "Spain":
                    file1 = open("Data.txt", "a")
                    file1.write(country+"\n")
                    file1.close()
                    mobile_phone = input("Enter your phone number: +34")
                    if mobile_regexSp.match(mobile_phone):
                        break
                    else:
                        print("Invalid Phone Number..!\nRe-Enter a valid number: ")
                #France
                elif country == "Italy":
                    file1 = open("Data.txt", "a")
                    file1.write(country+"\n")
                    file1.close()
                    mobile_phone = input("Enter your phone number: +39")
                    if mobile_regexIt.match(mobile_phone):
                        break
                    else:
                        print("Invalid Phone Number..!\nRe-Enter a valid number: ")
                    
        print("Welcome", first_name, last_name, "from", country+"..!")
    def signin(self):
        while True:
            email = input("Please, Enter Your Email: \n")
            if re.fullmatch(email_regex, email):
                break
            else:
                print("Invalid Email")
        while True:
            password = maskpass.askpass()
            if pass_regex.match(password):
                break
            else:
                if len(password) < 6:
                    print("Too short Password..!")
                elif len(password) > 20:
                    print("Too long Password..!")
                elif not re.search(r'\d', password):
                    print("Password doesn't contain any number.")
                elif not re.search(r'[A-Z]', password):
                    print("Password doesn't contain any capital letter")
                elif not re.search(r'[a-z]', password):
                    print("Password doesn't contain any small letter")
                elif not re.search(r'[@$!%*#?&]', password):
                    print("Password doesn't contain any special character")
        readfile = open("Data.txt")
        data = readfile.readlines()
        users = []
        for i in data:
            users.append(i.strip("\n"))
        print(users)
        for user in users:
            userdetails = user.split(",")
            if userdetails[1] == email and userdetails[2] == password:
                print("Logged in Successfully")
                mainMenu.projectmenu(email)
                readfile.close()
                break
        else:
            print("User Doesnt Exit")
            self.login()
registration = Register()
registration.signup()
x = input("Do you want to signin?![y/n]")
if x == "y":
    registration.signin()
else:
    None
