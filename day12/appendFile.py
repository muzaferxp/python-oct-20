#Append file is used to add new content to the existing file or create a new file
#in write methods, existing data is deleted and only new data is added to the file
#but in append method, old data is not deleted. just the new data is added to the file.


data = ["order 4", "order 5", "order 6"]

f = open("D:/PythonOct20/day12/file3.txt" ,    "a")

for line in data:
    f.write(line + "\n")

f.close() 
