# Crowd_Funding
authentication and CRUD operation system
                                                										Documentation
                                                										=============
This Project is crowd_dunding, Crowdfunding is a form of crowd-sourcing and alternative finance.
This Project is divided into 2 partitions first partition which is authentication and second partition which is CRUD that is the core of the project in which you can create, read, Search
or delete information from your file.

I-Authentication
=================
	a)Regestration:
	===============
	in authentication you can register to the project and fill the form with your info start_name, last_name, your email, password and phone number 
	and to make all of that we use (regex, maskpass) libraries, lists, (isalpha, join) methods, write and append in file, while and for loops, and if statements.

	b)Signin:
	=========
	in signin page we could enter the email and password that we have registerd before to login the project and we have used regex and maskpass libraries, lists, while and for loops,
	if conditions, read method and open function, (split, strip) methods 

II-CRUD
========
	a)Project Class:
	================
	this is the parent class that all classes inherit from it we only defined attributes that will be inhereted from it.	

	b) Create
	=========
	in this class we inherit information from Project class and take thier values from the user as input so we've set a title, details, total target and start and end time values, and
	after taking these inputs from the user we wrote them in a file and we have used (super, isalpha, isnumeric, split, join) methods, while loops, if conditions, try..except handling
	blocks regex, datetime libraries and thier methods, write in file, lists. 
	
	c)View:
	=======
	is class that helps user to view/read the info that are found in the project, we've used only (read method, open function).

	d)Search:
	=========
	Search class contain search function that helps you to find the details or the info about the project you're looking for, and we've used if conditions, while and for loops, 
	read method and open function, isalpha method and lists.
	
	e)Delete:
	=========
	delete is class that contain deleting function that delete the project you want, we've used same tools that we've used in search function and we only added a write function to
	replace the wriiten info with white spaces.
