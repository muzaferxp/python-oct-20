#============CRUD using Python==========
#contacts app

contactsList  =  ["persone1=9876543210", "person2=9654654654"]

#1---------------------------- create--------------------------------
contactsList.append("person3=9000577060")
contactsList.append("person4=9876543135")

#2----------------------- read  (retrive / access / fetch)----------

#get first person
print(contactsList[0])

#get last person
print(contactsList[-1])

#3---------------------------- update ---------------------------
contactsList[0] = "person1=1231231230"
contactsList[-1] = "person4=9876541564"
contactsList[1] = "person2=654973210"

print(contactsList)

#4----------------------------delete------------------
temp = []
itemToDelete = 0
i = 0
for x in contactsList:
    if itemToDelete  != i:
        temp.append(x)
    i = i + 1
    
contactsList = temp

print(contactsList)