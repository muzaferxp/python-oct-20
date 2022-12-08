

file_path = "evaluation_code/data/hello.txt"

#1. Reading the txt File data
f = open(file_path, "r")
for line in f:
    print(line)
f.close()


#2. Write data 
f = open(file_path, "w")
f.write("New line 1 using white menthod\n")
f.close()

f = open(file_path, "w")
f.write("New line 2 different using white menthod\n")
f.close()


#3. Append data
f = open(file_path, "a")
f.write("New line added using append")
f.close()