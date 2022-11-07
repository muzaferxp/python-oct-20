

email = "test2@123.com"
password= "test456"

f = open("D:/PythonOct20/day12/example.csv")
                              
for line in f:                            
    details = line.split(",")                     
    if details[0] == email:                   
        print("Email found in data")
        if details[1] == password:
            print("Password is correct")
            print("Logged in successfully")
        else:
            print("Password is not correct")
    
    
f.close()

