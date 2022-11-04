#Data types

#1. String
name = "Adam"
print("Name: ", name)
print(type(name))

#2. Int
age = 25

#3. Float
balance = 1500.60

#4. Bool
status = True   # or False


#5. List  []    //array
fruitsList = ["Apple", "Mango", "Banana"]

fruitsList[0] = "Orange"
 
print(fruitsList)

#6. Dict  {}    //object
person = {
    "name" : "Adam",
    "phone" : "900577040"
}


#7.Tuple  ()   //
# It is same a list
# the only difference is that
# list is editable (mutable)
# tuple is not editable (immutable)

fruitsTuple = ("a", "c", "b")

#fruitsTuple[0] = "Orange"   #gets error coz it is not editable

print(fruitsTuple)


#8. set   {}
# removes duplicates
# sorting of items 
# not editable

fruitsSet = set(["c", "b", "a", "a", "c"])

print(fruitsSet)
