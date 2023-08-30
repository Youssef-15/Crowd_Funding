import re
from datetime import datetime
from tkinter import *

print("------------Project------------")
#TKinter window
#root = Tk()
#root.geometry("500x500")
#root.title("My App")root.config()
file1 = open("Project.txt", "a")
date1 = r'^\d{2}/\d{2}/\d{4}$'
class Project:
    title = ""
    details = ""
    total_target = 0
    start_time = "01/01/2001"
    end_time = "01/01/2001"

class Create(Project):
    def create(self):
        while True:
            super().title
            title = input("Title: ")
            if title.isalpha():
                break
            else:
                print("Invalid Title, Title must be only alphabets!!")
        while True:
            super().details
            details = input("Project Details: ")
            words = details.split(" ")
            if len(words) > 5:
                break
            else:
                print("you must write more than 20 Words")
        while True:
            super().total_target
            total_target = input("Total Target: ")
            if total_target.isnumeric():
                break
            else:
                print("Invalid Input..! Please, enter only numbers: ")
        while True:
            super().start_time
            try:
                start_time = input("Start Date: ")
                start_date = datetime.strptime(str(start_time), "%d/%m/%Y")
                today_date = datetime.today()
                if today_date > start_date:
                    print("Start date can't be before",today_date)
                else:
                    break
            except ValueError:
                print("Invalid start date format. Please enter in dd/mm/yyyy format.")

        while True:
            super().end_time
            try:
                end_time = input("End Date: ")
                end_date = datetime.strptime(str(end_time), "%d/%m/%Y")
                if start_date > end_date:
                    print("End date can't be before",start_date)
                else:
                    break
            except ValueError:
                print("Invalid end date format. Please enter in dd/mm/yyyy format.")

        info = "".join([title,"\n",details,"\n", total_target,"\n", str(start_date),"\n", str(end_date)])
        info=info+"\n"
        file1.write(info)
        file1.close()
#        print("[", title, details, total_target, start_date, end_date, "]")

class View_Project(Project):
    def reading(self):
        read = open("Project.txt", "r")
        print(read.read())

class Search(Project):
    def search(self):
        while True:        
            print("Search by:")
            print("1- Title")
            print("2- Date")
            choice = input("Choose 1 or 2: ")
            if choice == "1":
                while True:
                    project_title = input("Enter the Title of the project you're searching for: ")
                    if project_title.isalpha():
                        break
                    else:
                        print("Invalid title..!")
                readfile = open("Project.txt", "r")
                data = readfile.read()
                filelist = data.splitlines()
                for files in filelist:
                    start = filelist.index(files)
                    end = start + 5
                    if files == project_title:
                        for x in range(start, end):
                            print(filelist[x])
                        readfile.close()
            #elif choice == "2":
             #   while True:
              #      project_start = input("Enter the Start Date of the project you're searching for: ")
               #     if re.match(date1, project_start):
                #        break
                 #   else:
                  #      print("Invalid date..!")
                #readfile = open("Project.txt", "r")
                #data = readfile.read()
                #filelist = data.splitlines()
                #for files in filelist:
                 #   start = filelist.index(files)
                  #  end = start + 5
                   # print(start, end)
                    #if files == project_start.date():
                     #   for x in range(start, end):
                      #      print(filelist[x])
                       # readfile.close()

class Delete(Search):
    def deleting(self):
        while True:
            del_file = input("Enter the name of the file you want to delete: ")
            if del_file.isalpha():
                break
            else:
                print("Invalid title..!")
                readfile = open("Project.txt", "r")
                data = readfile.read()
                filelist = data.splitlines()
                for files in filelist:
                    start = filelist.index(files)
                    end = start + 4
                    if files == del_file:
                        for x in range(start, end):
                            writefile = open("Project.txt", "w")
                            filelist[x]
                            writefile.write("".join(filelist))
                        writefile.close()
                        readfile.close()
            print(filelist)
                
#root.mainloop()
print("---------Create Mode---------")
project = Create()
project.create()
print("---------view Mode---------")
view = View_Project()
view.reading()
print("---------Search Mode---------")
investigate = Search()
investigate.search()
print("---------Delete Mode---------")
removing = Delete()
removing.deleting()
print("---------view Mode---------")
view = View_Project()
view.reading()