#Creator JS 10/11/2022
first_name = input("Please input your first name:")
last_name = input("Please input your last name:")

if first_name == "Jan" and last_name == "Salafia":          #If the inputs match "Jan" and "Salafia" Access will be granted
    print("Access Granted")
else:
    print("Access Denied")                                  #If not, access will be denied

full_name = first_name + " " + last_name                    #No issue with output except for needed space between first name and last name
print(full_name)