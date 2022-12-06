#================SPLIT=================

file1 = "sample.model.txt"
file2  = "sample.info.csv"
file3  = "sample.info.json"

def getFileExt(name):
    partsList = name.split(".")
    
    #getting last item from list
    if partsList[-1] == "csv":
        print("This file extension is a csv, opening using csv reader")
    elif partsList[-1] == "txt":
        print("This file extension is a txt, opening notepad")
    elif partsList[-1] == "json":
        print("This file extension is a json, opening using json reader")
    
    


getFileExt(file1)
getFileExt(file2)
getFileExt(file3)


#===========REPLACE==================
adhar = "5778 1728 1333"

adhar = adhar.replace(" ", "")

print(adhar)


#==========STRIP====================
adhar = "    91 9876543210      "
adhar= adhar.strip()   #to remove the extra spaces

print(adhar)
print(len(adhar)) #91 9876543210

name = "$adam$ ^"

name = name.strip("$ ^")

print(name)
#==============JOIN=========
arr = ["a", "b" , "c"]

print(arr)
print(",".join(arr))  # join converts the arr to str