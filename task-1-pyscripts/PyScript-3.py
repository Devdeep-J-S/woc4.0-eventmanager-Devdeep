# Python ContactKeeper:

# You are asked to write a terminal based program in Python to store, manage and retrieve contacts.

# Make sure the user is well directed about how to use your program.

# Storage:
# -- Each record should consist of two fields, namely ‘name’ and ‘contact number’.
# -- Find a way to store multiple contacts of a person.
# -- Use a data structure of your choice.

# Management:
# -- The contacts should be arranged w.r.t. the alphabetical order of their names, at any point of time.

# Retrieval:
# -- Make the required arrangements so that whenever the user searches for a key word, (s)he gets a collection of names which include that key word.
# -- Further let him/her select a name and lastly, output the contact number of the selected person.

# -- Also give an option to view all contacts.


import os, time, string, random


#functions that will be used

#to view the content in data base 
def view_all_contacts():
    fhand = open("databaseForContactkeeper.txt", "r")
    for lines in fhand:
        temp_list = lines.split(" ")
        print("Name:" + temp_list[0] + " " * (15 - len(temp_list[0])) +
              "Contact number: ",
              end="")
        print(temp_list[1:len(temp_list) - 1])

# to get dictionary form database 
def get_dictionary_from_database():
    fhand = open("databaseForContactkeeper.txt", "r")
    di = dict()
    for lines in fhand:
        temp_list = lines.split(" ")
        di[temp_list[0]] = list()
        di[temp_list[0]] = temp_list[1:(len(temp_list) - 1)]
    return di

# to arrange the contacts w.r.t. the alphabetical order of their names
def manage_dictionary(di):
    temp_di = dict()
    for i in sorted(di):
        temp_di[i] = di[i]
    fhand = open("databaseForContactkeeper.txt", "w")
    for x, y in temp_di.items():
        fhand.write(x + " ")
        temp_list = y
        for i in temp_list:
            fhand.write(str(i) + " ")
        fhand.write("\n")

# to add a contact 
def insert_contect():
    di = get_dictionary_from_database()
    name = input("Enter name:")
    #for insert
    try:
        ask = int(input("How many contact numbers do you want to add for this name?     "))
    except:
        print("Please Enter number only")    
        return
    for i in range(0, ask):
        i = input("Enter contact number : ")
        if name not in di:
            di[name] = list()
            di[name].append(i)
        else:
            di[name].append(i)
    manage_dictionary(di)

# to search contact by name 
def serach_by_name():
    name = input("Enter the name you want to search in Contact keeper : ")
    di = get_dictionary_from_database()
    if name in di.keys():
        print("Name : " + name + " Contact number : ", end="")
        for i in di[name]:
            print(i + " ", end="")
        print("\n")
    else:
        print("No search result")

# to search contact by key word 
def search_by_keyword():
    keyWord = input(
        "Enter the key word you want to search in Contact keeper : ")
    di = get_dictionary_from_database()
    temp_list = list()
    for i in di.keys():
        if keyWord in i:
            temp_list.append(i)
    if len(temp_list) == 0:
        print("Key Word not found")
    else:
        print(
            "Please select the name that you wanted to search from this list : "
        )
        print(temp_list)
        serach_by_name()


# welcoming page
print(
    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
)
print(
    "\t\t\t\t@@ _______________________________________________________________________________________ @@"
)
print(
    "\t\t\t\t@@|                                           		                                  |@@"
)
print(
    "\t\t\t\t@@|                                           		                                  |@@"
)
print(
    "\t\t\t\t@@|                                           		                                  |@@"
)
print(
    "\t\t\t\t@@|                                           		                                  |@@"
)
print(
    "\t\t\t\t@@|                                           		                                  |@@"
)
print(
    "\t\t\t\t@@|                                           		                                  |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|                                 Python Contact Keeper                                 |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|                                                                                       |@@"
)
print(
    "\t\t\t\t@@|_______________________________________________________________________________________|@@"
)
print(
    "\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n\t\t\t\t\t"
)
time.sleep(5)
command = 'clear'
if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
os.system(command)

while(True):
    print ("Menu to use Contact keeper :\n Please Enter number to do respective thing in menu: \n1. Insert Contact\n2. View all contacts\n3. Search by name\n4. Search by Key word\n5. To exit the code\n")
    i = input ("Enter the number : ")
    if (i=="1"):
        insert_contect()
    elif (i=="2"):
        view_all_contacts()
    elif (i=="3"):
        serach_by_name()
    elif (i=="4"):s
        search_by_keyword()
    elif(i=="5"):
        exit()
    else:
        print("Please enter the number given in Menu.")            
                
    