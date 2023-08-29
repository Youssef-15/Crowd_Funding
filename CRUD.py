import re
from datetime import datetime
from tkinter import *

print("------------Project------------")
#TKinter window
#root = Tk()
#root.geometry("500x500")
#root.title("My App")root.config()
file1 = open("Project.txt", "a")
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
            data = readfile.readlines()
            #print(data)
            projects = []
            projectsdetails = []
            for i in data:
                projects.append(i.strip("\n"))
              #  x = i.index() 
               # x += 1
            #print("------first_try--------")
            print (projects)
            #x = 0
            #for x in projects:
             #   project = projects[x]
                #projectsdetails = project.split(",")
                #project.index() += 1
            #print("------second_try--------")
            #print(projectsdetails)
              #  if project == project_title:
               #     print(project)
                #else:
                 #   x = x+1
                    #print("----------------Projects----------------")
             #   print(f"{project_title}")
              #  readfile.close()
            #else:
             #   print("The Project you're searching for is not found..!")


#root.mainloop()
#project = Create()
#project.create()
#print("---------view Mode---------")
#view = View_Project()
#view.reading()
print("---------Search Mode---------")
investigate = Search()
investigate.search()