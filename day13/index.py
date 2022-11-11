
#        0         1         2
data = ["Apple", 'Mango', "Banana", "Orange", "Grapes"]
#         -3        -2        -1

#          start:end
#print(data[ 1  :  3 ])

#data.reverse()

data.sort()

data.append("Kiwi")

print(data)

if "WM" in data:
    data.remove("WM")

try:
    data.remove("something")
except Exception as e:
    print("Could not remove something because ", e)

print(data)



person = {
    "name" : "Adam",
    "age" : 25
}

if "age" in person:
    print(person['age'])


print("-------END------")

















