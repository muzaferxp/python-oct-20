person = {
    "name" : "Adam"
}

print(person)

person['phoneNumber']  = 9876543210

person["name"] = "New Name"
person['name'] = "Sam"

print(list(person.keys()))
print(list(person.values()))