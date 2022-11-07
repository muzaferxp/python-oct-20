
data = ["line 1", "line 2", "line 3"]

f = open("D:/PythonOct20/day12/file2.txt" ,    "w")

for line in data:
    f.write(line + "\n\n")

f.close() 