myList = ["A", "B"]
print(myList)

#create
myList.append("D")
print("Added D to the list")
#read
print(myList)

#update
myList[-1] = "C"
print("Updated the last item")
print(myList)

#delete
myList.remove("B")
print("Removed B from the list")

print(myList)