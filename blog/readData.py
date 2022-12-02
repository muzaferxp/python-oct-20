import json

path = "blogs.json"
def getData():
    #read the data from file
    f = open(path)
    data = json.load(f)
    f.close()
    return data
print(getData())