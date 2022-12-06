person = {
    "firstName" : "Syed",
    "lastName"  : "Amer"
}


#create a function
def sayHello(name):   # formal param
    print("Hello", name)


def getFullName():
    return person['firstName'] + " " +  person['lastName']

#call
sayHello("Sam")  #passing the params  (actial params)

fullName = getFullName()
print(fullName)


arr = ["Blog 1"]

arr.append("Blog 2")
arr.append("Blog 3")
arr.append("Blog 4")
arr.append("Blog 5")

arr.reverse()


print(arr)

views = [50000, 80000, 900000, 45000, 265010]
views.sort()
views.reverse()
views.insert(0, 100000)
views.remove(900000)

print(views)

print(min(views))






