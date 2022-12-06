person = {
    "name" : "adan",
    "city" : "Hyd",
    "country" : "India"
}

#1. add new field in person dict
person['phone'] = "9876543210"

#2. update existing field in person dict
person['name'] = "adam"

#3.remove field
person.pop("phone")

#4. accessing
print(person['name'])

#5. check if field exists in dict
if "phone" in person:
    print("Phone number exists")
else:
    print("Phone number does not exists")
print(person)

#6. loop over the dict
for field in person:
    print(field,  person[field])
    



